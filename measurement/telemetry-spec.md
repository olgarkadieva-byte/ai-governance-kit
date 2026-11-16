# AI tool telemetry specification

A platform-neutral specification for measuring whether internal AI tools are used,
whether they complete real work, and whether they repay the effort it took to build them.

It is based on the article
[How to Measure AI Tool Adoption, Productivity, and ROI](https://olgasoffice.substack.com/p/were-building-ai-faster-than-ever).

## Principles

1. **Define the questions before the dashboard.** Every event and field below exists to answer a question listed in [Questions this answers](#questions-this-answers).
2. **Execution is not outcome.** A task can finish technically and still not help the person. Capture both completion and usefulness.
3. **One set of definitions across all tools.** "Active user", "completed task", and "time saved" mean the same thing for every AI tool, so tools can be compared.
4. **Platform-neutral.** The spec defines events, dimensions, and metrics. It can be implemented in Adobe Analytics, Amplitude, Mixpanel, Google Analytics, OpenTelemetry, or a data warehouse.
5. **Privacy by design.** Adoption and productivity can be measured without collecting prompts, ticket content, email bodies, or personal communications. Use pseudonymous user IDs and report at team level.

## Event model

One user interaction with an AI tool produces a sequence of events:

```
session_started → task_submitted → tool_invoked (0..n) → task_completed → feedback_submitted (optional)
```

| Event | Fired when | Tells you |
| --- | --- | --- |
| `session_started` | A person opens the AI tool | Usage (someone showed up) |
| `task_submitted` | The person asks the tool to do something | Intent (someone tried to get work done) |
| `tool_invoked` | The AI calls an external tool or data source (for example through MCP) | How the AI does the work: which integrations, how long, how often it retries |
| `task_completed` | The workflow reaches an end state: success, failure, or abandoned | Execution (did it finish?) |
| `feedback_submitted` | The person rates whether the result helped | Outcome (was it useful?) |

The exact fields for each event are defined in [`event-schema.json`](event-schema.json) (JSON Schema) and listed in [`data-dictionary.csv`](data-dictionary.csv).

### Where MCP fits

MCP standardizes how an AI application discovers and calls external tools. It is not a telemetry system.
Instrument `tool_invoked` in the AI application or its orchestration layer, once per external call,
recording the tool name, status, latency, and retry count. MCP also does not grant access by itself:
each integration still needs its own connector, permissions, and authentication.

## Metrics

| Metric | Definition | Notes |
| --- | --- | --- |
| Adoption rate | Active users ÷ eligible users × 100 | The denominator is the people the tool is for, not the whole company. |
| Active user | A person with at least one `task_submitted` in the period | Opening the tool is not enough. |
| Repeat usage rate | Users active in two or more distinct weeks ÷ users who tried it × 100 | Separates habit from curiosity. |
| Task success rate | `task_completed` with `outcome = success` ÷ `task_submitted` × 100 | Execution quality. |
| Usefulness rate | `feedback_submitted` with `useful = true` ÷ all feedback × 100 | Outcome quality, as judged by the user. |
| Time saved (hours) | (Baseline minutes − AI minutes including review) × successful tasks ÷ 60 | Baseline must be defensible; AI time must include review and rework. |
| Development effort payback | Development hours ÷ net hours saved per period | How many periods until the tool repays its build effort. |
| Tasks to break even | Development hours × 60 ÷ minutes saved per task | Same idea, counted in tasks. |

Reference implementations of these formulas are in [`aigov/measurement.py`](../aigov/measurement.py), with tests.

### Worked example

A Jira debugging assistant took **120 engineering hours** to build. An engineer spends **25 minutes**
investigating a typical issue manually and **8 minutes** with the assistant, including reviewing its output.

- Time saved per task: 17 minutes
- 100 successful tasks: 100 × 17 ÷ 60 = **28.3 hours saved**
- If it saved 15 minutes per task, it would need 120 × 60 ÷ 15 = **480 successful tasks** to break even.

```python
from aigov import time_saved_hours, tasks_to_break_even

time_saved_hours(25, 8, 100)      # 28.3
tasks_to_break_even(120, 15)      # 480
```

## Reference data you also need

Some metrics cannot come from events alone. Keep these as small reference tables:

| Table | Fields | Used for |
| --- | --- | --- |
| Eligible users | `team_id`, `eligible_user_count`, `period` | Adoption rate denominator |
| Task baselines | `tool_id`, `workflow`, `baseline_minutes`, `baseline_method`, `measured_on` | Time saved |
| Development investment | `tool_id`, `development_hours`, `maintenance_hours_per_period`, `run_cost_per_period` | Payback |

## Questions this answers

- Which AI tools have the highest repeat adoption?
- Which teams are realizing the greatest estimated time savings?
- Which tools have recovered their development investment?
- Which tools are heavily used but struggle to complete tasks?
- Where are the estimates strong, and where do they need more validation?

## Cautions

- **Usage is not value.** Track usage, but never make it the success KPI.
- **Recovered time is not cash.** Saved hours usually become capacity, speed, or quality, not lower payroll. Report it that way.
- **Count the full cost.** Include maintenance, infrastructure, model usage, and the time people spend validating AI output.
- **Set a guardrail.** A speed gain that lowers quality or raises complaints is not a win.
