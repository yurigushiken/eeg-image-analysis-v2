# Small vs Large vs Crossover Analysis Guide

## Testing the Hypothesis: "1" Drives Small-Large Differences

This guide explains how to replicate your original study design and test whether the number "1" is responsible for the observed categorical differences between small (1-3) and large (4-6) numerosities.

---

## Background from Original Study

Your original poster showed:
- **Small-to-Small (SS)**: 1→2, 1→3, 2→1, 2→3, 3→1, 3→2
- **Large-to-Large (LL)**: 4→5, 4→6, 5→4, 5→6, 6→4, 6→5
- **Crossovers (SL/LS)**: 3→4, 4→3, etc.

**Key findings:**
- Decreasing Small-Small had **stronger P3b** than Large-Large
- Categorical break between small and large numbers
- N1 scaled with magnitude in small (1-3) but not large (4-6) range

## New Hypothesis

**If "1" is removed, the small-large categorical distinction will disappear or be greatly reduced.**

This would suggest that "1" (as a unique singular quantity) drives the apparent categorical boundary, rather than a genuine subitizing/ANS distinction between 1-3 vs 4-6.

---

## Analysis Design

### WITH "1" (Replicating Original Design)

#### Increasing Direction:
- **Small**: 12, 13, 23
- **Crossover**: 14, 24, 25, 34, 35, 36
- **Large**: 45, 46, 56

#### Decreasing Direction:
- **Small**: 21, 31, 32
- **Crossover**: 41, 42, 52, 43, 53, 63
- **Large**: 54, 64, 65

### WITHOUT "1" (Testing Hypothesis)

#### Increasing Direction:
- **Small**: 23 (only one condition!)
- **Crossover**: 24, 25, 34, 35, 36
- **Large**: 45, 46, 56

#### Decreasing Direction:
- **Small**: 32 (only one condition!)
- **Crossover**: 42, 52, 43, 53, 63
- **Large**: 54, 64, 65

---

## Running the Analyses

### Option 1: Run Everything (Recommended for Publication)

```bash
# Step 1: Run all ERP analyses (takes ~10-20 minutes per analysis)
bash run_small_large_crossover_analyses.sh

# Step 2: Run all statistics
bash run_small_large_crossover_stats.sh
```

### Option 2: Run Individual Analyses

#### PART A: Main ERP Analyses

**With "1" - Increasing:**
```bash
python scripts/run_analysis.py --config configs/analyses/increasing_large_vs_small_vs_crossover.yaml
python scripts/run_analysis.py --config configs/analyses/increasing_large_vs_small_vs_crossover_ACC1.yaml
```

**With "1" - Decreasing:**
```bash
python scripts/run_analysis.py --config configs/analyses/decreasing_large_vs_small_vs_crossover.yaml
python scripts/run_analysis.py --config configs/analyses/decreasing_large_vs_small_vs_crossover_ACC1.yaml
```

**Without "1" - Increasing:**
```bash
python scripts/run_analysis.py --config configs/analyses/increasing_large_vs_small_vs_crossover_without_1.yaml
python scripts/run_analysis.py --config configs/analyses/increasing_large_vs_small_vs_crossover_without_1_ACC1.yaml
```

**Without "1" - Decreasing:**
```bash
python scripts/run_analysis.py --config configs/analyses/decreasing_large_vs_small_vs_crossover_without_1.yaml
python scripts/run_analysis.py --config configs/analyses/decreasing_large_vs_small_vs_crossover_without_1_ACC1.yaml
```

#### PART B: Statistical Analyses

First, create the stats config files:
```bash
python scripts/create_stat_configs.py
```

Then run statistics for each analysis:

**With "1":**
```bash
python scripts/run_statistics.py --config configs/statistics/increasing_large_vs_small_vs_crossover.yaml
python scripts/run_statistics.py --config configs/statistics/increasing_large_vs_small_vs_crossover_ACC1.yaml
python scripts/run_statistics.py --config configs/statistics/decreasing_large_vs_small_vs_crossover.yaml
python scripts/run_statistics.py --config configs/statistics/decreasing_large_vs_small_vs_crossover_ACC1.yaml
```

**Without "1":**
```bash
python scripts/run_statistics.py --config configs/statistics/increasing_large_vs_small_vs_crossover_without_1.yaml
python scripts/run_statistics.py --config configs/statistics/increasing_large_vs_small_vs_crossover_without_1_ACC1.yaml
python scripts/run_statistics.py --config configs/statistics/decreasing_large_vs_small_vs_crossover_without_1.yaml
python scripts/run_statistics.py --config configs/statistics/decreasing_large_vs_small_vs_crossover_without_1_ACC1.yaml
```

---

## Where to Find Results

### ERP Plots
- `docs/assets/plots/<analysis_name>/`
  - `<analysis_name>-P1.png`
  - `<analysis_name>-N1.png`
  - `<analysis_name>-P3b.png`

### Statistical Reports
- `docs/assets/stats/<analysis_name>/STATISTICAL_REPORT.md`
- `docs/assets/stats/<analysis_name>/plots/` (boxplots, violin plots)

### Subject-Level Data
- `docs/assets/tables/<analysis_name>/subject_measurements.csv`

---

## Critical Comparisons for Your Hypothesis

### 1. P3b Amplitude - Main Effect of Condition

**WITH "1" (Expected):**
- Significant main effect: Small > Crossover > Large
- Strong pairwise differences

**WITHOUT "1" (If hypothesis is true):**
- **Non-significant** or **greatly reduced** main effect
- **No clear Small > Large pattern**

### 2. N1 Amplitude - Scaling with Magnitude

**WITH "1" (Expected):**
- N1 scales with magnitude in Small range
- Flat in Large range

**WITHOUT "1" (If hypothesis is true):**
- **Loss of magnitude scaling**
- Similar N1 for all conditions

### 3. P3b Latency - Speed of Processing

**WITH "1" (Expected):**
- Faster for Small than Large

**WITHOUT "1" (If hypothesis is true):**
- **No latency differences**

---

## Statistical Predictions

### Hypothesis Supported If:

1. **WITH "1"**: Significant ANOVA main effect for Small vs Large
   **WITHOUT "1"**: **Non-significant** ANOVA

2. **WITH "1"**: Significant pairwise: Small > Large (p < .05)
   **WITHOUT "1"**: **Non-significant** pairwise (p > .05)

3. **WITH "1"**: Large effect size (η²_G > 0.14)
   **WITHOUT "1"**: **Small effect size** (η²_G < 0.06)

---

## Example Results Structure for Paper

```
Results

Experiment 1: Replication of Original Small-Large Categorization (WITH "1")
  - P3b amplitude: Significant main effect (F(2,46) = X.XX, p < .001, η²_G = 0.XX)
  - Pairwise: Small > Crossover (p = .XXX); Small > Large (p < .001)

Experiment 2: Testing the "1" Hypothesis (WITHOUT "1")
  - P3b amplitude: **Non-significant** main effect (F(2,46) = X.XX, p = .XXX, η²_G = 0.XX)
  - Pairwise: Small vs Large (p = .XXX, n.s.)

Discussion
  These findings demonstrate that the number "1" drives the apparent categorical
  distinction between small (1-3) and large (4-6) numerosities. When "1" is removed,
  the small-large boundary disappears, suggesting that singular quantities engage
  qualitatively different cognitive mechanisms rather than reflecting a genuine
  subitizing vs ANS boundary.
```

---

## Files Created

### Analysis Configurations
1. `configs/analyses/increasing_large_vs_small_vs_crossover.yaml`
2. `configs/analyses/increasing_large_vs_small_vs_crossover_ACC1.yaml`
3. `configs/analyses/decreasing_large_vs_small_vs_crossover.yaml`
4. `configs/analyses/decreasing_large_vs_small_vs_crossover_ACC1.yaml`
5. `configs/analyses/increasing_large_vs_small_vs_crossover_without_1.yaml`
6. `configs/analyses/increasing_large_vs_small_vs_crossover_without_1_ACC1.yaml`
7. `configs/analyses/decreasing_large_vs_small_vs_crossover_without_1.yaml`
8. `configs/analyses/decreasing_large_vs_small_vs_crossover_without_1_ACC1.yaml`

### Execution Scripts
- `run_small_large_crossover_analyses.sh` (runs all ERP analyses)
- `run_small_large_crossover_stats.sh` (runs all statistics)

---

## Timeline Estimate

- **ERP Analyses**: ~10 minutes each × 8 = 80 minutes
- **Statistical Analyses**: ~2 minutes each × 8 = 16 minutes
- **Total**: ~90-100 minutes

---

## Good Luck!

This is a really elegant experimental design to test your hypothesis. The prediction is clear: if "1" is driving the small-large categorical distinction, then removing it should eliminate or greatly reduce the effect.

**Key advantage**: You're using the SAME participants, SAME paradigm, just excluding specific conditions. This is a very clean within-study manipulation.

Feel free to ask if you need help interpreting results or writing up the findings!
