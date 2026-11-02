# Use in ChatGPT Cloud Projects

1. Create or open a ChatGPT Project.
2. Paste PROJECT_INSTRUCTIONS.md into the project's instructions. Uploading this file alone does not configure instructions.
3. Add COMMANDS.md to the project's Sources/files.
4. Start a new chat inside that project and try `/VERIFY Check whether increasing from 80 to 100 is 25%.`
5. Try `/COMPARE /DECIDE` with real options and constraints. If the library cannot be retrieved, attach the relevant section directly.

You can also paste the instructions into an ordinary chat and attach the command library for that conversation. This does not install a plugin, register slash commands or modify global personalization. No Python installer is needed for this cloud adapter. Account capabilities and workspace policies govern browsing, analysis and file creation. The supplied workflows do not grant new tools or permissions.

Only the necessary files are packaged; there is no personal corpus or API credential. Existing unrelated project instructions should be preserved and reconciled. Select one language edition in a project to avoid contradictory defaults.

Official setup basis, checked 2026-11-02: [ChatGPT Projects](https://learn.chatgpt.com/docs/projects). The project instructions configure behavior; the uploaded library supplies workflow details. The adapter was installed and smoke-tested in a real ChatGPT Project on November 2, 2026. Source retrieval and representative VERIFY/COMPARE/DECIDE scenarios passed; a separate hard-budget boundary check passed. The first response exceeded the requested word limit. Package checks do not establish general reasoning quality or coverage of all 20 workflows.

## Live test scope — November 2, 2026

The project instructions were saved and the command library was added through Sources > Paste text (the UI named it COMMANDS.md.txt). VERIFY, COMPARE and DECIDE were tested using fictional data, including an unsupported claim and a hard-budget boundary. This is not full coverage of all 20 modes. The Claude adapter remains untested in a live Claude account.
