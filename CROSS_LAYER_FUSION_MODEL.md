# 🧭 Cross-Layer Fusion Model (SPD-R)

## 🧭 Purpose

This document defines the deterministic fusion logic between the three core system layers:

- 🛰️ Orbital Layer → OCRS (Orbital Connectivity Resilience Score)
- 📡 Observability Layer → DHTI (Dependency Health Trace Index)
- 💥 Cascade Layer → CPI (Cascade Propagation Index)

It produces a unified system-level metric:

# 🧮 System Resilience Score (SRS)

---

## 🔁 System Flow

OCRS → DHTI → CPI → SRS

Each layer contributes independently to the final system state evaluation.

---

## 📊 Input Metrics

### 🛰️ OCRS (Orbital Connectivity Resilience Score)
Measures stability of orbital-to-ground connectivity.

Range: **0.0 – 1.0**

---

### 📡 DHTI (Dependency Health Trace Index)
Measures observability, trace completeness, and dependency visibility.

Range: **0.0 – 1.0**

---

### 💥 CPI (Cascade Propagation Index)
Measures system fragility and failure propagation intensity.

Range: **0.0 – 1.0**

---

## ⚙️ Normalization Rules

All inputs MUST satisfy:

- OCRS ∈ [0, 1]
- DHTI ∈ [0, 1]
- CPI ∈ [0, 1]

Any out-of-range values must be clamped before computation.

---

## 🧮 Fusion Equation

### Final System Resilience Score (SRS)

SRS = OCRS × DHTI × (1 - CPI)

---

## 🔍 Interpretation Logic

- OCRS → structural connectivity strength
- DHTI → system observability confidence
- CPI → instability / cascade amplification factor (inverse effect)

The term **(1 - CPI)** represents system stability retention under cascade pressure.

---

## 📉 SRS Classification Bands

| SRS Range | System State |
|----------|--------------|
| 0.80 – 1.00 | Highly resilient system |
| 0.50 – 0.79 | Stable system |
| 0.20 – 0.49 | Fragile system |
| 0.00 – 0.19 | Critical instability |

---

## 🔄 Computation Pipeline

1. Acquire OCRS from Orbital Layer
2. Acquire DHTI from Observability Layer
3. Acquire CPI from Cascade Layer
4. Normalize all inputs to [0,1]
5. Compute SRS
6. Classify system state

---

## 🧠 Design Principles

- Deterministic execution (same inputs → same outputs)
- Fully sandboxed evaluation model
- No hidden weighting or external bias factors
- Layer independence preserved
- Cross-layer compatibility enforced

---

## ⚠️ Constraints

- Simulation-only model
- No operational control capability
- No real-world system integration
- No external dependency execution

---

## 📌 Output

Primary system-level metric:

SRS → System Resilience Score

This represents the unified resilience state of the entire SPD-R system stack.

---

End of Cross-Layer Fusion Model
