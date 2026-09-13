<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/profile-cover.svg?v=3" />
  <img src="./assets/profile-cover-light.svg?v=3" alt="Jeong Hwan Ju — Post-training Research Engineer" width="100%" />
</picture>

<p align="center">
  <em>Building evaluation-driven AI systems with grounded generation, explicit safety boundaries, and deployment-aware engineering.</em>
</p>

<p align="center">
  <strong>03</strong> Team Projects &nbsp;·&nbsp; <strong>01</strong> Award-winning Lead &nbsp;·&nbsp; <strong>08</strong> Independent Works
</p>

<p align="center">
  <a href="#selected-work">Selected Work</a> ·
  <a href="#research-direction">Research Direction</a> ·
  <a href="#independent-work">Independent Work</a> ·
  <a href="#toolkit">Toolkit</a>
</p>

<a id="selected-work"></a>
## Selected Work

Three team projects first — each one shows a different way I turn AI systems into useful, testable products.

<table>
  <tr>
    <td width="170" align="center">
      <img src="./assets/lease-companion-thumb.png" alt="Neon contract document and magnifying glass illustration" width="150" />
    </td>
    <td>
      <sub>RECOGNITION · 🏆 MINISTER OF EMPLOYMENT AND LABOR AWARD</sub>
      <h3><a href="https://github.com/coding-jhj/Lease-Companion">Lease-Companion</a></h3>
      <strong>Awarded contract analysis assistant | Team Lead, AI/LLM</strong>
      <p>A contract review assistant for first-time tenants. It combines document extraction,
      cross-document validation, official-source retrieval, and a Python rule engine to provide
      evidence-backed questions and actions instead of unsafe legal or safety claims.</p>
      <p><code>Document AI</code> <code>Rule Engine</code> <code>RAG</code> <code>Privacy</code> <code>Evaluation</code></p>
      <p>
        <strong>Offline evidence:</strong>
        <code>Contract checks · 100/100</code> ·
        <code>Judgment cases · 47/47</code><br />
        <sub>Fixed offline test data; not real-world contract coverage.</sub>
      </p>
      <p>
        <a href="https://github.com/coding-jhj/Lease-Companion">Repository</a> ·
        <a href="https://github.com/coding-jhj/Lease-Companion/blob/main/docs/ai/evaluation-plan.md">Evaluation Plan</a>
      </p>
    </td>
  </tr>
  <tr>
    <td width="170" align="center">
      <img src="./assets/voiceguide-thumb.png" alt="Neon smartphone, microphone, and navigation path illustration" width="150" />
    </td>
    <td>
      <sub>ON-DEVICE AI · ACCESSIBILITY</sub>
      <h3><a href="https://github.com/coding-jhj/VoiceGuide">VoiceGuide</a></h3>
      <strong>Walking assistant for blind and low-vision users</strong>
      <p>An Android system that runs YOLO/TFLite obstacle detection on device camera frames,
      then delivers stable risk-aware haptic feedback, Korean TTS, and audio cues. The system
      connects FastAPI, GPS events, SSE, and a Cloud Run dashboard without sending raw frames
      to the server.</p>
      <p><code>Android</code> <code>Kotlin</code> <code>TFLite</code> <code>YOLO</code> <code>FastAPI</code> <code>Accessibility</code></p>
      <p><a href="https://github.com/coding-jhj/VoiceGuide">Repository</a></p>
    </td>
  </tr>
  <tr>
    <td width="170" align="center">
      <img src="./assets/rainbow-bridge-thumb.png" alt="Neon GPU, server, and audio waveform infrastructure illustration" width="150" />
    </td>
    <td>
      <sub>AI INFRASTRUCTURE · CONTRIBUTION</sub>
      <h3><a href="https://github.com/mosejong/Rainbow-Bridge/tree/jeonghwanju">Rainbow Bridge</a></h3>
      <strong>AI and infrastructure contributor | Contribution branch: <code>jeonghwanju</code></strong>
      <p>Contributed to Qwen3 GPU TTS with asynchronous execution, tone mapping,
      STT/Gemini evaluation, recovery scoring, backend TTS and timeline flows,
      PM2 operations, and the demo video generation pipeline.</p>
      <p><code>Qwen3 TTS</code> <code>GPU Service</code> <code>Evaluation</code> <code>PM2</code> <code>Backend</code></p>
      <p><a href="https://github.com/mosejong/Rainbow-Bridge/tree/jeonghwanju">Contribution Branch</a></p>
    </td>
  </tr>
</table>

<a id="research-direction"></a>
## Research Direction

<sub>Post-training Research Engineer · research engineering preparation</sub>

### 🧪 Foundation model lab — [foundation-model-lab](https://github.com/coding-jhj/foundation-model-lab)
Reproducible decoder-only language model experiments covering tokenizers, causal self-attention, compact Transformers, checkpoints, validation loss, generation, and experiment records.

> [!NOTE]
> This is a foundation for research engineering and pre-training work, not a claim of completed post-training results.

### 🗂️ Execution workspace — [MY_CAREER_PLANNER](https://github.com/coding-jhj/MY_CAREER_PLANNER)
A Plan → Do → See workspace for research goals, execution logs, reviews, and measurable next experiments. It documents my preparation for **Post-training Research Engineer** work.

### 🔬 Local-model direction — Lease-Companion comparison track
An optional 7B 4-bit QLoRA comparison track. The current repository contains preprocessing, configuration, and evaluation scaffolding.

> [!NOTE]
> No trained weights or checkpoint are presented as completed results.

<a id="independent-work"></a>
## Independent Work

Independent work is not a list of ideas. It is a record of implementing analysis, search, security, operations, and failure handling.

<table>
  <tr>
    <td valign="top" width="50%">
      <sub>CODE ANALYSIS · AGENT</sub>
      <h3><a href="https://github.com/coding-jhj/RepoPilot">RepoPilot</a></h3>
      <p><strong>Evidence-grounded repository analysis agent</strong><br />
      Accepts a public GitHub URL, indexes the files, and analyzes Python, JavaScript, and TypeScript structure with static rules. Results retain file-and-line evidence, patch drafts, scope validation, and an optional PR flow.</p>
      <p><code>FastAPI</code> <code>Next.js</code> <code>Static Analysis</code> <code>Evidence</code></p>
      <p><a href="https://jeonghwanju-repopilot.hf.space/">Demo</a> · <a href="https://coding-jhj.github.io/RepoPilot/repopilot-code-guide.html">Code Guide</a></p>
    </td>
    <td valign="top" width="50%">
      <sub>PERSONAL KNOWLEDGE · RAG</sub>
      <h3><a href="https://github.com/coding-jhj/Personal-AI-Studio">Personal-AI-Studio</a></h3>
      <p><strong>Source-grounded personal AI workspace</strong><br />
      Unifies documents, code, notebooks, spreadsheets, photo metadata, and MongoDB into one knowledge base. It shows local retrieval results as source cards and connects voice input with a local fallback when an external LLM fails.</p>
      <p><code>Streamlit</code> <code>TF-IDF</code> <code>Voice</code> <code>Fallback</code></p>
      <p><a href="https://jeonghwanju-personal-ai-studio.hf.space">Demo</a></p>
    </td>
  </tr>
  <tr>
    <td valign="top" width="50%">
      <sub>WEB SEARCH · REACT LOOP</sub>
      <h3><a href="https://github.com/coding-jhj/AI_AGENT">AI_AGENT</a></h3>
      <p><strong>Agent that decides when search is needed</strong><br />
      Analyzes a question, decides whether to search, observes DuckDuckGo results, and continues with another search or an answer through a ReAct loop. It provides a FastAPI API and browser UI without storing the user-provided key on the server.</p>
      <p><code>Gemini</code> <code>LangChain</code> <code>DuckDuckGo</code> <code>FastAPI</code></p>
      <p><a href="https://jeonghwanju-ai-search-agent.hf.space">Demo</a></p>
    </td>
    <td valign="top" width="50%">
      <sub>DATA PIPELINE · OPERATIONS</sub>
      <h3><a href="https://github.com/coding-jhj/Stelive_data">Stelive_data</a></h3>
      <p><strong>Data product from collection to deployment</strong><br />
      Regularly collects YouTube Data API and CHZZK data, builds JSON and CSV history, regenerates the dashboard, and deploys it to GitHub Pages. The repository captures a repeatable operational flow across different external sources.</p>
      <p><code>Python</code> <code>GitHub Actions</code> <code>JSON/CSV</code> <code>GitHub Pages</code></p>
      <p><a href="https://coding-jhj.github.io/Stelive_data/">Dashboard</a></p>
    </td>
  </tr>
  <tr>
    <td valign="top" width="50%">
      <sub>DEVELOPER TOOLING · SAFETY</sub>
      <h3><a href="https://github.com/coding-jhj/claude-pwsh-kit">claude-pwsh-kit</a></h3>
      <p><strong>Claude Code harness for Windows and PowerShell</strong><br />
      Combines dangerous-command blocking, keyword-based skill routing, research verification guidance, and eight subagent templates. It documents non-ASCII encoding and PowerShell pipe issues and checks them with regression tests.</p>
      <p><code>PowerShell</code> <code>Safety Hooks</code> <code>Skill Router</code> <code>MIT</code></p>
    </td>
    <td valign="top" width="50%">
      <sub>SECURITY · PASSWORDLESS AUTH</sub>
      <h3><a href="https://github.com/coding-jhj/aleph-first-homework">Passkey Private Portfolio</a></h3>
      <p><strong>One service connecting a public portfolio and private workspace</strong><br />
      Uses WebAuthn passkeys and separates account-scoped private data through a Vercel API and Supabase PostgreSQL. The security boundary covers challenge replay prevention, session protection, account-scope checks, and RLS.</p>
      <p><code>WebAuthn</code> <code>Vercel</code> <code>Supabase</code> <code>RLS</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top" width="50%">
      <sub>RELIABILITY · DATA PRODUCT</sub>
      <h3><a href="https://github.com/coding-jhj/ALPEH_FIFTH_HOMEWORK">Real Information Board</a></h3>
      <p><strong>A dashboard that explains failures honestly</strong><br />
      <a href="https://github.com/coding-jhj/ALPEH_FIFTH_HOMEWORK">ALPEH_FIFTH_HOMEWORK</a> and <a href="https://github.com/coding-jhj/MINECRART_DASHBOARD">MINECRART_DASHBOARD</a> distinguish timeout, authentication rejection, rate limits, offline status, and schema changes while preserving the last known good value. Live requests and replay fixtures share the same core path, with nine fixtures covering failure and recovery.</p>
      <p><code>Next.js</code> <code>TypeScript</code> <code>Supabase</code> <code>Replay</code></p>
      <p><a href="https://t04-real-information-board.vercel.app">Demo</a></p>
    </td>
    <td valign="top" width="50%">
      <sub>CREATIVE ENGINEERING · BROWSER GAME</sub>
      <h3><a href="https://github.com/coding-jhj/ARKAN_FORGOTTEN_THRONE">ARKAN_FORGOTTEN_THRONE</a></h3>
      <p><strong>A turn-based RPG playable directly in the browser</strong><br />
      Connects the world map, town, guild, shop, NPC, dungeon, battle, compendium, and equipment-upgrade flows through static hosting. It includes a Canvas pixel background, modular code, responsive mobile layout, and headless QA for battles, saves, and progression gates.</p>
      <p><code>HTML/CSS/JS</code> <code>Canvas</code> <code>Responsive</code> <code>Playwright</code></p>
      <p><a href="https://coding-jhj.github.io/ARKAN_FORGOTTEN_THRONE/">Play</a></p>
    </td>
  </tr>
</table>

<a id="toolkit"></a>
## Toolkit

| Area | Tools |
| --- | --- |
| **LLM / Retrieval** | <code>Gemini</code> <code>RAG</code> <code>QLoRA</code> <code>Chroma</code> <code>BM25</code> |
| **Backend / Data** | <code>Python</code> <code>FastAPI</code> <code>Pydantic</code> <code>PostgreSQL</code> |
| **Mobile / Frontend** | <code>Kotlin</code> <code>Android</code> <code>TFLite</code> <code>React</code> <code>TypeScript</code> |
| **Infra** | <code>Docker</code> <code>GitHub Actions</code> |

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

<a href="https://github.com/coding-jhj">GitHub</a>
