# cross-agent-event-bus

Event backbone for resilient communication and workflow choreography.

## Scope

Topic design, schema contracts, and idempotent consumer handling.

## Capabilities

- Topic design, schema contracts, and idempotent consumer handling.
- Saga orchestration patterns for multi-step recovery workflows.
- Delivery guarantees with dead-letter and replay controls.
- Cross-service observability and ordered event processing support.

## Repository Layout

- `src/main.py` entrypoint and lightweight service bootstrap
- `src/project_profile.py` canonical project metadata
- `src/service_contract.py` baseline domain contract shape
- `tests/` smoke and contract tests
- `docs/` architecture and roadmap

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest -q
python -m src.main
```
