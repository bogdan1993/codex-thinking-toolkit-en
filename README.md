# Codex Thinking Toolkit — English

## Cloud editions: Claude and ChatGPT

| Platform | Setup | Ready-to-upload package |
|---|---|---|
| Claude cloud / Claude Code | [Claude guide](adapters/claude/README.md) | [thinking-toolkit-en.zip](https://github.com/bogdan1993/codex-thinking-toolkit-en/raw/refs/heads/main/adapters/claude/thinking-toolkit-en.zip) |
| ChatGPT Cloud Projects | [ChatGPT guide](adapters/chatgpt/README.md) | [ChatGPT package](https://github.com/bogdan1993/codex-thinking-toolkit-en/raw/refs/heads/main/adapters/chatgpt/thinking-toolkit-en-chatgpt.zip) |

Claude uses one skill with 20 referenced modes. ChatGPT uses project instructions and an uploaded command library. Both cloud packages are separate from the local Codex installer. Read the platform guide before uploading; uploading a whole repository is not installation. Live account behavior has not been tested.

**20 composable skills for research, critical thinking, decisions, planning and communication.** Each skill is a small instruction workflow you can invoke individually or combine with others.

English edition of [codex-thinking-toolkit](https://github.com/bogdan1993/codex-thinking-toolkit). Created by **Bogdan Pădurariu with Codex**. MIT licensed. This is an independent project, not an official OpenAI product.

## Install

Requires Codex with local file access and **Python 3.10+** for the installer. The installer and tests use only the Python standard library. Actual research, browsing and artifact creation use the tools available in your Codex session.

```bash
git clone https://github.com/bogdan1993/codex-thinking-toolkit-en.git
cd codex-thinking-toolkit-en
python3 install.py --check
python3 install.py
```

The default destination is `$CODEX_HOME/skills`, falling back to `~/.codex/skills`. To choose another supported location:

```bash
python3 install.py --dest /absolute/path/to/skills --check
python3 install.py --dest /absolute/path/to/skills
```

`--check` writes nothing. Installation verifies the skill files against the packaged SHA-256 manifest, checks every destination before copying, leaves identical installations alone, and refuses to replace different existing skills. If copying fails, it removes only newly created skill directories. Hashes detect accidental changes; they are not publisher signatures.

After installation, start a new chat or refresh skill discovery if needed. Use `$analyze`, `$verify`, etc. `/ANALYZE` and similar aliases are plain conversational text, not native slash commands registered by this installer.

**Choose one edition per installation location.** Both editions intentionally use the same 20 skill names. The installer will report a conflict if a different edition or a modified skill already exists. Back up or move selected old directories yourself before switching; there is no force-overwrite option. You can also copy selected `skills/<name>` folders manually if you only want a subset.

## Skills

| Invocation | Purpose | Example task |
|---|---|---|
| `$master` | Select useful stages; coordinate a complex task | Coordinate an analysis and decision using supplied evidence; no browsing needed. |
| `$research` | Investigate with sources actually read | Compare two reports and identify independent evidence. |
| `$fresh` | Check recency and distinguish dates | Check whether the cited release information is still current. |
| `$verify` | Check claims and calculations | Verify that an increase from 80 to 100 is 25%. |
| `$source-check` | Assess credibility and independence | Find whether three articles repeat one press release. |
| `$expert-lens` | Compare disciplinary perspectives | Examine AI adoption through technical and organizational lenses. |
| `$analyze` | Find relationships and implications | Analyze retention data without assuming causation. |
| `$assumptions` | Expose assumptions and unknowns | Identify assumptions that could change this budget. |
| `$compare` | Use common criteria across alternatives | Compare options with a stated budget and missing data. |
| `$critique` | Find concrete weaknesses and preserve strengths | Review this project plan against its objective. |
| `$red-team` | Explore plausible failures and mitigation | Stress-test the plan if its supplier becomes unavailable. |
| `$decide` | Make a supported or conditional recommendation | Choose from the supplied options under budget constraints. |
| `$plan` | Define stages, dependencies and acceptance | Plan a two-hour workshop for 12 people. |
| `$next` | Choose concrete next actions | Prioritize what to do after booking the venue. |
| `$checklist` | Make requirements verifiable | Create acceptance checks for a report containing tables. |
| `$optimize` | Improve an existing baseline | Shorten an existing process while preserving effective steps. |
| `$audience` | Adapt to a defined audience | Explain two-factor authentication to beginners. |
| `$rewrite` | Preserve meaning while changing expression | Rewrite this email warmly without adding commitments. |
| `$content-suite` | Adapt one message distinctly by channel | Create a LinkedIn post and short video from one idea. |
| `$brand` | Apply documented identity | Apply the supplied brand guide without inventing tokens. |

## Combining skills

```text
$research $source-check Compare the supplied reports and assess source independence.
$analyze $assumptions Explain the result and identify assumptions that could change it.
$compare $decide Compare these options and recommend one under the stated constraints.
$plan $checklist Plan the workshop and define observable acceptance criteria.
$rewrite $audience Adapt this existing email for a nontechnical audience.
```

Use `$master` when coordination adds value; it does not automatically run all 20 skills. Ask for the desired output and constraints in ordinary language. Default output language is English unless the request or context says otherwise. No API key, login or personal author corpus is bundled. Personal voice and brand profiles are optional inputs, not dependencies on a particular outside skill.

## Verification and limits

```bash
python3 -B -m unittest discover -s tests -v
python3 install.py --check --dest /absolute/path/to/a/test-skills-directory
```

The automated tests exercise installation, idempotence, conflict handling, rollback, Unicode-safe copying, path handling and source integrity. [Evaluation scenarios](docs/EVALUATION.md) describe behavior to check with an actual Codex session. File validation does not prove reasoning quality. These workflows cannot guarantee research accuracy, manufacture access to missing sources or grant permission for external actions. A plan or recommendation alone does not authorize execution.

To uninstall, back up any edits and remove only the chosen installed skill directories. The installer changes no global Codex configuration. It installs all 20 skills and does not silently replace existing names.

## Structure and provenance

- `skills/`: 20 self-contained instruction folders, each with its license.
- `manifest.json`: edition, version, skill names and file hashes.
- `install.py`: standard-library installer.
- `tests/`: automated installer checks.
- `docs/EVALUATION.md`: behavioral evaluation cases and release verification scope.

English adaptation of the author's Romanian command catalog. The English edition preserves task scope and evidence rules while translating instructions, examples and verdict labels. Personal voice samples, client records and private project paths are excluded.
