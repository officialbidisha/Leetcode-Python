# Guardrails — layered pipeline

Two layers, cheapest-first:

1. **`fast_filters.py`** — regex-only, no API call. Catches known prompt-injection
   phrases (`BLOCK`) and PII in the input (`FLAG`).
2. **`llm_classifier.py`** — only runs if the fast filter didn't already block.
   Uses `client.messages.parse()` with a Pydantic schema to get a reliable
   category + reasoning for jailbreaks, harmful requests, and off-topic input.

`pipeline.py` ties both together plus an **output** check (`output_validator.py`,
reuses the PII regexes on the model's response) and handles the server-side
`stop_reason == "refusal"` case explicitly.

## Setup

```bash
python3 -m venv .venv && .venv/bin/pip install -r llm_engineering/requirements.txt
export ANTHROPIC_API_KEY=your-key   # or `ant auth login`
```

## Run the demo (calls the API — costs a few cents)

```bash
.venv/bin/python -m llm_engineering.examples.run_guardrails_demo
```

## What's here vs. what a real system needs

- Fast filters are a starting point — the injection phrase list is small and
  the credit-card regex is a naive digit-count match. Real systems combine
  this with a maintained deny-list and/or a dedicated PII-detection library.
- The classifier is a single categorical judge — in production you'd run it
  against a labeled eval set (see the `evals` deep-dive, once we get there)
  to know its actual precision/recall before trusting it to block traffic.
- No logging/observability layer — every `GuardrailResult` should be logged
  with a request ID in a real deployment so blocked requests are auditable.
