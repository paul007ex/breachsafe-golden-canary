#!/usr/bin/env bats
# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
#
# Black-box CLI smoke tests for Golden Canary, driven through the INSTALLED
# console script (not the Python API). bats-core is provided by the
# breachsafe-container image; install locally with `brew install bats-core`.
# Run with `just test-cli`.

setup() {
    # Prefer the console script on PATH (activated venv / container); otherwise
    # fall back to `uv run` so the harness works from a bare checkout too.
    if command -v breachsafe-golden-canary >/dev/null 2>&1; then
        CLI=(breachsafe-golden-canary)
    else
        CLI=(uv run breachsafe-golden-canary)
    fi
}

@test "--help exits 0 and prints usage" {
    run "${CLI[@]}" --help
    [ "$status" -eq 0 ]
    [[ "$output" == *"usage:"* ]]
    [[ "$output" == *"breachsafe-golden-canary"* ]]
}

@test "--version exits 0 and prints the version" {
    run "${CLI[@]}" --version
    [ "$status" -eq 0 ]
    [[ "$output" == *"0.0.1"* ]]
}

@test "default invocation exits 0 and greets" {
    run "${CLI[@]}"
    [ "$status" -eq 0 ]
    [[ "$output" == *"Golden Canary"* ]]
}
