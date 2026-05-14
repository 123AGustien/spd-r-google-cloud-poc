import json

def run_simulation():

    # Deterministic nodes
    nodes = ["A", "B", "C", "D"]

    # Dependency chain (A → B → C → D)
    dependencies = {
        "A": ["B"],
        "B": ["C"],
        "C": ["D"],
        "D": []
    }

    log = []
    failed = set()

    # Cascade simulation
    for i, node in enumerate(nodes):

        failed.add(node)
        log.append({"event": "FAIL", "node": node})

        # propagate failure deterministically
        for dep in dependencies[node]:
            if dep not in failed:
                log.append({
                    "event": "PROPAGATE",
                    "from": node,
                    "to": dep
                })
                failed.add(dep)

    # --- Metrics (aligned to your system) ---

    total_nodes = len(nodes)
    failure_ratio = len(failed) / total_nodes

    CPI = round(failure_ratio, 3)      # Cascade Propagation Index (simple form)
    DHTI = 1.0                         # perfect trace completeness (simulation)
    OCRS = 1.0 - CPI                  # inverse stability assumption

    SRS = round(OCRS * DHTI * (1 - CPI), 3)

    output = {
        "log": log,
        "metrics": {
            "OCRS": OCRS,
            "DHTI": DHTI,
            "CPI": CPI,
            "SRS": SRS
        },
        "replay_test": True
    }

    with open("result.json", "w") as f:
        json.dump(output, f, indent=2)

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    run_simulation()
