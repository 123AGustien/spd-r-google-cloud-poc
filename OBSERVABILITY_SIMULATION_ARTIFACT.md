# 📡 Observability Layer – Measurable Simulation Artifact

## Purpose
This document defines the single measurable output produced by the Observability layer (SPD-R) of the Sextant Protocol ecosystem.

It formalises deterministic system visibility, trace completeness, and dependency observability in sandbox simulation environments.

---

## 🧪 Simulation Artifact Definition

### 📊 Dependency Health Trace Index (DHTI)

The Observability Layer produces a deterministic scalar metric:

\[
DHTI = \frac{T_{complete} \times S_{resolution} \times R_{consistency}}{N_{events} + \varepsilon}
\]

---

## 📡 Variable Definitions

- **T_complete** = proportion of system events fully traced end-to-end  
- **S_resolution** = granularity of dependency state visibility  
- **R_consistency** = repeatability score across identical simulations  
- **N_events** = total number of system events processed (raw count before normalization)  
- **ε** = numerical stability constant  

---

## 📏 Normalisation Rules

All input variables are normalised to the range **[0,1]** prior to computation:

- T_complete ∈ [0,1]  
- S_resolution ∈ [0,1]  
- R_consistency ∈ [0,1]  

Event scaling is applied as:

\[
N_{events} = \log(1 + \text{raw\_event\_count})
\]

This ensures logarithmic scaling and prevents system distortion under high event load.

---

## ⚙️ Stability Constant

\[
\varepsilon = 1 \times 10^{-6}
\]

Purpose:
- Prevent division instability
- Maintain deterministic output under edge-case conditions

---

## ⚙️ Simulation Outputs

The Observability layer produces:

- DHTI (primary visibility score)
- Event trace completeness map
- Dependency state graph snapshot
- Anomaly detection distribution
- Temporal event reconstruction accuracy curve

---

## 📉 Interpretation Scale

- **0.80 – 1.00** → fully observable system (high trace clarity)  
- **0.50 – 0.79** → partial observability gaps  
- **0.20 – 0.49** → fragmented dependency visibility  
- **0.00 – 0.19** → low system traceability / opaque system state  

---

## 🧠 System Role

DHTI is a synthetic observability metric used only for:

- simulation-based system analysis  
- dependency graph evaluation  
- resilience research in sandbox environments  

It does **not** represent real-world monitoring or production telemetry.

---

## 🔁 Behaviour Model

The observability engine operates through the following deterministic pipeline:

1. Event ingestion into trace system  
2. Dependency mapping reconstruction  
3. State snapshot generation  
4. Cross-run consistency validation  
5. Trace completeness scoring  

All outputs are fully reproducible under identical inputs.

---

## 🔗 Cross-Layer Dependency Mapping

DHTI integrates into the system-wide resilience model:

- Orbital Layer input → connectivity degradation signals (OCRS)
- Cascade Layer input → failure propagation visibility feedback (FPC)
- Observability Layer output → DHTI (system visibility score)

### Final System Equation:

\[
SRS = f(OCRS, FPC, DHTI)
\]

Where:
- OCRS = Orbital Connectivity Resilience Score  
- FPC = Failure Propagation Coefficient  
- DHTI = Dependency Health Trace Index  

---

## ⚠️ Constraints

- Simulation-only observability model  
- No production monitoring authority  
- No external system control  
- Sandbox execution environment only  

---

## 📌 Design Principles

- Deterministic trace reconstruction  
- Full dependency transparency  
- Cross-run reproducibility  
- Cascade-aware observability alignment  
- Cross-layer metric integration  

---

End of Observability Simulation Artifact
