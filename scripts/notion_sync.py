#!/usr/bin/env python3
"""
GitHub repos -> Notion "Projects" DB 자동 동기화.

동작:
- coding-jhj 의 public repo 목록을 GitHub API 로 가져온다.
- Notion DB 에서 "Name" 으로 기존 카드를 찾는다.
- 있으면: GitHub/Demo/Stars/Language/Status/Last Synced 만 갱신 (수동 작성 필드 보존).
- 없으면: 새 카드 생성 (Name, One-liner=description, GitHub, Stars, Language, Status, Last Synced).

수동으로 채운 Category / Highlight / Stack / One-liner(기존) 은 절대 덮어쓰지 않는다.

환경 변수:
  NOTION_TOKEN   Notion internal integration token (secret_xxx)
  NOTION_DB_ID   Projects 데이터베이스 ID
  GH_USER        GitHub username (기본: coding-jhj)
  GITHUB_TOKEN   (선택) rate limit 완화용. Actions 가 자동 주입.
"""
import os
import sys
import datetime
import urllib.request
import urllib.error
import json

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
NOTION_DB_ID = os.environ["NOTION_DB_ID"]
GH_USER = os.environ.get("GH_USER", "coding-jhj")
GH_TOKEN = os.environ.get("GITHUB_TOKEN")

NOTION_VERSION = "2022-06-28"
TODAY = datetime.date.today().isoformat()


def http(url, method="GET", headers=None, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=headers or {})
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} {method} {url}\n{e.read().decode()}", file=sys.stderr)
        raise


def gh_repos():
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "notion-sync"}
    if GH_TOKEN:
        headers["Authorization"] = f"Bearer {GH_TOKEN}"
    repos, page = [], 1
    while True:
        url = f"https://api.github.com/users/{GH_USER}/repos?per_page=100&page={page}&type=owner&sort=updated"
        batch = http(url, headers=headers)
        if not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    # profile readme repo 제외
    return [r for r in repos if r["name"].lower() != GH_USER.lower()]


def notion_headers():
    return {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def notion_existing():
    """{name_lower: page_id} 매핑."""
    out, cursor = {}, None
    while True:
        body = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        res = http(
            f"https://api.notion.com/v1/databases/{NOTION_DB_ID}/query",
            method="POST", headers=notion_headers(), body=body,
        )
        for p in res["results"]:
            t = p["properties"].get("Name", {}).get("title", [])
            name = "".join(x.get("plain_text", "") for x in t).strip()
            if name:
                out[name.lower()] = p["id"]
        if not res.get("has_more"):
            break
        cursor = res["next_cursor"]
    return out


def status_for(repo):
    if repo.get("archived"):
        return "Archived"
    if repo.get("homepage"):
        return "Live"
    return "Active"


def base_props(repo):
    """동기화로 갱신하는 필드만. 수동 필드는 포함하지 않음."""
    props = {
        "GitHub": {"url": repo["html_url"]},
        "Stars": {"number": repo.get("stargazers_count", 0)},
        "Status": {"select": {"name": status_for(repo)}},
        "Last Synced": {"date": {"start": TODAY}},
    }
    if repo.get("homepage"):
        props["Demo"] = {"url": repo["homepage"]}
    if repo.get("language"):
        props["Language"] = {"rich_text": [{"text": {"content": repo["language"]}}]}
    return props


def main():
    repos = gh_repos()
    existing = notion_existing()
    print(f"GitHub repos: {len(repos)} | Notion cards: {len(existing)}")
    for r in repos:
        name = r["name"]
        props = base_props(r)
        pid = existing.get(name.lower())
        if pid:
            http(f"https://api.notion.com/v1/pages/{pid}", method="PATCH",
                 headers=notion_headers(), body={"properties": props})
            print(f"  updated: {name}")
        else:
            props["Name"] = {"title": [{"text": {"content": name}}]}
            if r.get("description"):
                props["One-liner"] = {"rich_text": [{"text": {"content": r["description"][:1900]}}]}
            http("https://api.notion.com/v1/pages", method="POST",
                 headers=notion_headers(),
                 body={"parent": {"database_id": NOTION_DB_ID}, "properties": props})
            print(f"  created: {name}")
    print("done.")


if __name__ == "__main__":
    main()
