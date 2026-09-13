<div align="center">
  <img src="./assets/profile-cover.svg" alt="Jeong Hwan Ju — post-training research engineering portfolio" width="100%" />
</div>

<h1 align="center">JEONG HWAN JU</h1>

<p align="center">
  <strong>Post-training Research Engineer</strong><br />
  I build evaluation-driven AI systems with grounded generation,<br />
  explicit safety boundaries, and deployment-aware engineering.
</p>

<p align="center">
  <a href="#selected-work">Selected Work</a> ·
  <a href="#research-direction">Research Direction</a> ·
  <a href="#independent-work">Independent Work</a> ·
  <a href="https://github.com/coding-jhj">GitHub</a>
</p>

<hr />

<p align="center">
  <img src="./assets/selected-work-index.svg" alt="Selected work: Lease-Companion, VoiceGuide, and Rainbow Bridge" width="100%" />
</p>

<a id="selected-work"></a>
## Selected Work

<p>Three team projects first — each one shows a different way I turn AI systems into useful, testable products.</p>

<p>
  <img src="./assets/selected-work-neon.png" alt="Neon project cards in order: Lease-Companion, VoiceGuide, and Rainbow Bridge" width="100%" />
</p>

<p align="center">
  <a href="https://github.com/coding-jhj/Lease-Companion">Lease-Companion</a> ·
  <a href="https://github.com/coding-jhj/VoiceGuide">VoiceGuide</a> ·
  <a href="https://github.com/mosejong/Rainbow-Bridge/tree/jeonghwanju">Rainbow Bridge contribution branch</a>
</p>

<p align="center">
  <strong>Offline evidence:</strong>
  <code>Contract checks · 100/100</code> ·
  <code>Judgment cases · 47/47</code><br />
  <sub>Fixed offline test data; not real-world contract coverage.</sub>
</p>

<details>
  <summary><strong>Lease-Companion · Team Lead, AI/LLM</strong></summary>

  <p><strong>Awarded contract analysis assistant | Team Lead, AI/LLM</strong></p>

  <p>A contract review assistant for first-time tenants. It combines document extraction,
  cross-document validation, official-source retrieval, and a Python rule engine to provide
  evidence-backed questions and actions instead of unsafe legal or safety claims.</p>

  <p><code>Document AI</code> <code>Rule Engine</code> <code>RAG</code> <code>Privacy</code> <code>Evaluation</code></p>

  <p>
    <a href="https://github.com/coding-jhj/Lease-Companion">Repository</a> ·
    <a href="https://github.com/coding-jhj/Lease-Companion/blob/main/docs/ai/evaluation-plan.md">Evaluation Plan</a>
  </p>
</details>

<details>
  <summary><strong>VoiceGuide · On-device AI and accessibility</strong></summary>

  <p><strong>Walking assistant for blind and low-vision users</strong></p>

  <p>An Android system that runs YOLO/TFLite obstacle detection on device camera frames,
  then delivers stable risk-aware haptic feedback, Korean TTS, and audio cues. The system
  connects FastAPI, GPS events, SSE, and a Cloud Run dashboard without sending raw frames
  to the server.</p>

  <p><code>Android</code> <code>Kotlin</code> <code>TFLite</code> <code>YOLO</code> <code>FastAPI</code> <code>Accessibility</code></p>

  <p><a href="https://github.com/coding-jhj/VoiceGuide">Repository</a></p>
</details>

<details>
  <summary><strong>Rainbow Bridge · AI infrastructure contributor</strong></summary>

  <p><strong>Contribution branch: <code>jeonghwanju</code></strong></p>

  <p>Contributed to Qwen3 GPU TTS with asynchronous execution, tone mapping,
  STT/Gemini evaluation, recovery scoring, backend TTS and timeline flows,
  PM2 operations, and the demo video generation pipeline.</p>

  <p><code>Qwen3 TTS</code> <code>GPU Service</code> <code>Evaluation</code> <code>PM2</code> <code>Backend</code></p>

  <p><a href="https://github.com/mosejong/Rainbow-Bridge/tree/jeonghwanju">Contribution Branch</a></p>
</details>

<a id="research-direction"></a>
## Research Direction

<p>
  <img src="./assets/research-direction-neon.png" alt="Neon research direction panel for post-training research engineering, model feedback, reward modeling, evaluation, toolkit, and GitHub contact" width="100%" />
</p>

<p align="center">
  <strong>Post-training Research Engineer</strong><br />
  Building the research engineering foundation needed to make model behavior measurable,
  reproducible, and useful in real products.
</p>

<details>
  <summary><strong>foundation-model-lab · Reproducible model experiments</strong></summary>

  <p>Reproducible decoder-only language model experiments covering tokenizers,
  causal self-attention, compact Transformers, checkpoints, validation loss,
  generation, and experiment records.</p>

  <p><strong>This is a foundation for research engineering and pre-training work, not a claim of completed post-training results.</strong></p>

  <p><a href="https://github.com/coding-jhj/foundation-model-lab">Open foundation-model-lab</a></p>
</details>

<details>
  <summary><strong>MY_CAREER_PLANNER · Execution workspace</strong></summary>

  <p>A Plan → Do → See workspace for research goals, execution logs, reviews,
  and measurable next experiments. It documents my preparation for
  <strong>Post-training Research Engineer</strong> work.</p>

  <p><a href="https://github.com/coding-jhj/MY_CAREER_PLANNER">Open MY_CAREER_PLANNER</a></p>
</details>

<details>
  <summary><strong>Local-model direction · Current experiment track</strong></summary>

  <p>Lease-Companion contains an optional 7B 4-bit QLoRA comparison track. The current
  repository contains preprocessing, configuration, and evaluation scaffolding;
  <strong>no trained weights or checkpoint are presented as completed results.</strong></p>
</details>

<a id="independent-work"></a>
## Independent Work

<details>
  <summary><strong>Explore 8 supporting projects</strong></summary>

- **[RepoPilot](https://github.com/coding-jhj/RepoPilot)**: evidence-grounded repository analysis agent producing file-and-line findings, static-analysis results, and patch drafts. [Demo](https://jeonghwanju-repopilot.hf.space/) | [Code Guide](https://coding-jhj.github.io/RepoPilot/repopilot-code-guide.html)
- **[Personal-AI-Studio](https://github.com/coding-jhj/Personal-AI-Studio)**: source-grounded personal AI workspace with citation cards and local retrieval fallback. [Demo](https://jeonghwanju-personal-ai-studio.hf.space)
- **[AI_AGENT](https://github.com/coding-jhj/AI_AGENT)**: ReAct web-search agent using Gemini, LangChain, DuckDuckGo, FastAPI, and Hugging Face Spaces. [Demo](https://jeonghwanju-ai-search-agent.hf.space)
- **[Stelive_data](https://github.com/coding-jhj/Stelive_data)**: automated YouTube and CHZZK data pipeline with scheduled collection and a GitHub Pages dashboard. [Dashboard](https://coding-jhj.github.io/Stelive_data/)
- **[claude-pwsh-kit](https://github.com/coding-jhj/claude-pwsh-kit)**: MIT-licensed Claude Code harness for Windows and PowerShell with safety hooks, skill routing, regression tests, and subagent templates.
- **[aleph-first-homework](https://github.com/coding-jhj/aleph-first-homework)**: Passkey-based private portfolio using WebAuthn and Supabase PostgreSQL.
- **[ALPEH_FIFTH_HOMEWORK](https://github.com/coding-jhj/ALPEH_FIFTH_HOMEWORK) / [MINECRART_DASHBOARD](https://github.com/coding-jhj/MINECRART_DASHBOARD)**: reliability-focused information dashboard with stale-data handling and replay fixtures.
- **[ARKAN_FORGOTTEN_THRONE](https://github.com/coding-jhj/ARKAN_FORGOTTEN_THRONE)**: playable single-file browser RPG. [Play](https://coding-jhj.github.io/ARKAN_FORGOTTEN_THRONE/)

</details>

## Toolkit

<p>
  <code>Python</code> <code>FastAPI</code> <code>Pydantic</code> <code>PostgreSQL</code> <code>Chroma</code> <code>BM25</code> <code>Gemini</code> <code>RAG</code> <code>QLoRA</code><br />
  <code>Kotlin</code> <code>Android</code> <code>TFLite</code> <code>React</code> <code>TypeScript</code> <code>Docker</code> <code>GitHub Actions</code>
</p>

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

<hr />

<p align="center">
  <strong>Building toward more reliable AI</strong><br />
  <a href="https://github.com/coding-jhj">GitHub →</a>
</p>
