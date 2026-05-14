# 🌐 Global System Graph (Sextant Ecosystem)

## 1. Purpose

Defines the unified deterministic dependency graph across all Sextant Protocol repositories and their cross-layer interactions.

All system components are treated as nodes in a single reproducible simulation graph enabling cross-domain resilience modelling.

---

## 2. System Nodes (Repositories)

| Node | Repository | Layer |
|------|------------|------|
| CORE | Sextant-Protocol | Cascade Engine |
| OBS | spd-r-google-cloud-poc | Observability Layer |
| ORB | sextant-orbital-resilience-framework | Orbital Simulation Layer |
| EXT | Sextant-protocol- | Execution / Grid Simulation Layer |

---

## 3. Cross-Layer Flow Model

The system operates under a deterministic transformation pipeline:

OCRS → DHTI → CPI → SRS

Where:

- OCRS = Orbital Connectivity Resilience Score  
- DHTI = Dependency Health Trace Index  
- CPI = Cascade Propagation Index  
- SRS = System Resilience Score (final fused output)

---

## 4. Dependency Graph Model

Each repository is represented as a deterministic node in a directed acyclic graph (DAG).

### 4.1 Node Properties
- State value normalized in range: [0, 1]
- Deterministic output per simulation run
- Stateless between runs unless explicitly re-initialized
- Fully sandbox constrained

### 4.2 Edge Properties
- Weighted dependency influence
- Directional propagation of state changes
- Cascade-enabled transitions
- No circular dependency activation in baseline mode

---

## 5. Global State Equation

The system-wide resilience function is defined as:

SRS = f(OCRS, DHTI, CPI)

Expanded deterministic fusion form:

SRS = OCRS × DHTI × (1 − CPI)

---

## 6. Layer Interaction Rules

1. Orbital Layer generates infrastructure stability signal → OCRS  
2. Observability Layer computes trace completeness → DHTI  
3. Cascade Layer computes failure propagation pressure → CPI  
4. Fusion Layer computes final system resilience state → SRS  

---

## 7. System Constraints

- Fully sandboxed simulation environment only  
- No production or live system coupling  
- Deterministic replay required for all executions  
- Identical inputs must produce identical outputs  
- No external runtime mutation of system graph  

---

## 8. Design Principles

- Deterministic graph execution  
- Cross-layer observability alignment  
- Explicit dependency transparency  
- Reproducible simulation outcomes  
- Modular separation of all system layers  

---

## 9. System Interpretation

This graph represents a **multi-repository deterministic resilience simulation topology**, not an operational infrastructure system.

It is designed for:
- dependency research
- cascade modelling
- observability evaluation
- orbital-to-ground resilience simulation

---

## End of Global System Graph Definition
