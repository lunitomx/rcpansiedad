# Installation — `0.1.0-alpha`

This release is a portable Skill folder for controlled testing. It is text-complete in English and Spanish and does not need a server, account, MCP connection or project backend.

## Portable installation

1. Download or clone this repository.
2. Copy `skills/rcpansiedad/` into the host agent's local Skills directory.
3. Restart or reload the host agent's Skills.
4. Start with a synthetic test prompt such as: `I am frustrated with my workday; guide me through RCP.`
5. Confirm that the safety gate appears before Step 1.

The exact destination and reload action are host-specific. The package is intentionally portable so Claude, Codex, Hermes and Antigravity/Gemini can load the same `SKILL.md` without a project server. Do not paste personal RCP entries into GitHub issues or test reports.

## Runtime expectations

- Claude: install the folder through the local Skills mechanism.
- Codex: install the folder through the local Skills mechanism.
- Hermes: install the folder through the local Skills mechanism.
- Antigravity/Gemini: install the folder through the local Skills mechanism.

If a host cannot guarantee local-only handling, use the Skill without saving or do not install it.

## What this is not

This is not a medical device, diagnosis, crisis service or replacement for a psychologist, physician or emergency service. It is an alpha release for controlled review.
