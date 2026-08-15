from __future__ import annotations

from .fast_filters import redact_pii
from .models import Category, GuardrailResult, Verdict


def check_output(text: str) -> list[GuardrailResult]:
    """Checks run on the model's response before it reaches the user."""
    redacted, found = redact_pii(text)
    if found:
        return [
            GuardrailResult(
                verdict=Verdict.BLOCK,
                category=Category.PII_DETECTED,
                layer="output_filter",
                reason=f"response contained PII: {', '.join(found)}",
                redacted_text=redacted,
            )
        ]

    return [
        GuardrailResult(
            verdict=Verdict.ALLOW,
            category=Category.SAFE,
            layer="output_filter",
            reason="no PII detected in response",
        )
    ]
