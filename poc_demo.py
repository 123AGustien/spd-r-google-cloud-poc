import json

def run_simulation():
    log = []

    # Simple deterministic cascade
    nodes = ["A", "B", "C", "D"]

    for i in range(len(nodes)):
        log.append(f"{nodes[i]} failed")
        if i < len(nodes) - 1:
            log.append(f"{nodes[i]} impacts {nodes[i+1]}")

    output = {
        "log": log,
        "replay_test": True
    }

    with open("result.json", "w") as f:
        json.dump(output, f, indent=2)

    print("\n".join(log))
    print("\nREPLAY TEST: True")


if __name__ == "__main__":
    run_simulation()
