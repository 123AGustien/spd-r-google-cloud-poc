from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Dict

app = FastAPI()

class SimulationRequest(BaseModel):
    event_id: str
    input: Dict[str, Any]

processed_events = {}

@app.post("/v1/simulate")
def simulate(request: SimulationRequest):

    # Idempotency check
    if request.event_id in processed_events:
        return processed_events[request.event_id]

    # Basic validation
    if not request.input:
        raise HTTPException(status_code=400, detail="Invalid input")

    # Simulated processing
    result = {
        "status": "success",
        "event_id": request.event_id,
        "result": {
            "processed": True,
            "output_value": request.input.get("value", 0)
        }
    }

    processed_events[request.event_id] = result

    return result

Add core simulation API (FastAPI service)
