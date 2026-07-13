# RCP de la Ansiedad

> A bilingual, privacy-first open-source project for a future installable RCP reflection skill across Claude, Codex, Hermes and Antigravity/Gemini.

## Status: public development scaffold

This repository is public so the project can be inspected and built in the open. It is **not yet a public clinical release and does not contain an installable Skill**. Do not use this repository as a substitute for professional or emergency care.

The first release will only ship after the canonical RCP source, rights, clinical claims, safety language, English/Spanish parity, attribution and runtime tests are explicitly reviewed.

## What this project is building

RCP means *Reconstrucción Cognitiva del Pensamiento*. The future tool will guide a consenting adult through a structured writing exercise:

1. stressful event;
2. emotions and personal ratings;
3. automatic thoughts and belief ratings;
4. a user-authored reconstruction; and
5. reading and reassessment.

It will not diagnose, interpret a person's mind, prescribe medication, replace therapy, manage an emergency or speak as a psychologist.

## Privacy promise

Personal RCP entries belong to the person using the agent. The project, Fernando, Eduardo and maintainers will never receive, synchronize or read them. No personal RCP text belongs in this repository, its issues, pull requests, telemetry or support channels.

## Supported runtimes planned for the first release

- Antigravity / Gemini
- Claude
- Codex
- Hermes

Text is mandatory. Voice may be supported only when a runtime provides a verified native capability, without changing the method, safety rules or privacy boundary.

## Repository separation

- Public: [rcpansiedad](https://github.com/lunitomx/rcpansiedad) — sanitized code, contracts, public documentation and approved release artifacts only.
- Private: [rcpansiedad-lab](https://github.com/lunitomx/rcpansiedad-lab) — source manuals, videos, hashes, claims review, rights and clinical decisions.

## Spanish

Este repositorio público es un armazón de desarrollo bilingüe, no una versión clínica instalable. RCP es una herramienta de auto-reflexión educativa; no sustituye a un psicólogo ni atiende emergencias. El proyecto agradece a J. Fernando Villanueva Luna por crear la metodología y a Eduardo Luna por impulsar su desarrollo tecnológico y divulgación.

## Contributing

Do not submit personal stories, RCP entries, medical claims, emergency-resource guesses or copied source-manual text. See `docs/public-private-boundary.md` before opening an issue or pull request.
