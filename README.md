<div align="center">
  <img src="./assets/profile-cover.svg" alt="Jeong Hwan Ju — post-training research engineering portfolio" width="100%" />
</div>

<table width="100%" cellpadding="22" cellspacing="0">
  <tr>
    <td align="center" bgcolor="#090D18">
      <h1><font color="#F8FAFC">JEONG HWAN JU</font></h1>
      <h2><font color="#C084FC">POST-TRAINING RESEARCH ENGINEER</font></h2>
      <p><font color="#CBD5E1">I build evaluation-driven AI systems with grounded generation,<br />
      explicit safety boundaries, and deployment-aware engineering.</font></p>
      <p>
        <font color="#A78BFA">EVALUATION</font>
        <font color="#64748B"> · </font>
        <font color="#FB7185">GROUNDING</font>
        <font color="#64748B"> · </font>
        <font color="#22D3EE">DEPLOYMENT</font>
      </p>
    </td>
  </tr>
</table>

<p align="center">
  <a href="#selected-work"><font color="#8B5CF6">Selected Work</font></a> ·
  <a href="#research-direction"><font color="#F43F5E">Research Direction</font></a> ·
  <a href="#independent-work"><font color="#0891B2">Independent Work</font></a> ·
  <a href="https://github.com/coding-jhj"><font color="#475569">GitHub</font></a>
</p>

<table width="100%" cellpadding="18" cellspacing="0">
  <tr>
    <td valign="top" width="33%" bgcolor="#17112A">
      <font color="#C084FC"><sub>DIRECTION</sub></font><br />
      <strong><font color="#F8FAFC">Post-training Research Engineer</font></strong><br />
      <font color="#A5B4FC"><sub>Research engineering preparation</sub></font>
    </td>
    <td valign="top" width="34%" bgcolor="#24121C">
      <font color="#FB7185"><sub>RECOGNITION</sub></font><br />
      <strong><font color="#F8FAFC">Minister of Employment and Labor Award</font></strong><br />
      <a href="https://github.com/coding-jhj/Lease-Companion"><font color="#FDA4AF">Lease-Companion</font></a>
      <font color="#CBD5E1"> · Team Lead, AI/LLM</font>
    </td>
    <td valign="top" width="33%" bgcolor="#0C2430">
      <font color="#22D3EE"><sub>FOCUS</sub></font><br />
      <strong><font color="#F8FAFC">Evaluation · Grounding · Deployment</font></strong><br />
      <font color="#A5F3FC"><sub>Research with real constraints</sub></font>
    </td>
  </tr>
</table>

<a id="selected-work"></a>
## <font color="#111827">Selected Work</font>

<p><font color="#475569">Three team projects first — each one shows a different way I turn AI systems into useful, testable products.</font></p>

<p>
  <img src="./assets/selected-work-index.svg" alt="Selected work: Lease-Companion, VoiceGuide, and Rainbow Bridge" width="100%" />
</p>

<table width="100%" cellpadding="20" cellspacing="0">
  <tr>
    <td valign="top" width="22%" bgcolor="#26143A">
      <font color="#C084FC"><sub>RECOGNITION</sub></font><br />
      <h3><font color="#F8FAFC">LEASE-COMPANION</font></h3>
      <font color="#DDD6FE"><sub>TEAM LEAD · AI/LLM</sub></font>
    </td>
    <td valign="top" bgcolor="#101827">
      <strong><font color="#F8FAFC">Awarded contract analysis assistant | Team Lead, AI/LLM</font></strong>
      <p><font color="#CBD5E1">A contract review assistant for first-time tenants. It combines document extraction,
      cross-document validation, official-source retrieval, and a Python rule engine to provide
      evidence-backed questions and actions instead of unsafe legal or safety claims.</font></p>
      <font color="#C084FC"><sub>CAPABILITIES</sub></font><br />
      <code>Document AI</code> <code>Rule Engine</code> <code>RAG</code> <code>Privacy</code> <code>Evaluation</code>
      <p>
        <strong><font color="#F8FAFC">Offline evidence</font></strong><br />
        <font color="#A78BFA">Contract checks · 100/100</font>
        <font color="#64748B"> · </font>
        <font color="#FB7185">Judgment cases · 47/47</font><br />
        <font color="#94A3B8"><sub>Fixed offline test data; not real-world contract coverage.</sub></font>
      </p>
      <p>
        <a href="https://github.com/coding-jhj/Lease-Companion"><font color="#C084FC">Repository →</font></a> ·
        <a href="https://github.com/coding-jhj/Lease-Companion/blob/main/docs/ai/evaluation-plan.md"><font color="#FDA4AF">Evaluation Plan →</font></a>
      </p>
    </td>
  </tr>
</table>

<br />

<table width="100%" cellpadding="20" cellspacing="0">
  <tr>
    <td valign="top" width="22%" bgcolor="#321827">
      <font color="#FB7185"><sub>ON-DEVICE AI</sub></font><br />
      <h3><font color="#F8FAFC">VOICEGUIDE</font></h3>
      <font color="#FECDD3"><sub>ACCESSIBILITY · PRIVACY</sub></font>
    </td>
    <td valign="top" bgcolor="#111827">
      <strong><font color="#F8FAFC">Walking assistant for blind and low-vision users</font></strong>
      <p><font color="#CBD5E1">An Android system that runs YOLO/TFLite obstacle detection on device camera frames,
      then delivers stable risk-aware haptic feedback, Korean TTS, and audio cues. The system
      connects FastAPI, GPS events, SSE, and a Cloud Run dashboard without sending raw frames
      to the server.</font></p>
      <font color="#FB7185"><sub>CAPABILITIES</sub></font><br />
      <code>Android</code> <code>Kotlin</code> <code>TFLite</code> <code>YOLO</code> <code>FastAPI</code> <code>Accessibility</code>
      <p><a href="https://github.com/coding-jhj/VoiceGuide"><font color="#FB7185">Repository →</font></a></p>
    </td>
  </tr>
</table>

<br />

<table width="100%" cellpadding="20" cellspacing="0">
  <tr>
    <td valign="top" width="22%" bgcolor="#0C2B36">
      <font color="#22D3EE"><sub>AI INFRASTRUCTURE</sub></font><br />
      <h3><font color="#F8FAFC">RAINBOW BRIDGE</font></h3>
      <font color="#A5F3FC"><sub>CONTRIBUTION BRANCH</sub></font>
    </td>
    <td valign="top" bgcolor="#0E1B27">
      <strong><font color="#F8FAFC">AI and infrastructure contributor | Branch: <code>jeonghwanju</code></font></strong>
      <p><font color="#CBD5E1">Contributed to Qwen3 GPU TTS with asynchronous execution, tone mapping,
      STT/Gemini evaluation, recovery scoring, backend TTS and timeline flows,
      PM2 operations, and the demo video generation pipeline.</font></p>
      <font color="#22D3EE"><sub>CAPABILITIES</sub></font><br />
      <code>Qwen3 TTS</code> <code>GPU Service</code> <code>Evaluation</code> <code>PM2</code> <code>Backend</code>
      <p><a href="https://github.com/mosejong/Rainbow-Bridge/tree/jeonghwanju"><font color="#22D3EE">Contribution Branch →</font></a></p>
    </td>
  </tr>
</table>

<a id="research-direction"></a>
## <font color="#111827">Research Direction</font>

<table width="100%" cellpadding="22" cellspacing="0">
  <tr>
    <td bgcolor="#17112A">
      <font color="#C084FC"><sub>CURRENT DIRECTION</sub></font>
      <h2><font color="#F8FAFC">Post-training Research Engineer</font></h2>
      <p><font color="#CBD5E1">I am building the research engineering foundation needed to make model behavior
      measurable, reproducible, and useful in real products.</font></p>
    </td>
  </tr>
</table>

<br />

<table width="100%" cellpadding="18" cellspacing="0">
  <tr>
    <td valign="top" width="22%" bgcolor="#17223D">
      <font color="#93C5FD"><sub>REPRODUCIBLE MODEL EXPERIMENTS</sub></font>
    </td>
    <td valign="top" bgcolor="#F8FAFC">
      <strong><a href="https://github.com/coding-jhj/foundation-model-lab">foundation-model-lab</a></strong>
      <p>Reproducible decoder-only language model experiments covering tokenizers,
      causal self-attention, compact Transformers, checkpoints, validation loss,
      generation, and experiment records.</p>
      <p><strong>This is a foundation for research engineering and pre-training work, not a claim of completed post-training results.</strong></p>
    </td>
  </tr>
  <tr>
    <td valign="top" bgcolor="#332717">
      <font color="#FBBF24"><sub>EXECUTION WORKSPACE</sub></font>
    </td>
    <td valign="top" bgcolor="#FFFCF4">
      <strong><a href="https://github.com/coding-jhj/MY_CAREER_PLANNER">MY_CAREER_PLANNER</a></strong>
      <p>A Plan → Do → See workspace for research goals, execution logs, reviews,
      and measurable next experiments. It documents my preparation for
      <strong>Post-training Research Engineer</strong> work.</p>
    </td>
  </tr>
  <tr>
    <td valign="top" bgcolor="#26143A">
      <font color="#C084FC"><sub>CURRENT EXPERIMENT TRACK</sub></font>
    </td>
    <td valign="top" bgcolor="#FBFAFF">
      <strong>Local-model direction</strong>
      <p>Lease-Companion contains an optional 7B 4-bit QLoRA comparison track. The current
      repository contains preprocessing, configuration, and evaluation scaffolding;
      <strong>no trained weights or checkpoint are presented as completed results.</strong></p>
    </td>
  </tr>
</table>

<a id="independent-work"></a>
## <font color="#111827">Independent Work</font>

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

## <font color="#111827">Toolkit</font>

<table width="100%" cellpadding="18" cellspacing="0">
  <tr>
    <td bgcolor="#0E1B27">
      <font color="#A5F3FC"><sub>AI SYSTEMS · RESEARCH ENGINEERING · PRODUCT DELIVERY</sub></font><br /><br />
      <code>Python</code> <code>FastAPI</code> <code>Pydantic</code> <code>PostgreSQL</code> <code>Chroma</code> <code>BM25</code> <code>Gemini</code> <code>RAG</code> <code>QLoRA</code><br />
      <code>Kotlin</code> <code>Android</code> <code>TFLite</code> <code>React</code> <code>TypeScript</code> <code>Docker</code> <code>GitHub Actions</code>
    </td>
  </tr>
</table>

## <font color="#111827">All Public Repositories</font>

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

<table width="100%" cellpadding="22" cellspacing="0">
  <tr>
    <td align="center" bgcolor="#090D18">
      <font color="#C084FC"><sub>LET'S CONNECT</sub></font>
      <h2><font color="#F8FAFC">Building toward more reliable AI</font></h2>
      <a href="https://github.com/coding-jhj"><font color="#22D3EE">GitHub →</font></a>
    </td>
  </tr>
</table>
