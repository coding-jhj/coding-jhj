<div align="center">

# Hi, I'm Jeong Hwan Ju

### AI Agent, Data, Android, and Product-minded Builder

I build small but working products from idea to deployment: AI agents, on-device computer vision, public-data dashboards, and playable web experiences.

[![GitHub](https://img.shields.io/badge/GitHub-coding--jhj-181717?style=for-the-badge&logo=github)](https://github.com/coding-jhj)
[![Portfolio Focus](https://img.shields.io/badge/Focus-AI%20Agents%20%7C%20Data%20%7C%20Android-2563eb?style=for-the-badge)](#featured-projects)
[![Open Source](https://img.shields.io/badge/Public%20Repos-8-22c55e?style=for-the-badge)](https://github.com/coding-jhj?tab=repositories)

</div>

---

## What I Build

I like projects that do something end-to-end:

- AI agents that can search, analyze repositories, and explain their reasoning
- Android AI apps that run inference on-device instead of sending camera frames to a server
- Data pipelines that collect, clean, visualize, and deploy automatically
- Lightweight web games and interactive demos that can be opened immediately in the browser

```txt
Idea
  -> prototype
  -> working backend / app / dashboard
  -> deployment
  -> README, demo, and evidence
```

## Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white" />
  <img src="https://img.shields.io/badge/Android-3DDC84?style=flat-square&logo=android&logoColor=white" />
  <img src="https://img.shields.io/badge/TensorFlow%20Lite-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/YOLO-111111?style=flat-square" />
  <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=111111" />
  <img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" />
  <img src="https://img.shields.io/badge/Google%20Cloud%20Run-4285F4?style=flat-square&logo=googlecloud&logoColor=white" />
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square" />
</p>

## Featured Projects

### VoiceGuide

> On-device AI walking assistant for visually impaired users

[Repository](https://github.com/coding-jhj/VoiceGuide) | [Live Dashboard](https://voiceguide-1063164560758.asia-northeast3.run.app/dashboard)

VoiceGuide detects obstacles on an Android device with YOLO/TFLite, gives Korean TTS and vibration feedback, and sends only detection JSON/GPS data to a FastAPI dashboard. The project includes Android inference, server APIs, real-time dashboarding, tests, public-data scenario generation, and deployment.

**Highlights**

- Android CameraX + TFLite YOLO on-device inference
- Korean TTS, vibration patterns, voice-command modes, and offline guidance behavior
- FastAPI server with detection, GPS, history, SSE, route, and dashboard endpoints
- Public-data scenario for safer walking-route comparison around accessibility facilities
- Cloud Run deployment and automated test coverage

### RepoPilot

> Free GitHub repository analysis agent MVP

[Repository](https://github.com/coding-jhj/RepoPilot) | [Live Demo](https://jeonghwanju-repopilot.hf.space/) | [Code Guide](https://coding-jhj.github.io/RepoPilot/)

RepoPilot clones a public GitHub repository, indexes source files, retrieves relevant code chunks, runs deterministic static-analysis checks, and drafts patch suggestions with file/line evidence. It is designed as a free-first MVP without paid LLM APIs, paid vector databases, or GPU hosting.

**Highlights**

- FastAPI backend and Next.js static UI
- Python AST parsing and lightweight JS/TS symbol extraction
- Local retrieval over indexed code chunks
- Evidence-backed findings and patch-draft workflow
- Hugging Face Spaces deployment

### StelLive Data Dashboard

> Automated data collection and visualization dashboard

[Repository](https://github.com/coding-jhj/Stelive_data) | [Live Dashboard](https://coding-jhj.github.io/Stelive_data/)

StelLive Data Dashboard collects YouTube and CHZZK data, stores it as structured JSON/CSV, and publishes a web dashboard through GitHub Pages. It also uses GitHub Actions for scheduled collection and deployment.

**Highlights**

- YouTube API and CHZZK data collection
- Streams, music, collaborations, followers, subscribers, videos, and clip data
- GitHub Actions automation
- Static dashboard deployment with GitHub Pages

### AI Search Agent

> ReAct-style search agent with FastAPI and LangChain

[Repository](https://github.com/coding-jhj/AI_AGENT) | [Live Demo](https://jeonghwanju-ai-search-agent.hf.space)

AI Search Agent receives a user question, decides whether web search is needed, searches through DuckDuckGo, analyzes the results, and returns an answer. It demonstrates a practical ReAct loop using a free deployment setup.

**Highlights**

- Gemini 2.0 Flash, LangChain ReAct, DuckDuckGo search
- FastAPI server with a small built-in web UI
- Hugging Face Spaces Docker deployment
- Privacy-aware design: user API keys are not stored on the server

### Arkan: Forgotten Throne

> Single-file browser RPG

[Repository](https://github.com/coding-jhj/ARKAN_FORGOTTEN_THRONE) | [Play](https://coding-jhj.github.io/ARKAN_FORGOTTEN_THRONE/ARKAN-FORGOTTEN-THRONE.html)

A fantasy RPG built with HTML, CSS, and vanilla JavaScript. It includes a world map, party selection, shops, NPCs, dungeon movement, turn-based combat, character stats, and a playable GitHub Pages deployment.

**Highlights**

- No build step and no external runtime required
- Turn-based battle system and party composition
- Pixel-style browser UI
- Instant play through GitHub Pages

## Project Map

| Area | Projects | What it shows |
| --- | --- | --- |
| Accessibility AI | [VoiceGuide](https://github.com/coding-jhj/VoiceGuide) | Android AI, TFLite, safety UX, FastAPI, public data |
| AI Agents | [RepoPilot](https://github.com/coding-jhj/RepoPilot), [AI_AGENT](https://github.com/coding-jhj/AI_AGENT) | Agent workflow, retrieval, ReAct, deployment |
| Data Products | [Stelive_data](https://github.com/coding-jhj/Stelive_data) | Data collection, visualization, GitHub Actions |
| Web Experience | [ARKAN_FORGOTTEN_THRONE](https://github.com/coding-jhj/ARKAN_FORGOTTEN_THRONE) | Interactive browser app, game logic, GitHub Pages |
| Learning Log | [Review-Estcamp-AI-Human](https://github.com/coding-jhj/Review-Estcamp-AI-Human) | Study review and course notes |

## GitHub Stats

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=coding-jhj&show_icons=true&theme=tokyonight&hide_border=true&rank_icon=github" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=coding-jhj&layout=compact&theme=tokyonight&hide_border=true" />

<br />

<img src="https://github-readme-activity-graph.vercel.app/graph?username=coding-jhj&theme=tokyo-night&hide_border=true" />

</div>

## Current Direction

I am especially interested in:

- Building AI agents that produce evidence, not just text
- Making AI useful on real devices with latency and privacy constraints
- Turning public data into clear product decisions
- Shipping small demos that people can immediately open and understand

---

<div align="center">

### Thanks for visiting

If a project here looks interesting, the best place to start is [VoiceGuide](https://github.com/coding-jhj/VoiceGuide) for full-stack AI accessibility work or [RepoPilot](https://github.com/coding-jhj/RepoPilot) for AI-agent architecture.

</div>