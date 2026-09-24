from __future__ import annotations

import json
from pathlib import Path
from typing import Any


POLICY_PATH = Path(__file__).resolve().parent.parent / "config" / "agent_policy.json"


def load_repository_policy() -> dict[str, Any]:
    """Load project policy; repository permissions remain enforced by GitHub."""
    with POLICY_PATH.open(encoding="utf-8") as policy_file:
        return json.load(policy_file)


def validate_write_operation(operation: str, confirmed: bool) -> tuple[bool, str]:
    """Apply local approval rules before a future repository tool is called."""
    policy = load_repository_policy()
    allowed = operation in policy.get("allowed_operations", [])
    requires_confirmation = (
        policy.get("approval_policy", {}).get("write_operations")
        == "require_explicit_confirmation"
    )

    if not allowed:
        return False, f"Operation is not allowed by policy: {operation}"
    if requires_confirmation and not confirmed:
        return False, "Explicit confirmation is required before a write operation."
    return True, "Operation is allowed."
