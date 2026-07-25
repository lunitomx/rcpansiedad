# RCP de la Ansiedad

> A bilingual, privacy-first open-source project with a portable RCP reflection Skill for Claude, Codex, Hermes and Antigravity/Gemini.

## Status: `0.1.0-alpha` controlled testing

This repository contains the first installable alpha Skill for controlled testing. It is **not a clinical release, crisis service or substitute for professional or emergency care**. Use synthetic scenarios during review and never publish personal RCP entries.

The method source, digital adaptation, initial safety boundary and attribution were confirmed by Fer as reported in the private lab. Technical gates, four-runtime verification and public feedback remain open before a stable release.

## Install for a controlled test

See [installation.md](docs/installation.md) and use the Skill folder at [`skills/rcpansiedad/`](skills/rcpansiedad/). Fer's synthetic test plan is in [fer-test.md](docs/fer-test.md).

## What this project provides

RCP means *Reconstrucción Cognitiva del Pensamiento*. The future tool will guide a consenting adult through a structured writing exercise:

1. stressful event;
2. emotions and personal ratings;
3. automatic thoughts and belief ratings;
4. a user-authored reconstruction; and
5. reading and reassessment.

It does not diagnose, interpret a person's mind, prescribe medication, replace therapy, manage an emergency or speak as a psychologist.

## Privacy promise

Personal RCP entries belong to the person using the agent. The project, Fernando, Eduardo and maintainers will never receive, synchronize or read them. No personal RCP text belongs in this repository, its issues, pull requests, telemetry or support channels.

## Supported runtimes planned for the first release

- Antigravity / Gemini
- Claude
- Codex
- Hermes

Text is mandatory. Voice may be supported only when a runtime provides a verified native capability, without changing the method, safety rules or privacy boundary.

## Repository separation

- Public: [rcpansiedad](https://github.com/lunitomx/rcpansiedad) — sanitized code, contracts, public documentation and alpha release artifacts only.
- Private: [rcpansiedad-lab](https://github.com/lunitomx/rcpansiedad-lab) — source manuals, videos, hashes, claims review, rights and clinical decisions.

## Spanish

Este repositorio público contiene una primera Skill bilingüe para pruebas controladas; no es una versión clínica ni atiende emergencias. RCP es una herramienta de auto-reflexión educativa y no sustituye a un psicólogo, médico o servicio de emergencia. Agradecemos a J. Fernando Villanueva Luna por crear la metodología y a Eduardo Luna por impulsar su desarrollo tecnológico y divulgación.

La metodología y recursos oficiales de Fer pueden conocerse en [su sitio](https://psicologoqueretaro.com/) y en [la playlist de YouTube](https://www.youtube.com/playlist?list=PLbGKfvX_T7EPDV-bcI--z42VSz4Xxdyor).

## Contributing

Do not submit personal stories, RCP entries, medical claims, emergency-resource guesses or copied source-manual text. See `docs/public-private-boundary.md` before opening an issue or pull request.
