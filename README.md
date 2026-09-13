<table width="100%" cellpadding="24" cellspacing="0" bgcolor="#0b111d">
  <tr>
    <td valign="top" width="68%">
      <sub><font color="#c4b5fd">AI SYSTEMS · EVALUATION · DEPLOYMENT</font></sub>
      <h1><font color="#f8fafc">Jeong Hwan Ju</font></h1>
      <p><strong><font color="#f0abfc">Post-training Research Engineer</font></strong></p>
      <blockquote>
        <p><font color="#d6deea">Building evaluation-driven AI systems with grounded generation, explicit safety boundaries, and deployment-aware engineering.</font></p>
      </blockquote>
    </td>
    <td valign="top" width="32%">
      <sub><font color="#22d3ee">PROOF AT A GLANCE</font></sub>
      <p><font color="#a78bfa"><strong>03</strong></font><br /><sub><font color="#93a4ba">TEAM PROJECTS</font></sub></p>
      <p><font color="#fb7185"><strong>01</strong></font><br /><sub><font color="#93a4ba">AWARD-WINNING LEAD</font></sub></p>
      <p><font color="#22d3ee"><strong>08</strong></font><br /><sub><font color="#93a4ba">INDEPENDENT WORKS</font></sub></p>
    </td>
  </tr>
</table>

<p align="center">
  <a href="#selected-work"><code>01 · SELECTED WORK</code></a> ·
  <a href="#research-direction"><code>02 · RESEARCH DIRECTION</code></a> ·
  <a href="#independent-work"><code>03 · INDEPENDENT WORK</code></a> ·
  <a href="https://github.com/coding-jhj"><code>GITHUB</code></a>
</p>

<table width="100%" cellpadding="18" cellspacing="0" bgcolor="#0e1726">
  <tr>
    <td valign="top" width="33%">
      <sub><font color="#a78bfa">DIRECTION</font></sub>
      <p><strong>Post-training Research Engineer</strong><br /><sub>Research engineering preparation</sub></p>
    </td>
    <td valign="top" width="34%">
      <sub><font color="#fb7185">RECOGNITION</font></sub>
      <p><strong>Minister of Employment and Labor Award</strong><br /><a href="https://github.com/coding-jhj/Lease-Companion">Lease-Companion</a> · Team Lead, AI/LLM</p>
    </td>
    <td valign="top" width="33%">
      <sub><font color="#22d3ee">SELECTED WORK</font></sub>
      <p><strong>Lease-Companion</strong><br />VoiceGuide · Rainbow Bridge</p>
    </td>
  </tr>
</table>

<a id="selected-work"></a>
<h2>Selected Work</h2>

<p>Three team projects first — each one shows a different way I turn AI systems into useful, testable products.</p>

<table width="100%" cellpadding="18" cellspacing="0" bgcolor="#111b2b">
  <tr>
    <td valign="middle" width="29%" align="center">
      <img src="./assets/projects/project-lease-companion.jpg" alt="Lease-Companion: contract documents connected to evidence validation" width="320" /><br />
      <sub><font color="#a78bfa">CONTRACT / EVIDENCE</font></sub>
    </td>
    <td valign="top">
      <h3>Recognition · <a href="https://github.com/coding-jhj/Lease-Companion">Lease-Companion</a></h3>
      <strong>Awarded contract analysis assistant | Team Lead, AI/LLM</strong>
      <p>A contract review assistant for first-time tenants. It combines document extraction,
      cross-document validation, official-source retrieval, and a Python rule engine to provide
      evidence-backed questions and actions instead of unsafe legal or safety claims.</p>
      <p>
        <sub>STACK</sub><br />
        <code>Document AI</code> <code>Rule Engine</code> <code>RAG</code> <code>Privacy</code> <code>Evaluation</code>
      </p>
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
</table>

<table width="100%" cellpadding="18" cellspacing="0" bgcolor="#111b2b">
  <tr>
    <td valign="middle" width="29%" align="center">
      <img src="./assets/projects/project-voiceguide.jpg" alt="VoiceGuide: smartphone navigation and risk-aware accessibility guidance" width="320" /><br />
      <sub><font color="#fb7185">MOBILE / ACCESSIBILITY</font></sub>
    </td>
    <td valign="top">
      <h3>On-device AI · <a href="https://github.com/coding-jhj/VoiceGuide">VoiceGuide</a></h3>
      <strong>Walking assistant for blind and low-vision users</strong>
      <p>An Android system that runs YOLO/TFLite obstacle detection on device camera frames,
      then delivers stable risk-aware haptic feedback, Korean TTS, and audio cues. The system
      connects FastAPI, GPS events, SSE, and a Cloud Run dashboard without sending raw frames
      to the server.</p>
      <p>
        <sub>STACK</sub><br />
        <code>Android</code> <code>Kotlin</code> <code>TFLite</code> <code>YOLO</code> <code>FastAPI</code> <code>Accessibility</code>
      </p>
      <p><a href="https://github.com/coding-jhj/VoiceGuide">Repository</a></p>
    </td>
  </tr>
</table>

<table width="100%" cellpadding="18" cellspacing="0" bgcolor="#111b2b">
  <tr>
    <td valign="middle" width="29%" align="center">
      <img src="./assets/projects/project-rainbow-bridge.jpg" alt="Rainbow Bridge: GPU service, TTS pipeline, and audio infrastructure" width="320" /><br />
      <sub><font color="#22d3ee">GPU / PIPELINE</font></sub>
    </td>
    <td valign="top">
      <h3>AI Infrastructure · <a href="https://github.com/mosejong/Rainbow-Bridge/tree/jeonghwanju">Rainbow Bridge</a></h3>
      <strong>AI and infrastructure contributor | Contribution branch: <code>jeonghwanju</code></strong>
      <p>Contributed to Qwen3 GPU TTS with asynchronous execution, tone mapping,
      STT/Gemini evaluation, recovery scoring, backend TTS and timeline flows,
      PM2 operations, and the demo video generation pipeline.</p>
      <p>
        <sub>STACK</sub><br />
        <code>Qwen3 TTS</code> <code>GPU Service</code> <code>Evaluation</code> <code>PM2</code> <code>Backend</code>
      </p>
      <p><a href="https://github.com/mosejong/Rainbow-Bridge/tree/jeonghwanju">Contribution Branch</a></p>
    </td>
  </tr>
</table>

<a id="research-direction"></a>
<h2>Research Direction</h2>

<table width="100%" cellpadding="18" cellspacing="8">
  <tr>
    <th align="left" bgcolor="#0e1726">Direction</th>
    <th align="left" bgcolor="#0e1726">Work</th>
    <th align="left" bgcolor="#0e1726">What it demonstrates</th>
  </tr>
  <tr>
    <td valign="top" width="33%" bgcolor="#111b2b">
      <sub><font color="#a78bfa">FOUNDATION MODEL LAB</font></sub>
      <h3><a href="https://github.com/coding-jhj/foundation-model-lab">foundation-model-lab</a></h3>
      <p>Reproducible decoder-only language model experiments covering tokenizers, causal self-attention, compact Transformers, checkpoints, validation loss, generation, and experiment records.</p>
      <hr />
      <sub>This is a foundation for research engineering and pre-training work, not a claim of completed post-training results.</sub>
    </td>
    <td valign="top" width="33%" bgcolor="#111b2b">
      <sub><font color="#fb7185">02 / EXECUTION WORKSPACE</font></sub>
      <h3><a href="https://github.com/coding-jhj/MY_CAREER_PLANNER">MY_CAREER_PLANNER</a></h3>
      <p>A Plan → Do → See workspace for research goals, execution logs, reviews, and measurable next experiments.</p>
      <hr />
      <sub>It documents my preparation for <strong>Post-training Research Engineer</strong> work.</sub>
    </td>
    <td valign="top" width="34%" bgcolor="#111b2b">
      <sub><font color="#22d3ee">LOCAL-MODEL DIRECTION</font></sub>
      <h3>Lease-Companion comparison track</h3>
      <p>An optional 7B 4-bit QLoRA comparison track. The current repository contains preprocessing, configuration, and evaluation scaffolding;<br />
      <sub><strong>no trained weights or checkpoint are presented as completed results.</strong></sub></p>
    </td>
  </tr>
</table>

<a id="independent-work"></a>
<h2>Independent Work</h2>

<p>Independent work is not a list of ideas. It is a record of implementing analysis, search, security, operations, and failure handling.</p>

<table width="100%" cellpadding="14" cellspacing="8">
  <tr>
    <td valign="top" width="50%" bgcolor="#0e1726">
      <sub><font color="#a78bfa">CODE ANALYSIS · AGENT</font></sub>
      <table width="100%" cellpadding="4" cellspacing="0">
        <tr>
          <td valign="top"><h3><a href="https://github.com/coding-jhj/RepoPilot">RepoPilot</a></h3><strong>Evidence-grounded repository analysis agent</strong></td>
          <td valign="top" align="right"><img src="./assets/projects/project-repopilot.jpg" alt="RepoPilot repository analysis evidence graph" width="210" /></td>
        </tr>
      </table>
      <p>Accepts a public GitHub URL, indexes the files, and analyzes Python, JavaScript, and TypeScript structure with static rules. Results retain file-and-line evidence, patch drafts, scope validation, and an optional PR flow.</p>
      <p><code>FastAPI</code> <code>Next.js</code> <code>Static Analysis</code> <code>Evidence</code></p>
      <p><a href="https://jeonghwanju-repopilot.hf.space/">Demo</a> · <a href="https://coding-jhj.github.io/RepoPilot/repopilot-code-guide.html">Code Guide</a></p>
    </td>
    <td valign="top" width="50%" bgcolor="#0e1726">
      <sub><font color="#fb7185">PERSONAL KNOWLEDGE · RAG</font></sub>
      <table width="100%" cellpadding="4" cellspacing="0">
        <tr>
          <td valign="top"><h3><a href="https://github.com/coding-jhj/Personal-AI-Studio">Personal-AI-Studio</a></h3><strong>Source-grounded personal AI workspace</strong></td>
          <td valign="top" align="right"><img src="./assets/projects/project-personal-ai-studio.jpg" alt="Personal-AI-Studio grounded knowledge graph" width="210" /></td>
        </tr>
      </table>
      <p>Unifies documents, code, notebooks, spreadsheets, photo metadata, and MongoDB into one knowledge base. It shows local retrieval results as source cards and connects voice input with a local fallback when an external LLM fails.</p>
      <p><code>Streamlit</code> <code>TF-IDF</code> <code>Voice</code> <code>Fallback</code></p>
      <p><a href="https://jeonghwanju-personal-ai-studio.hf.space">Demo</a></p>
    </td>
  </tr>
  <tr>
    <td valign="top" width="50%" bgcolor="#0e1726">
      <sub><font color="#22d3ee">WEB SEARCH · REACT LOOP</font></sub>
      <table width="100%" cellpadding="4" cellspacing="0">
        <tr>
          <td valign="top"><h3><a href="https://github.com/coding-jhj/AI_AGENT">AI_AGENT</a></h3><strong>Agent that decides when search is needed</strong></td>
          <td valign="top" align="right"><img src="./assets/projects/project-ai-agent.jpg" alt="AI_AGENT search decision and ReAct loop" width="210" /></td>
        </tr>
      </table>
      <p>Analyzes a question, decides whether to search, observes DuckDuckGo results, and continues with another search or an answer through a ReAct loop. It provides a FastAPI API and browser UI without storing the user-provided key on the server.</p>
      <p><code>Gemini</code> <code>LangChain</code> <code>DuckDuckGo</code> <code>FastAPI</code></p>
      <p><a href="https://jeonghwanju-ai-search-agent.hf.space">Demo</a></p>
    </td>
    <td valign="top" width="50%" bgcolor="#0e1726">
      <sub><font color="#bef264">DATA PIPELINE · OPERATIONS</font></sub>
      <table width="100%" cellpadding="4" cellspacing="0">
        <tr>
          <td valign="top"><h3><a href="https://github.com/coding-jhj/Stelive_data">Stelive_data</a></h3><strong>Data product from collection to deployment</strong></td>
          <td valign="top" align="right"><img src="./assets/projects/project-stelive-data.jpg" alt="Stelive_data collection, transformation, and deployment flow" width="210" /></td>
        </tr>
      </table>
      <p>Regularly collects YouTube Data API and CHZZK data, builds JSON and CSV history, regenerates the dashboard, and deploys it to GitHub Pages. The repository captures a repeatable operational flow across different external sources.</p>
      <p><code>Python</code> <code>GitHub Actions</code> <code>JSON/CSV</code> <code>GitHub Pages</code></p>
      <p><a href="https://coding-jhj.github.io/Stelive_data/">Dashboard</a></p>
    </td>
  </tr>
  <tr>
    <td valign="top" width="50%" bgcolor="#0e1726">
      <sub><font color="#fbbf24">DEVELOPER TOOLING · SAFETY</font></sub>
      <table width="100%" cellpadding="4" cellspacing="0">
        <tr>
          <td valign="top"><h3><a href="https://github.com/coding-jhj/claude-pwsh-kit">claude-pwsh-kit</a></h3><strong>Claude Code harness for Windows and PowerShell</strong></td>
          <td valign="top" align="right"><img src="./assets/projects/project-claude-pwsh-kit.jpg" alt="PowerShell safe execution gate" width="210" /></td>
        </tr>
      </table>
      <p>Combines dangerous-command blocking, keyword-based skill routing, research verification guidance, and eight subagent templates. It documents non-ASCII encoding and PowerShell pipe issues and checks them with regression tests.</p>
      <p><code>PowerShell</code> <code>Safety Hooks</code> <code>Skill Router</code> <code>MIT</code></p>
    </td>
    <td valign="top" width="50%" bgcolor="#0e1726">
      <sub><font color="#a78bfa">SECURITY · PASSWORDLESS AUTH</font></sub>
      <table width="100%" cellpadding="4" cellspacing="0">
        <tr>
          <td valign="top"><h3><a href="https://github.com/coding-jhj/aleph-first-homework">Passkey Private Portfolio</a></h3><strong>One service connecting a public portfolio and private workspace</strong></td>
          <td valign="top" align="right"><img src="./assets/projects/project-passkey-private-portfolio.jpg" alt="Passkey boundary between public and private portfolio data" width="210" /></td>
        </tr>
      </table>
      <p>Uses WebAuthn passkeys and separates account-scoped private data through a Vercel API and Supabase PostgreSQL. The security boundary covers challenge replay prevention, session protection, account-scope checks, and RLS.</p>
      <p><code>WebAuthn</code> <code>Vercel</code> <code>Supabase</code> <code>RLS</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top" width="50%" bgcolor="#0e1726">
      <sub><font color="#fb7185">RELIABILITY · DATA PRODUCT</font></sub>
      <table width="100%" cellpadding="4" cellspacing="0">
        <tr>
          <td valign="top"><h3><a href="https://github.com/coding-jhj/ALPEH_FIFTH_HOMEWORK">Real Information Board</a></h3><strong>A dashboard that explains failures honestly</strong></td>
          <td valign="top" align="right"><img src="./assets/projects/project-real-information-board.jpg" alt="Real Information Board failure states and recovery timeline" width="210" /></td>
        </tr>
      </table>
      <p><a href="https://github.com/coding-jhj/ALPEH_FIFTH_HOMEWORK">ALPEH_FIFTH_HOMEWORK</a> and <a href="https://github.com/coding-jhj/MINECRART_DASHBOARD">MINECRART_DASHBOARD</a> distinguish timeout, authentication rejection, rate limits, offline status, and schema changes while preserving the last known good value. Live requests and replay fixtures share the same core path, with nine fixtures covering failure and recovery.</p>
      <p><code>Next.js</code> <code>TypeScript</code> <code>Supabase</code> <code>Replay</code></p>
      <p><a href="https://t04-real-information-board.vercel.app">Demo</a></p>
    </td>
    <td valign="top" width="50%" bgcolor="#0e1726">
      <sub><font color="#22d3ee">CREATIVE ENGINEERING · BROWSER GAME</font></sub>
      <table width="100%" cellpadding="4" cellspacing="0">
        <tr>
          <td valign="top"><h3><a href="https://github.com/coding-jhj/ARKAN_FORGOTTEN_THRONE">ARKAN_FORGOTTEN_THRONE</a></h3><strong>A turn-based RPG playable directly in the browser</strong></td>
          <td valign="top" align="right"><img src="./assets/projects/project-arkan.jpg" alt="ARKAN_FORGOTTEN_THRONE browser RPG world, battle, and growth loop" width="210" /></td>
        </tr>
      </table>
      <p>Connects the world map, town, guild, shop, NPC, dungeon, battle, compendium, and equipment-upgrade flows through static hosting. It includes a Canvas pixel background, modular code, responsive mobile layout, and headless QA for battles, saves, and progression gates.</p>
      <p><code>HTML/CSS/JS</code> <code>Canvas</code> <code>Responsive</code> <code>Playwright</code></p>
      <p><a href="https://coding-jhj.github.io/ARKAN_FORGOTTEN_THRONE/">Play</a></p>
    </td>
  </tr>
</table>

<h2>Toolkit</h2>

<p><sub><font color="#a78bfa">TOOLS</font></sub></p>

<table width="100%" cellpadding="18" cellspacing="8">
  <tr>
    <td valign="top" width="50%" bgcolor="#111b2b">
      <code>Python</code> <code>FastAPI</code> <code>Pydantic</code> <code>PostgreSQL</code> <code>Chroma</code> <code>BM25</code> <code>Gemini</code> <code>RAG</code> <code>QLoRA</code>
    </td>
    <td valign="top" width="50%" bgcolor="#111b2b">
      <code>Kotlin</code> <code>Android</code> <code>TFLite</code> <code>React</code> <code>TypeScript</code> <code>Docker</code> <code>GitHub Actions</code>
    </td>
  </tr>
</table>

<h2>All Public Repositories</h2>

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

<h2>Contact</h2>

<p><a href="https://github.com/coding-jhj"><strong>↳ GitHub</strong></a></p>
