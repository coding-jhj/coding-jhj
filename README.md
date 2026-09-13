<div align="center">

# Jeong Hwan Ju

### AI Engineer building toward Post-training Research

I build reliable AI systems through data curation, evaluation, grounded generation,
safety boundaries, and deployment-aware engineering.

`Post-training` `Evaluation` `RAG` `Guardrails` `On-device AI`

<p>
  <a href="https://github.com/coding-jhj">GitHub</a> |
  <a href="#selected-work">Selected Work</a> |
  <a href="#research-track">Research Track</a> |
  <a href="#all-public-repositories">All Repositories</a>
</p>

</div>

---

## What I Build

I focus on the boundary between model capability and product reliability:

- **Evaluation-driven AI:** fixed datasets, regression checks, explicit failure cases, and reproducible experiment records.
- **Grounded generation:** retrieval, source evidence, deterministic rules, and guardrails around model output.
- **Deployment-aware systems:** on-device inference, GPU-backed services, fallbacks, observability, and practical delivery.
- **Human-centered interfaces:** accessibility feedback, privacy-aware workflows, and products that can be opened and tested.

My preferred loop is:

```text
Problem
  -> Data and scope
  -> Baseline
  -> Controlled experiment
  -> Evaluation and failure analysis
  -> Deployable system
```

## Recognition

> **Minister of Employment and Labor Award (Encouragement Award)**
>
> **Project:** [Lease-Companion](https://github.com/coding-jhj/Lease-Companion)
>
> **Role:** Team Lead, AI/LLM

Lease-Companion is a contract review assistant for first-time tenants. It combines
document extraction, cross-document checks, an explicit Python rule engine, official-source
retrieval, and privacy-aware processing. The system is designed to provide evidence-backed
questions and actions rather than making unsafe legal or safety claims.

## Selected Work

### 01 | [Lease-Companion](https://github.com/coding-jhj/Lease-Companion)

**Awarded contract analysis assistant | Team Lead, AI/LLM**

- Structured contract, registry, and building documents before analysis.
- Used hosted LLMs for document structuring and explanation while keeping final judgments in a Python rule engine.
- Connected official legal and public sources through RAG without allowing retrieval to change rule results.
- Applied local PII tokenization before external model calls and local restoration after processing.
- Built evaluation and regression workflows around synthetic, de-identified goldsets.

**Offline evidence:** R01-R10 regression `100/100`; J01-J13 regression `51/51`.
These are fixed synthetic goldset results, not a claim about generalization to every real contract.

[Repository](https://github.com/coding-jhj/Lease-Companion) |
[AI Evaluation Plan](https://github.com/coding-jhj/Lease-Companion/blob/main/docs/ai/evaluation-plan.md)

### 02 | [VoiceGuide](https://github.com/coding-jhj/VoiceGuide)

**On-device walking assistant for blind and low-vision users**

- Ran YOLO/TFLite obstacle detection on Android camera frames without sending raw frames to the server.
- Used temporal voting, IoU tracking, and EMA smoothing to reduce unstable alerts.
- Delivered risk-aware haptic feedback, Korean TTS, and audio cues on the device.
- Connected FastAPI, GPS events, SSE, and a Cloud Run dashboard for system monitoring.

[Repository](https://github.com/coding-jhj/VoiceGuide)

### 03 | [Rainbow-Bridge](https://github.com/mosejong/Rainbow-Bridge/tree/jeonghwanju)

**AI and infrastructure contributor | Contribution branch: `jeonghwanju`**

- Integrated and operated a Qwen3 GPU TTS service with asynchronous execution.
- Implemented tone mapping and voice behavior for recovery-oriented conversations.
- Worked on STT/Gemini evaluation, recovery scoring, backend TTS and timeline flows.
- Supported PM2 operations and the demo video generation pipeline.

This project is linked to the contribution branch because the work is branch-specific.

## Research Track

### [foundation-model-lab](https://github.com/coding-jhj/foundation-model-lab)

**Reproducible decoder-only language model research lab**

The lab covers tokenizer and causal self-attention implementations, compact decoder-only
Transformers, training configuration, checkpoints, validation loss, generation, and
experiment records. It is a foundation for research engineering and pre-training work,
not a claim of completed post-training results.

### [MY_CAREER_PLANNER](https://github.com/coding-jhj/MY_CAREER_PLANNER)

**Research engineering workflow system**

A Plan -> Do -> See workspace for turning goals into tasks, execution logs, reviews,
and measurable next experiments. The project documents my preparation for
Post-training Research Engineer work.

### Local-model evaluation direction

Lease-Companion also contains an optional 7B 4-bit QLoRA comparison track. The current
repository contains preprocessing, configuration, and evaluation scaffolding; the local
model is outside the MVP critical path, and no trained weights or checkpoint are presented
as completed results.

## Independent Builds

### [RepoPilot](https://github.com/coding-jhj/RepoPilot)

Evidence-grounded repository analysis agent that produces file-and-line findings,
static-analysis results, and patch drafts. It is designed for free-first deployment.

[Live Demo](https://jeonghwanju-repopilot.hf.space/) |
[Code Guide](https://coding-jhj.github.io/RepoPilot/repopilot-code-guide.html)

### [Personal-AI-Studio](https://github.com/coding-jhj/Personal-AI-Studio)

Source-grounded personal AI workspace for documents, code, notebooks, spreadsheets,
and photo metadata. It exposes citations and keeps a local retrieval fallback when
external services are unavailable.

[Live Demo](https://jeonghwanju-personal-ai-studio.hf.space)

### [AI_AGENT](https://github.com/coding-jhj/AI_AGENT)

ReAct web-search agent using Gemini, LangChain, DuckDuckGo, FastAPI, and Hugging Face Spaces.

[Live Demo](https://jeonghwanju-ai-search-agent.hf.space)

### [Stelive_data](https://github.com/coding-jhj/Stelive_data)

Automated YouTube and CHZZK data pipeline with JSON/CSV outputs, scheduled GitHub Actions,
and a GitHub Pages dashboard.

[Live Dashboard](https://coding-jhj.github.io/Stelive_data/)

### [claude-pwsh-kit](https://github.com/coding-jhj/claude-pwsh-kit)

MIT-licensed Claude Code harness for Windows and PowerShell, including safety hooks,
skill routing, regression tests, and eight subagent templates.

### [ALPEH_FIFTH_HOMEWORK](https://github.com/coding-jhj/ALPEH_FIFTH_HOMEWORK) /
[MINECRART_DASHBOARD](https://github.com/coding-jhj/MINECRART_DASHBOARD)

Reliability-focused information dashboard with stale-data handling, replay fixtures,
and failure-aware data presentation.

### [aleph-first-homework](https://github.com/coding-jhj/aleph-first-homework)

Passkey-based private portfolio using WebAuthn, Supabase PostgreSQL, and a deployed web flow.

### [ARKAN_FORGOTTEN_THRONE](https://github.com/coding-jhj/ARKAN_FORGOTTEN_THRONE)

Playable single-file browser RPG with a world map, party management, dungeons, and turn-based combat.

[Play Now](https://coding-jhj.github.io/ARKAN_FORGOTTEN_THRONE/)

## Engineering Toolkit

`Python` `FastAPI` `Pydantic` `PostgreSQL` `Chroma` `BM25` `Gemini`
`RAG` `QLoRA` `Kotlin` `Android` `TFLite` `React` `TypeScript`
`Docker` `GitHub Actions` `Cloud Run` `Hugging Face Spaces`

## Live Demos

| Project | Demo | Platform |
|---|---|---|
| RepoPilot | [Open demo](https://jeonghwanju-repopilot.hf.space/) | Hugging Face Spaces |
| Personal AI Studio | [Open demo](https://jeonghwanju-personal-ai-studio.hf.space) | Hugging Face Spaces |
| AI Search Agent | [Open demo](https://jeonghwanju-ai-search-agent.hf.space) | Hugging Face Spaces |
| Stelive Data | [Open dashboard](https://coding-jhj.github.io/Stelive_data/) | GitHub Pages |
| AI Learning Textbook | [Open textbook](https://coding-jhj.github.io/Review-Estcamp-AI-Human/AI%20%ED%95%99%EC%8A%B5%20%EA%B5%90%EC%9E%AC%20_%20coding-jhj%20%EC%99%84%EC%A0%84%ED%8C%90.html) | GitHub Pages |
| Arkan RPG | [Play](https://coding-jhj.github.io/ARKAN_FORGOTTEN_THRONE/) | GitHub Pages |

## All Public Repositories

The sections above are the projects I want readers to understand first. The complete
public repository map is kept below so that coursework, experiments, and older work are
not hidden.

### Profile and research

- [coding-jhj](https://github.com/coding-jhj): this profile README and portfolio hub
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

## Evidence Policy

I separate shipped systems, measured offline results, and planned experiments.
Metrics in this profile are linked to repository documentation and are labeled when
they come from fixed synthetic or held-out test sets. A planned fine-tuning path is
not presented as a trained model, and a regression baseline is not presented as
real-world generalization.

## Start Here

1. Start with [Lease-Companion](https://github.com/coding-jhj/Lease-Companion) for evaluation-driven AI, RAG, and safety boundaries.
2. Open [VoiceGuide](https://github.com/coding-jhj/VoiceGuide) for on-device inference and accessibility engineering.
3. Open [Rainbow-Bridge](https://github.com/mosejong/Rainbow-Bridge/tree/jeonghwanju) for my team-project AI and infrastructure contribution.
4. Try [RepoPilot](https://jeonghwanju-repopilot.hf.space/) for a live evidence-grounded agent.

## Contact

[GitHub](https://github.com/coding-jhj)
