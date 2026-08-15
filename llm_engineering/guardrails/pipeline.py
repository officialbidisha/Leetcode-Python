from __future__ import annotations

from typing import Any

import anthropic

from .fast_filters import run_fast_filters
from .llm_classifier import classify_input
from .models import GuardrailResult, Verdict
from .output_validator import check_output


def combine(results: list[GuardrailResult]) -> Verdict:
    if any(r.verdict == Verdict.BLOCK for r in results):
        return Verdict.BLOCK
    if any(r.verdict == Verdict.FLAG for r in results):
        return Verdict.FLAG
    return Verdict.ALLOW


class GuardrailPipeline:
    """Layered guardrail: cheap regex filters run first and can short-circuit
    before paying for an LLM classification call or the main generation call."""

    def __init__(self, client: anthropic.Anthropic, model: str = "claude-opus-5"):
        self.client = client
        self.model = model

    def check_input(self, text: str) -> list[GuardrailResult]:
        results = [run_fast_filters(text)]
        if results[-1].verdict != Verdict.BLOCK:
            results.append(classify_input(self.client, text, self.model))
        return results

    def generate(self, user_input: str, system: str | None = None) -> dict[str, Any]:
        input_checks = self.check_input(user_input)

        if combine(input_checks) == Verdict.BLOCK:
            return {
                "response": None,
                "blocked_at": "input",
                "input_checks": input_checks,
            }

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=system,
            messages=[{"role": "user", "content": user_input}],
        )

        if response.stop_reason == "refusal":
            return {
                "response": None,
                "blocked_at": "model_refusal",
                "input_checks": input_checks,
                "refusal_category": getattr(response.stop_details, "category", None),
            }

        output_text = next((b.text for b in response.content if b.type == "text"), "")
        output_checks = check_output(output_text)
        output_verdict = combine(output_checks)

        return {
            "response": output_text if output_verdict != Verdict.BLOCK else None,
            "blocked_at": "output" if output_verdict == Verdict.BLOCK else None,
            "input_checks": input_checks,
            "output_checks": output_checks,
        }
