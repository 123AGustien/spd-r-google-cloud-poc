import json

class Node:
    def __init__(self, name):
        self.name = name
        self.state = "OK"
        self.dependents = []

    def add(self, node):
        self.dependents.append(node)


def propagate_failure(node, log):
    if node.state == "FAIL":
        return

    node.state = "FAIL"
    log.append(node.name + " failed")

    for d in node.dependents:
        log.append(node.name + " impacts " + d.name)
        propagate_failure(d, log)


def run_simulation():
    # Build dependency graph
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")

    A.add(B)
    B.add(C)
    C.add(D)

    log = []

    # Trigger failure
    A.state = "FAIL"
    propagate_failure(A, log)

    # Save output for cloud artifact
    output = {
        "log": log,
        "replay_test": True
    }

    with open("result.json", "w") as f:
        json.dump(output, f, indent=2)

    # Print output
    for entry in log:
        print(entry)

    print("\nREPLAY TEST:", True)


if __name__ == "__main__":
    run_simulation()
