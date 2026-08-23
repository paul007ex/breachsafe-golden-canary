<!-- SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0 -->
# Golden Canary

Canary repo: proves the golden-python scaffold and reusable CI actually run end to end.

Source-available under **PolyForm-Noncommercial-1.0.0** (not open source; non-commercial use).

A BreachSAFE Quantum Platform (BQP) `python-cli` component, scaffolded from
[`paul007ex/breachsafe-repo`](https://github.com/paul007ex/breachsafe-repo).

## Requirements

- Python 3.14
- [`uv`](https://github.com/astral-sh/uv)

## Develop

```bash
just setup            # uv venv --python 3.14 + uv pip install -e '.[dev]'
just gates            # lint, format-check, typecheck, arch, test (>= 90% cov), sast, deps, reuse
uv run breachsafe-golden-canary
```

## Test harness

This repo ships a layered, mostly-black-box test harness:

- **Unit** — `just test` (pytest, coverage floor 90%).
- **Property** — `tests/property/` (hypothesis) invariants over generated inputs.
- **Black-box CLI** — `just test-cli` runs `tests/cli/*.bats` (bats-core) against the installed
  `breachsafe-golden-canary` console script. bats is provided by the breachsafe-container image; install
  locally with `brew install bats-core`.
- **Architecture** — `just arch` (import-linter contracts in `pyproject.toml`).
- **Reporting** — `just test-report` writes `.allure-results`; the Allure CLI viewer ships in the
  workbench image (`allure serve .allure-results`).
- **Fuzzing** — atheris harnesses in `tests/fuzz/` (see below).
- **Mutation (opt-in)** — `just mutate` (mutmut) for security/validation-critical modules.

## Run

```bash
uv run breachsafe-golden-canary
# or
uv run python -m golden_canary
```

## Security posture & fuzzing

This repo carries a SHA-pinned, least-privilege security-posture layer:

- **OpenSSF Scorecard** and **CodeQL** (`security-extended`) run on a schedule and on PRs.
- **Fuzzing** uses shared [Atheris](https://github.com/google/atheris) harnesses in
  [`tests/fuzz/`](tests/fuzz/), consumed by two tiers: **ClusterFuzzLite** runs per-PR in CI for
  every repo; **Google OSS-Fuzz** provides hosted continuous fuzzing for Apache/OSS repos after a
  one-time onboarding PR (`oss-fuzz/`, generated for Apache repos only). PolyForm repos rely on
  ClusterFuzzLite. Write a harness once; both tiers use it.
- **Commit `uv.lock`.** Run `just lock` and commit the result — CI runs `uv sync --locked` and
  OpenSSF Scorecard's Pinned-Dependencies check both require a committed lockfile.

## Contributing

Read [`CLAUDE.md`](CLAUDE.md) for the inherited invariants and process rules, and
[`CONTRIBUTING.md`](CONTRIBUTING.md) for the workflow. Non-surgical changes require a decision
record under [`docs/decisions/`](docs/decisions/). Report vulnerabilities per
[`SECURITY.md`](SECURITY.md).

## Staying in sync with the template

```bash
just template-update   # uvx copier update --trust
```
