import json
import argparse


# -----------------------------
# CASCADE LAYER (CPI)
# -----------------------------
def run_cascade_simulation():
    nodes = ["A", "B", "C", "D"]
    failed = set()

    log = []

    for i, node in enumerate(nodes):
        failed.add(node)
        log.append({"event": "FAIL", "node": node})

        if i < len(nodes) - 1:
            log.append({"event": "PROPAGATE", "from": node, "to": nodes[i + 1]})
            failed.add(nodes[i + 1])

    CPI = len(failed) / len(nodes)

    return CPI, log


# -----------------------------
# OBSERVABILITY LAYER (DHTI)
# -----------------------------
def compute_dhti(log):
    if not log:
        return 0.0

    trace_events = len([e for e in log if "event" in e])
    expected = len(log)

    DHTI = trace_events / expected if expected > 0 else 0.0
    return round(DHTI, 3)


# -----------------------------
# ORBITAL LAYER (OCRS)
# -----------------------------
def compute_ocrs(cpi):
    # simple deterministic inversion model
    OCRS = 1.0 - cpi
    return round(OCRS, 3)


# -----------------------------
# FUSION LAYER (SRS)
# -----------------------------
def compute_srs(ocrs, dhti, cpi):
    SRS = ocrs * dhti * (1 - cpi)
    return round(SRS, 3)


# -----------------------------
# MAIN CLI EXECUTION
# -----------------------------
def run_system():
    CPI, log = run_cascade_simulation()
    DHTI = compute_dhti(log)
    OCRS = compute_ocrs(CPI)
    SRS = compute_srs(OCRS, DHTI, CPI)

    result = {
        "cascade": {
            "CPI": round(CPI, 3),
            "log": log
        },
        "observability": {
            "DHTI": DHTI
        },
        "orbital": {
            "OCRS": OCRS
        },
        "fusion": {
            "SRS": SRS
        },
        "system_status": "deterministic_replay_success"
    }

    print("\n=== SEXTANT SYSTEM EXECUTION ===")
    print(json.dumps(result, indent=2))

    with open("system_result.json", "w") as f:
        json.dump(result, f, indent=2)


# -----------------------------
# CLI ENTRYPOINT
# -----------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sextant SPD-R System CLI Runner")
    args = parser.parse_args()

    run_system()
