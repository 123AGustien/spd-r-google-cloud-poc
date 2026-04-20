# SPD-R Google Cloud Proof of Concept

## Overview

The Supervisory Protocol for Data Resilience (SPD-R) is a Proof of Concept designed to model system-level resilience, dependency propagation, and failure behavior in distributed cloud architectures.

It introduces a cascade trace model that captures how events flow through interconnected systems, enabling deterministic analysis of system behavior under controlled conditions.

This project is intended for sandbox-based evaluation only.

---

## Core Capabilities

### Event Simulation API
A REST API that processes synthetic events and returns deterministic responses.

Endpoint:
POST /v1/simulate

---

### Cascade Trace Model
The system supports hierarchical event relationships where each event can generate downstream dependent events.

Example:
- invoice.created → invoice.paid → payment.settled

See: /docs/sample-trace.json

---

### Deterministic Processing
Identical inputs produce consistent outputs for reproducible evaluation.

---

## System Architecture

- FastAPI backend
- Stateless processing model
- Optional SQLite trace storage (extended version)
- Docker containerized deployment

---

## Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- Docker

---

## Run Instructions

### Build
docker build -t spd-r-api .

### Run
docker run -p 8000:8000 spd-r-api

---

## Example Request

```json
{
  "event_id": "evt_001",
  "input": {
    "type": "simulation",
    "value": 250
  }
}


Example Response{
  "status": "success",
  "event_id": "evt_001",
  "result": {
    "processed": true,
    "output_value": 250
  }
}



Key Design Principles
Stateless execution
Deterministic behavior
Synthetic data only
Sandbox-safe architecture
No production dependencies
Supporting Artifacts
/docs/sample-trace.json → Cascade trace example
/docs/technical-appendix.md → Evaluation framework (optional)
Status
Proof of Concept – Early Stage Architecture Validation

---

