# 🧭 Cross-Layer Fusion Model (SPD-R)

## Purpose
Defines deterministic interaction rules between Orbital, Observability, and Cascade layers.

## System Flow

OCRS → DHTI → CPI → SRS

## Rules
1. Each layer output is immutable per simulation run
2. All values must be normalized [0,1]
3. Cascade output influences system stability inversion
4. Observability governs confidence weighting

## Final Output Chain

SRS = OCRS × DHTI × (1 - CPI)

## Constraint
All computations must remain deterministic and sandboxed.
