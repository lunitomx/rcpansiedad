# Runtime contract

The first release targets Antigravity/Gemini, Claude, Codex and Hermes.

Every adapter must preserve the same behavior:

- English and Spanish support;
- text-complete flow;
- explicit safety check before RCP;
- separate consent before starting;
- pause, exit, export and delete intents;
- no project-controlled journal transmission;
- transparent AI identity;
- optional native voice only when verified by that runtime;
- no default audio or full-transcript retention.

Runtime-specific syntax belongs in adapter packages only after the shared content and safety contract are approved.
