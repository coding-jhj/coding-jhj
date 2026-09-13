<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,45:1D4ED8,100:0F766E&height=240&section=header&text=JEONG%20HWAN%20JU&fontSize=52&fontColor=FFFFFF&fontAlignY=38&desc=POST-TRAINING%20RESEARCH%20%7C%20EVALUATION%20%7C%20GROUNDED%20AI&descAlignY=61&descSize=17&descColor=CBD5E1" alt="Jeong Hwan Ju - Post-training Research and Evaluation" />

<p>
  <a href="https://github.com/coding-jhj"><img src="https://img.shields.io/badge/FOCUS-POST--TRAINING-0F766E?style=for-the-badge&labelColor=0F172A" alt="Focus: Post-training" /></a>
  <a href="#recognition"><img src="https://img.shields.io/badge/RECOGNITION-MINISTER%27S%20AWARD-CB9A2C?style=for-the-badge&labelColor=0F172A" alt="Minister's Award" /></a>
  <a href="#selected-work"><img src="https://img.shields.io/badge/WORK-SHIPPED%20SYSTEMS-2563EB?style=for-the-badge&labelColor=0F172A" alt="Shipped systems" /></a>
</p>

<p>
  <a href="#selected-work">Selected Work</a> |
  <a href="#research-track">Research Track</a> |
  <a href="#independent-builds">Independent Builds</a> |
  <a href="#all-public-repositories">All Repositories</a>
</p>

</div>

<p align="center">
  <strong>Building systems where model capability meets measurable reliability.</strong><br />
  Data curation, controlled generation, evaluation, safety boundaries, and deployment-aware engineering.
</p>

<table align="center">
  <tr>
    <td width="25%" align="center"><strong>01</strong><br /><sub>EVALUATION</sub><br /><small>Baselines<br />Regression<br />Failure analysis</small></td>
    <td width="25%" align="center"><strong>02</strong><br /><sub>GROUNDING</sub><br /><small>RAG<br />Evidence<br />Rules</small></td>
    <td width="25%" align="center"><strong>03</strong><br /><sub>DEPLOYMENT</sub><br /><small>On-device<br />GPU services<br />Fallbacks</small></td>
    <td width="25%" align="center"><strong>04</strong><br /><sub>HUMAN USE</sub><br /><small>Privacy<br />Accessibility<br />Clear actions</small></td>
  </tr>
</table>

---

## Recognition

<table>
  <tr>
    <td width="19%" align="center" valign="middle">
      <img src="https://img.shields.io/badge/ENCOURAGEMENT-AWARD-CB9A2C?style=for-the-badge&labelColor=0F172A" alt="Encouragement Award" />
    </td>
    <td valign="middle">
      <h3>Minister of Employment and Labor Award</h3>
      <strong>Encouragement Award</strong><br />
      <strong>Project:</strong> <a href="https://github.com/coding-jhj/Lease-Companion">Lease-Companion</a><br />
      <strong>Role:</strong> Team Lead, AI/LLM
    </td>
  </tr>
</table>

<p>
  Lease-Companion is a contract review assistant for first-time tenants. It combines
  document extraction, cross-document checks, an explicit Python rule engine, official-source
  retrieval, and privacy-aware processing. It provides evidence-backed questions and actions
  instead of making unsafe legal or safety claims.
</p>

## Selected Work

<table>
  <tr>
    <td valign="top">
      <img src="https://img.shields.io/badge/01-AWARDED%20AI%20SYSTEM-CB9A2C?style=flat-square&labelColor=0F172A" alt="Awarded AI system" />
      <h3><a href="https://github.com/coding-jhj/Lease-Companion">Lease-Companion</a></h3>
      <strong>Contract analysis assistant | Team Lead, AI/LLM</strong>
      <ul>
        <li>Structured contract, registry, and building documents before analysis.</li>
        <li>Kept final judgments in a Python rule engine while using hosted LLMs for structuring and explanation.</li>
        <li>Connected official legal and public sources through RAG without allowing retrieval to change rule results.</li>
        <li>Applied local PII tokenization before external model calls and local restoration after processing.</li>
      </ul>
      <p><strong>Offline evidence:</strong> R01-R10 <code>100/100</code> | J01-J13 <code>51/51</code><br /><small>Fixed synthetic goldset regression results, not a claim about every real contract.</small></p>
      <a href="https://github.com/coding-jhj/Lease-Companion"><img src="https://img.shields.io/badge/Repository-181717?style=flat-square&logo=github&logoColor=white" alt="Lease-Companion repository" /></a>
      <a href="https://github.com/coding-jhj/Lease-Companion/blob/main/docs/ai/evaluation-plan.md"><img src="https://img.shields.io/badge/Evaluation%20Plan-2563EB?style=flat-square" alt="Lease-Companion evaluation plan" /></a>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="https://img.shields.io/badge/02-ON--DEVICE%20AI-2563EB?style=flat-square&labelColor=0F172A" alt="On-device AI" />
      <h3><a href="https://github.com/coding-jhj/VoiceGuide">VoiceGuide</a></h3>
      <strong>Walking assistant for blind and low-vision users</strong>
      <ul>
        <li>YOLO/TFLite obstacle detection on Android camera frames.</li>
        <li>Temporal voting, IoU tracking, and EMA smoothing for stable alerts.</li>
        <li>Risk-aware haptic feedback, Korean TTS, and audio cues on-device.</li>
        <li>FastAPI, GPS events, SSE, and Cloud Run dashboard integration.</li>
      </ul>
      <a href="https://github.com/coding-jhj/VoiceGuide"><img src="https://img.shields.io/badge/Repository-181717?style=flat-square&logo=github&logoColor=white" alt="VoiceGuide repository" /></a>
    </td>
    <td width="50%" valign="top">
      <img src="https://img.shields.io/badge/03-AI%20INFRASTRUCTURE-0F766E?style=flat-square&labelColor=0F172A" alt="AI infrastructure" />
      <h3><a href="https://github.com/mosejong/Rainbow-Bridge/tree/jeonghwanju">Rainbow-Bridge</a></h3>
      <strong>AI and infrastructure contributor</strong><br />
      <small>Contribution branch: <code>jeonghwanju</code></small>
      <ul>
        <li>Qwen3 GPU TTS service with asynchronous execution.</li>
        <li>Tone mapping and voice behavior for recovery conversations.</li>
        <li>STT/Gemini evaluation, recovery scoring, TTS, and timeline flows.</li>
        <li>PM2 operations and demo video generation pipeline.</li>
      </ul>
      <a href="https://github.com/mosejong/Rainbow-Bridge/tree/jeonghwanju"><img src="https://img.shields.io/badge/Contribution%20Branch-0F766E?style=flat-square" alt="Rainbow-Bridge contribution branch" /></a>
    </td>
  </tr>
</table>

## Research Track

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="https://img.shields.io/badge/RESEARCH-PRE--TRAINING%20FOUNDATIONS-6366F1?style=flat-square&labelColor=0F172A" alt="Pre-training foundations" />
      <h3><a href="https://github.com/coding-jhj/foundation-model-lab">foundation-model-lab</a></h3>
      <p>Reproducible decoder-only language model research lab covering tokenizers, causal self-attention, compact Transformers, training configuration, checkpoints, validation loss, generation, and experiment records.</p>
      <small>Foundation for research engineering and pre-training work, not a claim of completed post-training results.</small>
    </td>
    <td width="50%" valign="top">
      <img src="https://img.shields.io/badge/WORKFLOW-PLAN%20%7C%20DO%20%7C%20SEE-6366F1?style=flat-square&labelColor=0F172A" alt="Research workflow" />
      <h3><a href="https://github.com/coding-jhj/MY_CAREER_PLANNER">MY_CAREER_PLANNER</a></h3>
      <p>A research engineering workspace for turning goals into tasks, execution logs, reviews, and measurable next experiments.</p>
      <small>Documents my preparation for Post-training Research Engineer work.</small>
    </td>
  </tr>
</table>

<blockquote>
  <strong>Local-model evaluation direction:</strong> Lease-Companion contains an optional
  7B 4-bit QLoRA comparison track. The repository currently contains preprocessing,
  configuration, and evaluation scaffolding. No trained weights or checkpoint are presented
  as completed results.
</blockquote>

## Independent Builds

<table>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/coding-jhj/RepoPilot">RepoPilot</a></h3>
      <p>Evidence-grounded repository analysis agent producing file-and-line findings, static-analysis results, and patch drafts.</p>
      <a href="https://jeonghwanju-repopilot.hf.space/"><img src="https://img.shields.io/badge/Open%20Space-FFD21E?style=flat-square" alt="RepoPilot Space" /></a>
      <a href="https://coding-jhj.github.io/RepoPilot/repopilot-code-guide.html"><img src="https://img.shields.io/badge/Code%20Guide-6366F1?style=flat-square" alt="RepoPilot code guide" /></a>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/coding-jhj/Personal-AI-Studio">Personal-AI-Studio</a></h3>
      <p>Source-grounded personal AI workspace for documents, code, notebooks, spreadsheets, and photo metadata with citation cards and local retrieval fallback.</p>
      <a href="https://jeonghwanju-personal-ai-studio.hf.space"><img src="https://img.shields.io/badge/Live%20Demo-FFD21E?style=flat-square" alt="Personal AI Studio demo" /></a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/coding-jhj/AI_AGENT">AI_AGENT</a></h3>
      <p>ReAct web-search agent using Gemini, LangChain, DuckDuckGo, FastAPI, and Hugging Face Spaces.</p>
      <a href="https://jeonghwanju-ai-search-agent.hf.space"><img src="https://img.shields.io/badge/Live%20Demo-FFD21E?style=flat-square" alt="AI Search Agent demo" /></a>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/coding-jhj/Stelive_data">Stelive_data</a></h3>
      <p>Automated YouTube and CHZZK data pipeline with JSON/CSV outputs, scheduled GitHub Actions, and a GitHub Pages dashboard.</p>
      <a href="https://coding-jhj.github.io/Stelive_data/"><img src="https://img.shields.io/badge/Open%20Dashboard-222222?style=flat-square&logo=githubpages&logoColor=white" alt="Stelive Data dashboard" /></a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/coding-jhj/claude-pwsh-kit">claude-pwsh-kit</a></h3>
      <p>MIT-licensed Claude Code harness for Windows and PowerShell with safety hooks, skill routing, regression tests, and eight subagent templates.</p>
      <img src="https://img.shields.io/badge/MIT-22C55E?style=flat-square" alt="MIT licensed" />
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/coding-jhj/ALPEH_FIFTH_HOMEWORK">ALPEH_FIFTH_HOMEWORK</a> / <a href="https://github.com/coding-jhj/MINECRART_DASHBOARD">MINECRART_DASHBOARD</a></h3>
      <p>Reliability-focused information dashboard with stale-data handling, replay fixtures, and failure-aware data presentation.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/coding-jhj/aleph-first-homework">aleph-first-homework</a></h3>
      <p>Passkey-based private portfolio using WebAuthn, Supabase PostgreSQL, and a deployed web flow.</p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/coding-jhj/ARKAN_FORGOTTEN_THRONE">ARKAN_FORGOTTEN_THRONE</a></h3>
      <p>Playable single-file browser RPG with a world map, party management, dungeons, and turn-based combat.</p>
      <a href="https://coding-jhj.github.io/ARKAN_FORGOTTEN_THRONE/"><img src="https://img.shields.io/badge/Play%20Now-FF6B6B?style=flat-square" alt="Play Arkan RPG" /></a>
    </td>
  </tr>
</table>

## Engineering Toolkit

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white" alt="Pydantic" />
  <img src="https://img.shields.io/badge/Gemini-4285F4?style=flat-square&logo=google&logoColor=white" alt="Gemini" />
  <img src="https://img.shields.io/badge/RAG-0F766E?style=flat-square" alt="RAG" />
  <img src="https://img.shields.io/badge/QLoRA-6366F1?style=flat-square" alt="QLoRA" />
  <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin" />
  <img src="https://img.shields.io/badge/Android-3DDC84?style=flat-square&logo=android&logoColor=white" alt="Android" />
  <img src="https://img.shields.io/badge/TFLite-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" alt="TensorFlow Lite" />
  <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=111111" alt="React" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" />
</p>

## Open Builds

<p align="center">
  <a href="https://jeonghwanju-repopilot.hf.space/"><img src="https://img.shields.io/badge/RepoPilot-Open%20Space-FFD21E?style=for-the-badge" alt="Open RepoPilot" /></a>
  <a href="https://jeonghwanju-personal-ai-studio.hf.space"><img src="https://img.shields.io/badge/Personal%20AI%20Studio-Open%20Demo-FFD21E?style=for-the-badge" alt="Open Personal AI Studio" /></a>
  <a href="https://jeonghwanju-ai-search-agent.hf.space"><img src="https://img.shields.io/badge/AI%20Search%20Agent-Open%20Demo-FFD21E?style=for-the-badge" alt="Open AI Search Agent" /></a>
  <a href="https://coding-jhj.github.io/Stelive_data/"><img src="https://img.shields.io/badge/Stelive%20Data-Open%20Dashboard-222222?style=for-the-badge&logo=githubpages&logoColor=white" alt="Open Stelive Data" /></a>
  <a href="https://coding-jhj.github.io/ARKAN_FORGOTTEN_THRONE/"><img src="https://img.shields.io/badge/Arkan-Play%20Now-FF6B6B?style=for-the-badge" alt="Play Arkan" /></a>
</p>

## All Public Repositories

<details>
  <summary><strong>Explore all 23 public repositories</strong></summary>

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

</details>

## Evidence Policy

I separate shipped systems, measured offline results, and planned experiments.
Metrics in this profile are linked to repository documentation and are labeled when
they come from fixed synthetic or held-out test sets. A planned fine-tuning path is
not presented as a trained model, and a regression baseline is not presented as
real-world generalization.

## Start Here

<p>
  <a href="https://github.com/coding-jhj/Lease-Companion"><img src="https://img.shields.io/badge/01-Lease--Companion-CB9A2C?style=flat-square&labelColor=0F172A" alt="Start with Lease-Companion" /></a>
  <a href="https://github.com/coding-jhj/VoiceGuide"><img src="https://img.shields.io/badge/02-VoiceGuide-2563EB?style=flat-square&labelColor=0F172A" alt="Open VoiceGuide" /></a>
  <a href="https://github.com/mosejong/Rainbow-Bridge/tree/jeonghwanju"><img src="https://img.shields.io/badge/03-Rainbow--Bridge-0F766E?style=flat-square&labelColor=0F172A" alt="Open Rainbow-Bridge contribution branch" /></a>
  <a href="https://github.com/coding-jhj/RepoPilot"><img src="https://img.shields.io/badge/04-RepoPilot-6366F1?style=flat-square&labelColor=0F172A" alt="Open RepoPilot" /></a>
</p>

## Contact

<p>
  <a href="https://github.com/coding-jhj"><img src="https://img.shields.io/badge/GitHub-coding--jhj-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub profile" /></a>
</p>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F766E,50:1D4ED8,100:0F172A&height=120&section=footer" alt="footer" />
</div>
