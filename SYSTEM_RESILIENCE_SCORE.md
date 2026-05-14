# 🧭 System Resilience Score (SRS)

## 🧩 Purpose

The System Resilience Score (SRS) is a **cross-layer deterministic evaluation metric** within the SPD-R (Supervisory Protocol for Data Resilience) framework.

It provides a unified measure of system resilience by combining:

- 🛰️ Orbital Connectivity Stability (OCRS)
- 📡 Observability Completeness (DHTI)
- 💥 Cascade Propagation Intensity (CPI)

---

## 📊 Core Definition

### Primary Function

SRS = f(OCRS, DHTI, CPI)

---

### Deterministic Form

SRS = OCRS × DHTI × (1 - CPI)

---

## 📡 Input Metrics

### 🛰️ OCRS – Orbital Connectivity Resilience Score
Measures stability of satellite-to-ground or distributed node connectivity under stress.

Range: 0.0 – 1.0

---

### 📡 DHTI – Dependency Health Trace Index
Measures observability completeness and trace reconstruction accuracy across system events.

Range: 0.0 – 1.0

---

### 💥 CPI – Cascade Propagation Index
Measures intensity of failure propagation across system dependency graphs.

Range: 0.0 – 1.0

Interpretation:
- High CPI → strong cascade amplification
- Low CPI → localized or contained failures

---

## ⚙️ Computation Pipeline

### Step 1 — Collect Layer Outputs
From SPD-R subsystem layers:

- OCRS → Orbital simulation layer
- DHTI → Observability layer
- CPI → Cascade engine layer

---

### Step 2 — Normalize Inputs

All values must satisfy:

- OCRS ∈ [0, 1]
- DHTI ∈ [0, 1]
- CPI ∈ [0, 1]

---

### Step 3 — Convert Cascade Instability

Failure pressure is inverted:

Stability Factor = (1 - CPI)

---

### Step 4 — Final Computation

SRS = OCRS × DHTI × (1 - CPI)

---

## 📉 Interpretation Scale

| SRS Range | System State |
|------------|--------------|
| 0.80 – 1.00 | Fully resilient system |
| 0.50 – 0.79 | Moderately stable |
| 0.20 – 0.49 | Degraded resilience |
| 0.00 – 0.19 | Critical instability |

---

## 🧠 System Meaning

- OCRS → network / orbital stability
- DHTI → observability and trace fidelity
- CPI → cascade fragility and propagation strength

---

## ⚠️ System Constraints

- Deterministic under identical inputs
- Sandbox-only simulation metric
- No production or live system coupling
- Fully reproducible across simulation runs

---

## 🔗 Dependency Alignment

SRS is derived from:

- OBSERVABILITY_SIMULATION_ARTIFACT.md → DHTI
- CASCADE_SIMULATION_ARTIFACT.md → CPI
- ORBITAL_SIMULATION_ARTIFACT.md → OCRS

---

End of System Resilience Score Definition
