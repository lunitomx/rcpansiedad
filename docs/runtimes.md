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

The alpha includes one manifest per target runtime under `adapters/`. These manifests describe the shared contract; the exact installation destination remains host-specific and must be verified during Fer's test pass.
