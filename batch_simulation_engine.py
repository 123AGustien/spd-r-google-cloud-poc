import json
import random

# -----------------------------
# SINGLE SIMULATION (your existing logic simplified)
# -----------------------------
def run_single_simulation(seed: int):
    random.seed(seed)

    nodes = ["A", "B", "C", "D"]
    failed = 0

    for node in nodes:
        # probabilistic failure instead of forced failure
        if random.random() < 0.6:
            failed += 1

    cpi = failed / len(nodes)
    ocrs = 1 - cpi
    dhti = random.uniform(0.7, 1.0)

    srs = ocrs * dhti * (1 - cpi)

    return round(srs, 4)

# -----------------------------
# BATCH RUNNER
# -----------------------------
def run_batch(n=200):
    results = []

    for i in range(n):
        srs = run_single_simulation(i)
        results.append(srs)

    stats = {
        "count": n,
        "mean_srs": sum(results) / n,
        "min_srs": min(results),
        "max_srs": max(results),
        "results": results
    }

    with open("batch_results.json", "w") as f:
        json.dump(stats, f, indent=2)

    print("Batch complete")
    print(stats)

if __name__ == "__main__":
    run_batch(200)
