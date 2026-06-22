# Notion 자동 동기화 셋업 (5분)

GitHub 레포가 바뀌면 Notion 포트폴리오 DB가 자동으로 갱신되도록 연결합니다.
워크플로(`.github/workflows/notion-sync.yml`)와 스크립트(`scripts/notion_sync.py`)는 이미 들어가 있습니다.
**아래 토큰·시크릿 등록만** 하면 작동합니다.

## 1. Notion Integration 토큰 발급

1. https://www.notion.so/my-integrations 접속 → **New integration**
2. 이름: `github-sync`, 연결 워크스페이스 선택 → 생성
3. **Internal Integration Secret**(`secret_...` 또는 `ntn_...`) 복사

## 2. Integration 을 DB에 연결

1. Notion에서 **coding-jhj · AI 엔지니어 포트폴리오 → Projects** 데이터베이스 페이지 열기
2. 오른쪽 위 `···` → **Connections**(연결) → 방금 만든 `github-sync` 추가

> 이 단계를 빠뜨리면 토큰이 있어도 API가 DB를 못 봅니다 (가장 흔한 실패 원인).

## 3. GitHub Secrets 등록

`coding-jhj/coding-jhj` 레포 → **Settings → Secrets and variables → Actions → New repository secret**

| Name | Value |
|---|---|
| `NOTION_TOKEN` | 1번에서 복사한 Integration Secret |
| `NOTION_DB_ID` | `038f49fc43ac4d6daafaab829b1fec3b` |

## 4. 실행

- 레포 **Actions** 탭 → **Sync repos to Notion** → **Run workflow** (수동 1회 테스트)
- 이후 **매일 09:00 KST 자동 실행** + 워크플로/스크립트 수정 push 시 실행

## 무엇이 동기화되나

| 자동 갱신 (스크립트가 덮어씀) | 수동 유지 (절대 안 건드림) |
|---|---|
| GitHub URL, Demo, Stars, Language, Status, Last Synced | Category, One-liner(기존), Highlight, Stack |

- 새 레포를 만들면 → Notion에 카드 자동 생성 (이름·설명·링크·언어·별)
- 기존 카드의 직접 작성한 소개·하이라이트는 보존됩니다.

## 동작 원리 (한 줄)

`scripts/notion_sync.py` 가 GitHub API로 레포 목록을 읽고, Notion API로 이름 매칭하여 upsert합니다.
LLM·외부 서비스 없이 표준 REST 호출만 사용합니다.

---

## 부록 — 워크플로 파일 직접 추가

> PAT에 `workflow` 권한이 없어 자동 추가가 막혔습니다. 아래를 직접 넣어주세요 (1분).

레포 **Actions 탭 → New workflow → set up a workflow yourself** → 파일명 `notion-sync.yml` → 아래 붙여넣기 → Commit:

```yaml
name: Sync repos to Notion
on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch: {}
  push:
    branches: [main]
    paths: [".github/workflows/notion-sync.yml", "scripts/notion_sync.py"]
jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Sync to Notion
        env:
          NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
          NOTION_DB_ID: ${{ secrets.NOTION_DB_ID }}
          GH_USER: coding-jhj
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: python scripts/notion_sync.py
```
