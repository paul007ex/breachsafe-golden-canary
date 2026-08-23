# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
"""Command-line entry point for Golden Canary."""

from __future__ import annotations

import argparse

from golden_canary import __version__, greeting


def main(argv: list[str] | None = None) -> int:
    """Run the breachsafe-golden-canary command-line interface.

    Args:
        argv: Argument vector (defaults to ``sys.argv[1:]``). Pass an explicit
            list in tests so parsing is hermetic.

    Returns:
        The process exit code; ``0`` indicates success.
    """
    parser = argparse.ArgumentParser(
        prog="breachsafe-golden-canary",
        description="Canary repo: proves the golden-python scaffold and reusable CI actually run end to end.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.parse_args(argv)
    print(greeting("Golden Canary"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
