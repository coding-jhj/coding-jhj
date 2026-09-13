AI SYSTEMS · EVALUATION · DEPLOYMENT

# Jeong Hwan Ju

**Post-training Research Engineer**

> Building evaluation-driven AI systems with grounded generation, explicit safety boundaries, and deployment-aware engineering.

---

**PROOF AT A GLANCE**

| **03** | **01** | **08** |
| --- | --- | --- |
| TEAM PROJECTS | AWARD-WINNING LEAD | INDEPENDENT WORKS |

[Selected Work](#selected-work) · [Research Direction](#research-direction) · [Independent Work](#independent-work) · [GitHub](https://github.com/coding-jhj)

## Profile Snapshot

> **Direction**  
> **Post-training Research Engineer** · Research engineering preparation
>
> **Recognition**  
> **Minister of Employment and Labor Award** · [Lease-Companion](https://github.com/coding-jhj/Lease-Companion) · Team Lead, AI/LLM
>
> **Selected Work**  
> **Lease-Companion** · VoiceGuide · Rainbow Bridge

## Selected Work

Three team projects first — each one shows a different way I turn AI systems into useful, testable products.

### 01 / Recognition · [Lease-Companion](https://github.com/coding-jhj/Lease-Companion)

**Awarded contract analysis assistant | Team Lead, AI/LLM**

A contract review assistant for first-time tenants. It combines document extraction, cross-document validation, official-source retrieval, and a Python rule engine to provide evidence-backed questions and actions instead of unsafe legal or safety claims.

**STACK**

`Document AI` · `Rule Engine` · `RAG` · `Privacy` · `Evaluation`

**Offline evidence:** `Contract checks · 100/100` · `Judgment cases · 47/47`

> Fixed offline test data; not real-world contract coverage.

[Repository](https://github.com/coding-jhj/Lease-Companion) · [Evaluation Plan](https://github.com/coding-jhj/Lease-Companion/blob/main/docs/ai/evaluation-plan.md)

---

### 02 / On-device AI · [VoiceGuide](https://github.com/coding-jhj/VoiceGuide)

**Walking assistant for blind and low-vision users**

An Android system that runs YOLO/TFLite obstacle detection on device camera frames, then delivers stable risk-aware haptic feedback, Korean TTS, and audio cues. The system connects FastAPI, GPS events, SSE, and a Cloud Run dashboard without sending raw frames to the server.

**STACK**

`Android` · `Kotlin` · `TFLite` · `YOLO` · `FastAPI` · `Accessibility`

[Repository](https://github.com/coding-jhj/VoiceGuide)

---

### 03 / AI Infrastructure · [Rainbow Bridge](https://github.com/mosejong/Rainbow-Bridge/tree/jeonghwanju)

**AI and infrastructure contributor | Contribution branch: `jeonghwanju`**

Contributed to Qwen3 GPU TTS with asynchronous execution, tone mapping, STT/Gemini evaluation, recovery scoring, backend TTS and timeline flows, PM2 operations, and the demo video generation pipeline.

**STACK**

`Qwen3 TTS` · `GPU Service` · `Evaluation` · `PM2` · `Backend`

[Contribution Branch](https://github.com/mosejong/Rainbow-Bridge/tree/jeonghwanju)

## Research Direction

### 01 / Foundation model lab

**Work:** **[foundation-model-lab](https://github.com/coding-jhj/foundation-model-lab)**

**What it demonstrates:** Reproducible decoder-only language model experiments covering tokenizers, causal self-attention, compact Transformers, checkpoints, validation loss, generation, and experiment records. **This is a foundation for research engineering and pre-training work, not a claim of completed post-training results.**

---

### 02 / Execution workspace

**Work:** **[MY_CAREER_PLANNER](https://github.com/coding-jhj/MY_CAREER_PLANNER)**

**What it demonstrates:** A Plan → Do → See workspace for research goals, execution logs, reviews, and measurable next experiments. It documents my preparation for **Post-training Research Engineer** work.

---

### 03 / Local-model direction

**Work:** **Lease-Companion comparison track**

**What it demonstrates:** An optional 7B 4-bit QLoRA comparison track. The current repository contains preprocessing, configuration, and evaluation scaffolding; **no trained weights or checkpoint are presented as completed results.**

## Independent Work

Independent work is not a list of ideas. It is a record of implementing analysis, search, security, operations, and failure handling.

**CODE ANALYSIS · AGENT**

### 01 / [RepoPilot](https://github.com/coding-jhj/RepoPilot)

**Evidence-grounded repository analysis agent**

Accepts a public GitHub URL, indexes the files, and analyzes Python, JavaScript, and TypeScript structure with static rules. Results retain file-and-line evidence, patch drafts, scope validation, and an optional PR flow.

`FastAPI` · `Next.js` · `Static Analysis` · `Evidence`

[Demo](https://jeonghwanju-repopilot.hf.space/) · [Code Guide](https://coding-jhj.github.io/RepoPilot/repopilot-code-guide.html)

---

**PERSONAL KNOWLEDGE · RAG**

### 02 / [Personal-AI-Studio](https://github.com/coding-jhj/Personal-AI-Studio)

**Source-grounded personal AI workspace**

Unifies documents, code, notebooks, spreadsheets, photo metadata, and MongoDB into one knowledge base. It shows local retrieval results as source cards and connects voice input with a local fallback when an external LLM fails.

`Streamlit` · `TF-IDF` · `Voice` · `Fallback`

[Demo](https://jeonghwanju-personal-ai-studio.hf.space)

---

**WEB SEARCH · REACT LOOP**

### 03 / [AI_AGENT](https://github.com/coding-jhj/AI_AGENT)

**Agent that decides when search is needed**

Analyzes a question, decides whether to search, observes DuckDuckGo results, and continues with another search or an answer through a ReAct loop. It provides a FastAPI API and browser UI without storing the user-provided key on the server.

`Gemini` · `LangChain` · `DuckDuckGo` · `FastAPI`

[Demo](https://jeonghwanju-ai-search-agent.hf.space)

---

**DATA PIPELINE · OPERATIONS**

### 04 / [Stelive_data](https://github.com/coding-jhj/Stelive_data)

**Data product from collection to deployment**

Regularly collects YouTube Data API and CHZZK data, builds JSON and CSV history, regenerates the dashboard, and deploys it to GitHub Pages. The repository captures a repeatable operational flow across different external sources.

`Python` · `GitHub Actions` · `JSON/CSV` · `GitHub Pages`

[Dashboard](https://coding-jhj.github.io/Stelive_data/)

---

**DEVELOPER TOOLING · SAFETY**

### 05 / [claude-pwsh-kit](https://github.com/coding-jhj/claude-pwsh-kit)

**Claude Code harness for Windows and PowerShell**

Combines dangerous-command blocking, keyword-based skill routing, research verification guidance, and eight subagent templates. It documents non-ASCII encoding and PowerShell pipe issues and checks them with regression tests.

`PowerShell` · `Safety Hooks` · `Skill Router` · `MIT`

---

**SECURITY · PASSWORDLESS AUTH**

### 06 / [Passkey Private Portfolio](https://github.com/coding-jhj/aleph-first-homework)

**One service connecting a public portfolio and private workspace**

Uses WebAuthn passkeys and separates account-scoped private data through a Vercel API and Supabase PostgreSQL. The security boundary covers challenge replay prevention, session protection, account-scope checks, and RLS.

`WebAuthn` · `Vercel` · `Supabase` · `RLS`

---

**RELIABILITY · DATA PRODUCT**

### 07 / [Real Information Board](https://github.com/coding-jhj/ALPEH_FIFTH_HOMEWORK)

**A dashboard that explains failures honestly**

[ALPEH_FIFTH_HOMEWORK](https://github.com/coding-jhj/ALPEH_FIFTH_HOMEWORK) and [MINECRART_DASHBOARD](https://github.com/coding-jhj/MINECRART_DASHBOARD) distinguish timeout, authentication rejection, rate limits, offline status, and schema changes while preserving the last known good value. Live requests and replay fixtures share the same core path, with nine fixtures covering failure and recovery.

`Next.js` · `TypeScript` · `Supabase` · `Replay`

[Demo](https://t04-real-information-board.vercel.app)

---

**CREATIVE ENGINEERING · BROWSER GAME**

### 08 / [ARKAN_FORGOTTEN_THRONE](https://github.com/coding-jhj/ARKAN_FORGOTTEN_THRONE)

**A turn-based RPG playable directly in the browser**

Connects the world map, town, guild, shop, NPC, dungeon, battle, compendium, and equipment-upgrade flows through static hosting. It includes a Canvas pixel background, modular code, responsive mobile layout, and headless QA for battles, saves, and progression gates.

`HTML/CSS/JS` · `Canvas` · `Responsive` · `Playwright`

[Play](https://coding-jhj.github.io/ARKAN_FORGOTTEN_THRONE/)

## Toolkit

**TOOLS**

`Python` · `FastAPI` · `Pydantic` · `PostgreSQL` · `Chroma` · `BM25` · `Gemini` · `RAG` · `QLoRA`

`Kotlin` · `Android` · `TFLite` · `React` · `TypeScript` · `Docker` · `GitHub Actions`

## All Public Repositories

<details>
  <summary><strong>Explore all 23 public repositories</strong></summary>

### Profile and research

- [coding-jhj](https://github.com/coding-jhj): profile README and portfolio hub
- [foundation-model-lab](https://github.com/coding-jhj/foundation-model-lab): language-model research lab
- [Lease-Companion](https://github.com/coding-jhj/Lease-Companion): contract analysis assistant
- [MY_CAREER_PLANNER](https://github.com/coding-jhj/MY_CAREER_PLANNER): research engineering workflow
- [RepoPilot](https://github.com/coding-jhj/RepoPilot): repository analysis agent
- [AI_AGENT](https://github.com/coding-jhj/AI_AGENT): ReAct search agent
- [Personal-AI-Studio](https://github.com/coding-jhj/Personal-AI-Studio): source-grounded AI workspace

### Data, product, and engineering

- [VoiceGuide](https://github.com/coding-jhj/VoiceGuide): on-device accessibility AI
- [Stelive_data](https://github.com/coding-jhj/Stelive_data): automated data dashboard
- [MINECRART_DASHBOARD](https://github.com/coding-jhj/MINECRART_DASHBOARD): reliability-focused dashboard
- [ALPEH_FIFTH_HOMEWORK](https://github.com/coding-jhj/ALPEH_FIFTH_HOMEWORK): fixture-driven data product
- [claude-pwsh-kit](https://github.com/coding-jhj/claude-pwsh-kit): PowerShell AI development harness
- [aleph-first-homework](https://github.com/coding-jhj/aleph-first-homework): Passkey portfolio

### Learning, creative work, and coursework

- [SKT_ALEPH_STUDY_NOTE](https://github.com/coding-jhj/SKT_ALEPH_STUDY_NOTE): infrastructure and systems study notes
- [Review-Estcamp-AI-Human](https://github.com/coding-jhj/Review-Estcamp-AI-Human): interactive AI textbook
- [AI-Career-OS](https://github.com/coding-jhj/AI-Career-OS): early career operating system
- [ARKAN_FORGOTTEN_THRONE](https://github.com/coding-jhj/ARKAN_FORGOTTEN_THRONE): browser RPG
- [aleph-ninth-homework](https://github.com/coding-jhj/aleph-ninth-homework): web coursework
- [aleph-third-homework](https://github.com/coding-jhj/aleph-third-homework): web coursework
- [alpeh-second-mini-game](https://github.com/coding-jhj/alpeh-second-mini-game): browser game coursework
- [ALEPH_FIRST_HOMEWORK](https://github.com/coding-jhj/ALEPH_FIRST_HOMEWORK): web coursework

### Archived practice

- [Remote-Git-Practice](https://github.com/coding-jhj/Remote-Git-Practice): Git practice record
- [weekdays_vacation_python](https://github.com/coding-jhj/weekdays_vacation_python): Python learning record

</details>

## Contact

[GitHub](https://github.com/coding-jhj)
