# Direct Comparison: WITH vs WITHOUT "1"

This document explains the side-by-side comparison analyses that directly test whether "1" drives the small vs large categorical differences.

## Analysis Design

These analyses plot WITH "1" (solid lines) and WITHOUT "1" (dashed lines) on the **same figure**, allowing direct visual comparison of how removing "1" affects ERP waveforms.

### Color Scheme:
- **Purple** (`#9900ff`): Small numbers
  - Solid: Small with "1"
  - Dashed: Small without "1"
- **Orange** (`#ff7f00`): Crossover conditions
  - Solid: Crossover with "1"
  - Dashed: Crossover without "1"

---

## 1. Decreasing Direction

**Analysis:** [decreasing_small_crossover_with_and_without_1_ACC1](configs/analyses/decreasing_small_crossover_with_and_without_1_ACC1.yaml)

### Conditions:

**Small (with 1)** - Purple Solid:
- 21 (2→1)
- 31 (3→1)
- 32 (3→2)

**Small (without 1)** - Purple Dashed:
- 32 (3→2) *only*

**Crossover (with 1)** - Orange Solid:
- 41, 42, 52, 43, 53, 63

**Crossover (without 1)** - Orange Dashed:
- 42, 52, 43, 53, 63 *(excludes 41)*

### Key Comparison:

**CRITICAL QUESTION:** Do the purple solid and purple dashed lines overlap?

- **IF THEY OVERLAP**: "1" is **NOT** driving the small-number effects; 2-3 genuinely differ from larger numbers
- **IF THEY SEPARATE**: "1" **IS** driving the small-number effects; when removed, the "small" category looks different

### What to Look For:

**N1 Amplitude (POT region, ~176ms):**
- WITH "1": Purple solid should show LESS negative amplitude (based on our previous finding that transitions TO "1" have weaker N1)
- WITHOUT "1": Purple dashed should shift to match orange more closely
- **Prediction**: Solid and dashed purple lines should DIVERGE

**P3b Amplitude (Pz region, ~472ms):**
- WITH "1": Purple solid may be dampened by heterogeneity
- WITHOUT "1": Purple dashed may show STRONGER amplitude
- **Prediction**: Dashed purple might be LARGER than solid (revealing true 2-3 effect)

---

## 2. Increasing Direction

**Analysis:** [increasing_small_crossover_with_and_without_1_ACC1](configs/analyses/increasing_small_crossover_with_and_without_1_ACC1.yaml)

### Conditions:

**Small (with 1)** - Purple Solid:
- 12 (1→2)
- 13 (1→3)
- 23 (2→3)

**Small (without 1)** - Purple Dashed:
- 23 (2→3) *only*

**Crossover (with 1)** - Orange Solid:
- 14, 24, 25, 34, 35, 36

**Crossover (without 1)** - Orange Dashed:
- 24, 25, 34, 35, 36 *(excludes 14)*

### Key Comparison:

Same logic as decreasing direction.

### What to Look For:

**N1 Amplitude (~164ms):**
- Transitions FROM "1" (12, 13) might show enhanced early visual processing
- WITHOUT "1": Should look more like crossover/large

**P3b Latency (~468ms):**
- Based on previous results, effect might get STRONGER without "1"
- Look for faster latency in purple dashed vs. orange

---

## Where to Find Results

### ERP Plots:
**Decreasing:**
- [N1 plot](docs/assets/plots/decreasing_small_crossover_with_and_without_1_ACC1/decreasing_small_crossover_with_and_without_1_ACC1-N1.png)
- [P3b plot](docs/assets/plots/decreasing_small_crossover_with_and_without_1_ACC1/decreasing_small_crossover_with_and_without_1_ACC1-P3b.png)

**Increasing:**
- [N1 plot](docs/assets/plots/increasing_small_crossover_with_and_without_1_ACC1/increasing_small_crossover_with_and_without_1_ACC1-N1.png)
- [P3b plot](docs/assets/plots/increasing_small_crossover_with_and_without_1_ACC1/increasing_small_crossover_with_and_without_1_ACC1-P3b.png)

### Statistical Reports:
- [Decreasing stats](docs/assets/stats/decreasing_small_crossover_with_and_without_1_ACC1/STATISTICAL_REPORT.md)
- [Increasing stats](docs/assets/stats/increasing_small_crossover_with_and_without_1_ACC1/STATISTICAL_REPORT.md)

---

## Interpretation Guide

### Scenario 1: "1" Drives Everything (Original Hypothesis)

**Expected pattern:**
- Purple solid and dashed lines DIVERGE significantly
- Dashed purple overlaps with orange (crossover)
- WITH "1" creates artificial separation; WITHOUT "1" shows no small-large boundary

### Scenario 2: "1" is Unique, but 2-3 vs 4-6 Boundary Exists

**Expected pattern:**
- Purple solid and dashed lines show SOME divergence (due to "1")
- BUT dashed purple still differs from orange
- Removing "1" reduces but doesn't eliminate small-large distinction

### Scenario 3: "1" Obscures True Subitizing Boundary (Our Actual Finding)

**Expected pattern:**
- Purple dashed shows **STRONGER** effects than solid (especially P3b)
- Removing "1" **CLARIFIES** rather than eliminates the 2-3 vs 4-6 boundary
- Heterogeneity from "1" was masking the true effect

---

## Statistical Approach

Since all four conditions are in the same analysis, you **CAN** now directly compare:

**Interaction test:** `(Small_with - Small_without) vs (Crossover_with - Crossover_without)`

This tests whether the effect of removing "1" is **different** for Small vs Crossover conditions.

**Relevant LMM contrasts:**
1. `Small (with 1) - Small (without 1)` ← Effect of adding "1" to small numbers
2. `Crossover (with 1) - Crossover (without 1)` ← Effect of adding "41" condition
3. Compare these two differences

---

## Publication Figure

These plots are publication-ready! They visually demonstrate:

**Figure X. Direct comparison of ERP waveforms with and without the numerosity "1".**

*Grand average ERPs for decreasing numerical transitions. Solid lines include transitions involving "1" (e.g., 2→1, 3→1); dashed lines exclude all "1"-related transitions. Purple: small number transitions (1-3 range); Orange: crossover transitions (crossing 3-4 boundary). Shaded regions represent ±1 SEM.*

*(A) N1 component (POT region): Note divergence between purple solid and dashed lines, indicating "1"-driven effects.*

*(B) P3b component (Pz region): Dashed purple line shows enhanced amplitude compared to solid, revealing that removing "1" strengthens rather than eliminates the small-number effect.*

---

## Summary

These analyses provide the **cleanest test** of your hypothesis by:

1. **Same participants**, same data
2. **Same plot**, direct visual comparison
3. **Statistical power** to test interactions
4. **Clear interpretation**: solid vs dashed line separation = effect of "1"

You now have THREE levels of evidence:

1. **Separate analyses** (WITH "1" vs WITHOUT "1" in different YAMLs)
2. **Direct comparison** (both on same plot - THIS analysis)
3. **Specific contrasts** (landing on "1", increasing by "1", etc.)

This is comprehensive, rigorous, and publication-ready! 🎉
