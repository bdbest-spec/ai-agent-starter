from __future__ import annotations

BAD_PATTERNS = {
    "hack": "unauthorized access",
    "malware": "malicious software",
    "phishing": "deception or impersonation",
    "credential": "credential theft",
    "bypass": "security bypass",
    "exploit": "exploitation",
    "fraud": "fraudulent activity",
    "steal": "unauthorized taking",
    "blackmail": "coercion",
}

ETHICAL_VALUES = {
    "truthfulness": "Do not invent facts or claim certainty without evidence.",
    "justice": "Be fair, balanced, and respectful to all people.",
    "mercy": "Reduce harm and treat others with dignity.",
    "wisdom": "Use sound reasoning and avoid unnecessary risk.",
    "responsibility": "Protect privacy, safety, and accountability.",
    "restraint": "Avoid harmful, deceptive, or manipulative behavior.",
}


def ethical_guard(text: str) -> tuple[bool, str | None]:
    lowered = text.lower()
    for keyword, reason in BAD_PATTERNS.items():
        if keyword in lowered:
            return False, f"This request is not allowed because it seeks {reason}."
    return True, None


def get_ethics_summary() -> str:
    return "\n".join(f"- {key.title()}: {value}" for key, value in ETHICAL_VALUES.items())
