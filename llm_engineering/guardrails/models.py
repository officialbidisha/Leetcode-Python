from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Verdict(str, Enum):
    ALLOW = "allow"
    BLOCK = "block"
    FLAG = "flag"


class Category(str, Enum):
    SAFE = "safe"
    PII_DETECTED = "pii_detected"
    PROMPT_INJECTION = "prompt_injection"
    JAILBREAK_ATTEMPT = "jailbreak_attempt"
    HARMFUL_CONTENT = "harmful_content"
    OFF_TOPIC = "off_topic"


@dataclass
class GuardrailResult:
    verdict: Verdict
    category: Category
    layer: str
    reason: str
    redacted_text: str | None = None
