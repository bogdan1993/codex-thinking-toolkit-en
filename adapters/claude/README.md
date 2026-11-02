# Claude — EN

## Claude cloud

Enable code execution/file creation if required by your account. Open Customize > Skills, add/create a skill, choose Upload a skill, and upload **thinking-toolkit-en.zip** from this directory. Enable the uploaded skill. Do not upload the ZIP of the whole repository. Ask: "Use thinking-toolkit-en, verify mode: is an increase from 80 to 100 equal to 25%?" All 20 workflows live in one skill with references; it does not create 20 separate cloud menu commands.

## Claude Code (local, optional)

Copy the **thinking-toolkit-en** folder into `~/.claude/skills/` (personal) or `.claude/skills/` in your project. Keep existing different folders; back up before replacing an older edition. Invoke `/thinking-toolkit-en verify ...` or name another mode. A distinct toolkit name avoids collisions with built-in commands such as /plan. This does not install the skill into cloud sessions; use the account upload route for cloud.

## Sources and verification

Checked 2026-11-02: [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude), [Create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills), [Claude Code skills](https://code.claude.com/docs/en/skills).

The ZIP contains one skill folder at its root, with SKILL.md, all 20 references and LICENSE. Local packaging checks verify content, reference links and reproducibility. Claude account upload, invocation and model behavior have not been tested live. Tool availability and organization policy can affect use.
