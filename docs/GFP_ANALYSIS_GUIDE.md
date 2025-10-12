# Global Field Power (GFP) Analysis Guide

## Understanding Your New ERP Analysis Pipeline

This guide explains the **scientifically rigorous** approach now implemented in your ERP analysis pipeline, based on Global Field Power (GFP) with Full Width at Half Maximum (FWHM) windowing.

---

## Table of Contents

1. [What Changed and Why](#what-changed-and-why)
2. [The Scientific Problem We Solved](#the-scientific-problem-we-solved)
3. [How the GFP Approach Works](#how-the-gfp-approach-works)
4. [Interpreting Your Results](#interpreting-your-results)
5. [Configuring Your Analyses](#configuring-your-analyses)
6. [Writing This Up for Publication](#writing-this-up-for-publication)
7. [Troubleshooting](#troubleshooting)

---

## What Changed and Why

### The Old Approach (REMOVED)

❌ **ROI-based peak detection** - Selected channels based on prior electrode choices
❌ **Per-condition peak finding** - Found peaks separately for each experimental condition
❌ **Fixed ±20ms windows** - Arbitrary window width regardless of component characteristics
❌ **Fallback mechanisms** - Used window center if peak detection failed (hiding problems)

### The New Approach (IMPLEMENTED)

✅ **Global Field Power (GFP)** - Uses ALL channels simultaneously
✅ **Collapsed localizer** - Averages ALL conditions together before peak detection
✅ **FWHM windows** - Data-driven window widths adapted to each component
✅ **No fallbacks** - Raises errors if components can't be detected (transparency)

---

## The Scientific Problem We Solved

### Circular Analysis (Double-Dipping)

**The Problem:**
When you use the same data to both:
1. **Select** your analysis time window (by finding where the difference is largest)
2. **Test** for statistical differences in that window

...you inflate your false positive rate. This is called "circular analysis" or "double-dipping."

**Example of Bad Practice:**
```
1. Look at Condition A vs Condition B
2. Find the peak difference occurs at 180ms
3. Test if there's a significant difference at 180ms
4. Report p < 0.05
```

**Why This is Wrong:**
You **guaranteed** you'd find the largest difference at 180ms because that's how you selected 180ms! Your statistical test is no longer valid.

### The Collapsed Localizer Solution

**Our Approach:**
```
1. Average Condition A + Condition B together (collapsed localizer)
2. Find where the COMBINED signal peaks (using GFP)
3. Use this peak to define your time window
4. NOW test Condition A vs Condition B in this window
```

**Why This Works:**
The window selection is now **independent** from the condition comparison. The peak was found in the average of both conditions, not in the difference between them.

---

## How the GFP Approach Works

### Step 1: Collapsed Localizer

**Code:** All condition sets are averaged together
```python
all_evokeds = []
for condition_set in ['Increasing', 'Decreasing', 'NoChange']:
    all_evokeds.extend(subjects_in_that_condition)

grand_average = combine_evoked(all_evokeds, weights='equal')
```

**Scientific Rationale:**
This creates an **unbiased** waveform that shows general brain activity common to your experimental paradigm, independent of any specific condition effects.

### Step 2: Global Field Power (GFP)

**Mathematical Definition:**
```
GFP(t) = std(all_channels, t)
```

At each timepoint t, GFP is the **standard deviation across ALL channels**.

**What GFP Represents:**
- **High GFP** = Strong spatial topography (big voltage differences across scalp)
- **Low GFP** = Weak/flat topography (similar voltages everywhere)
- **GFP Peak** = Moment of maximal brain activity (strongest field configuration)

**Why GFP is Better Than ROI Averaging:**
- ✅ Uses all channels, not hand-picked electrodes
- ✅ Reference-independent (works regardless of EEG reference)
- ✅ Objective (no researcher bias in channel selection)
- ✅ Reflects true field strength

### Step 3: A Priori Search Range

**Configuration:** In `configs/components.yaml`:
```yaml
P1:
  window_ms: [60, 120]   # Search for P1 between 60-120ms
N1:
  window_ms: [125, 200]  # Search for N1 between 125-200ms
P3b:
  window_ms: [320, 420]  # Search for P3b between 320-420ms
```

**Scientific Rationale:**
These ranges come from **prior literature** (Luck & Kappenman, 2012; etc.). We only search within scientifically justified windows, preventing data snooping while remaining objective.

**Peak Detection:**
```python
# Find the time point with maximum GFP within the search range
peak_latency = time_of_max_GFP_within_range(gfp, search_range)
```

### Step 4: FWHM Window Calculation

**Definition:**
Full Width at Half Maximum = the width of the GFP peak at 50% of its maximum height.

**Calculation:**
```python
1. Find peak_height (maximum GFP value)
2. Calculate half_max = peak_height / 2
3. Find where GFP crosses half_max on left side → window_start
4. Find where GFP crosses half_max on right side → window_end
5. FWHM = window_end - window_start
```

**Why FWHM is Brilliant:**
- ✅ **Adaptive**: Sharp components get narrow windows, broad components get wide windows
- ✅ **Data-driven**: The component itself determines the window width
- ✅ **Objective**: No arbitrary ±20ms or ±50ms choices
- ✅ **Mathematically principled**: Based on signal processing theory

**Example Results:**
- P1: FWHM = 27ms (sharp, transient component)
- N1: FWHM = 60ms (broader component)
- P3b: FWHM = 80-120ms typically (very broad, sustained component)

---

## Interpreting Your Results

### Reading the Collapsed Localizer Plot

![Example Plot](assets/plots/small_increasing_vs_decreasing/small_increasing_vs_decreasing-collapsed_localizer.png)

**Key Elements:**

1. **Blue Line** = GFP trace (standard deviation across all channels)
2. **Red Dashed Line** = Detected peak latency
3. **Pink Shaded Region** = FWHM window (where you'll measure amplitudes)
4. **Dotted Vertical Lines** = A priori search range boundaries
5. **Gray Line at 0ms** = Stimulus onset

**What to Check:**

✅ **Peak is well-defined** - GFP should show a clear peak, not flat/noisy
✅ **Peak is within search range** - Should be between the dotted lines
✅ **FWHM makes sense** - Window width should match component characteristics
✅ **GFP magnitude is reasonable** - Should be >0.5µV typically (not near zero)

### Understanding the Metrics Box

In the top-right corner of each subplot:

```
Peak GFP: 2.00 µV       ← Maximum GFP value at peak
FWHM: 60.0 ms           ← Width of component at half maximum
Window: [148.9, 208.9] ms  ← Exact analysis window boundaries
```

**What These Numbers Mean:**

- **Peak GFP**: Strength of the scalp electric field (higher = stronger component)
- **FWHM**: Duration of the component (narrower = more transient, broader = more sustained)
- **Window**: The exact time range you'll use for amplitude measurements in condition comparisons

---

## Configuring Your Analyses

### Analysis YAML Files

Located in `configs/analyses/`, e.g., `small_increasing_vs_decreasing.yaml`:

```yaml
components: ["P1", "N1"]  # Which components to analyze

# A priori search ranges are defined in configs/components.yaml
# FWHM windows are computed automatically from the data
```

**Key Decision:** Which components to include?

✅ **Include** if: Component is expected in your paradigm
❌ **Exclude** if: Component not relevant OR peaks at epoch edge

### Components Configuration

File: `configs/components.yaml`

```yaml
P1:
  window_ms: [60, 120]    # Early visual component

N1:
  window_ms: [125, 200]   # Face-sensitive negativity

P3b:
  window_ms: [320, 420]   # Context updating / decision-making
```

**How to Set These Ranges:**

1. **Review literature** for your paradigm type (visual, auditory, cognitive, etc.)
2. **Look at prior studies** using similar stimuli
3. **Consult textbooks** (Luck, 2014; Luck & Kappenman, 2012)
4. **Be conservative** - use ranges that are well-established

**Do NOT:**
- ❌ Look at your own data first, then set ranges
- ❌ Make ranges very narrow to "force" a peak
- ❌ Adjust ranges to get "better" results

**Acceptable Adjustments:**
- ✅ Narrowing range if component consistently peaks early/late
- ✅ Shortening range to avoid epoch edges
- ✅ Citing literature justification for any changes

---

## Writing This Up for Publication

### Methods Section Template

```markdown
**ERP Component Analysis**

Component peaks and analysis windows were determined using a collapsed
localizer approach to prevent circular analysis (Luck & Gaspelin, 2017).
For each component of interest (P1, N1), we computed the grand average
ERP collapsed across all experimental conditions and subjects.

We calculated the Global Field Power (GFP; Lehmann & Skrandies, 1980)
as the standard deviation of voltage across all channels at each timepoint.
GFP provides a reference-independent measure of overall scalp electric
field strength. Component peaks were identified as the latency of maximum
GFP within literature-based a priori search ranges (P1: 60-120ms, N1: 125-200ms).

Analysis time windows were defined using the Full Width at Half Maximum
(FWHM) of each component's GFP peak. This data-driven approach adapts
window width to the actual duration of each component in our data (P1 FWHM:
27ms, N1 FWHM: 60ms). Mean amplitudes within these windows were extracted
for statistical comparison between conditions.

This procedure ensures that time window selection is independent from
condition-specific effects, preventing inflated false positive rates
(Kriegeskorte et al., 2009).
```

### Key References to Cite

**GFP Method:**
- Lehmann, D., & Skrandies, W. (1980). Reference-free identification of components of checkerboard-evoked multichannel potential fields. *Electroencephalography and Clinical Neurophysiology*, 48(6), 609-621.

**Circular Analysis:**
- Kriegeskorte, N., Simmons, W. K., Bellgowan, P. S., & Baker, C. I. (2009). Circular analysis in systems neuroscience: the dangers of double dipping. *Nature Neuroscience*, 12(5), 535-540.

**ERP Best Practices:**
- Luck, S. J., & Gaspelin, N. (2017). How to get statistically significant effects in any ERP experiment (and why you shouldn't). *Psychophysiology*, 54(1), 146-157.

**ERP Analysis Textbook:**
- Luck, S. J. (2014). *An introduction to the event-related potential technique* (2nd ed.). MIT Press.

### Results Section Template

```markdown
**Component Characteristics**

The collapsed localizer analysis revealed clear P1 and N1 components in
the grand average ERP. The P1 component peaked at 108ms (FWHM: 94-121ms,
width: 27ms), consistent with early visual processing. The N1 component
peaked at 172ms (FWHM: 149-209ms, width: 60ms), consistent with face-
selective processing in the visual stream.

[INSERT YOUR COLLAPSED LOCALIZER FIGURE HERE]

*Figure X*: Collapsed localizer results showing Global Field Power (GFP)
for P1 and N1 components. The GFP trace (blue) represents the standard
deviation across all 128 channels. Red dashed lines indicate detected
peaks, pink shaded regions show FWHM analysis windows, and dotted vertical
lines mark a priori search ranges based on prior literature.
```

---

## Troubleshooting

### Error: "Cannot compute FWHM: peak too close to data edge"

**What This Means:**
Your component peaks at the very beginning or end of your epoch, leaving insufficient samples to calculate FWHM.

**Example:**
```
ERROR: Cannot compute FWHM: GFP peak at 450.0 ms is too close to epoch edge.
Epoch spans [-100.0, 496.0] ms. Need at least 5 samples (~20 ms) on each side.
```

**Solutions:**

1. **Extend your epochs** (RECOMMENDED for future data collection)
   - If P3b peaks at 450ms and epoch ends at 496ms, extend to ~550ms
   - Re-preprocess your data with longer epochs

2. **Narrow the search range** (if component forms earlier)
   - If P3b consistently peaks late, try search range [300, 420]ms instead of [300, 496]ms
   - Update `configs/components.yaml`

3. **Exclude the component** (if not critical for your research question)
   - Remove it from your analysis YAML: `components: ["P1", "N1"]`
   - Document why in your methods section

**Important:** This error is **catching a real problem**. Don't try to "work around" it—address the underlying issue!

### Error: "No meaningful GFP peak found"

**What This Means:**
The GFP in your search range is less than 10% of the maximum GFP in the entire epoch.

**Example:**
```
ERROR: No meaningful GFP peak found in search range [125, 200] ms.
Peak GFP (0.3) is less than 10% of global maximum (5.2).
```

**Possible Causes:**

1. **Component not present** in your paradigm
   - Not all paradigms elicit all components
   - E.g., P3b requires an oddball/decision task

2. **Wrong search range** for your paradigm
   - Your N1 might be earlier/later than typical
   - Check prior studies using similar stimuli

3. **Data quality issues**
   - Poor preprocessing (artifacts, filtering issues)
   - Insufficient subjects (need adequate SNR)

**Solutions:**

1. **Review your paradigm** - Is this component expected?
2. **Check preprocessing** - Are epochs clean? Is filtering appropriate?
3. **Examine data quality** - Plot individual subjects' ERPs to verify component presence
4. **Consult literature** - What are typical latencies for your stimulus type?

### Warning: "some peaks have a prominence of 0" or "width of 0"

**What This Means:**
Scipy's peak detection found a very sharp/spiky peak. This is usually fine—GFP peaks can be narrow.

**Action:**
✅ No action needed if analysis completes successfully
⚠️ If you see this AND get FWHM errors, your data may have artifacts

---

## Command Quick Reference

### Run Single Analysis
```bash
python scripts/run_analysis.py --config configs/analyses/small_increasing_vs_decreasing.yaml
```

### Run All Analyses
```bash
python scripts/run_all_analyses.py
```

### Run Tests
```bash
# Test GFP implementation
pytest tests/test_gfp_measures.py -v

# Test all modules
pytest tests/ -v
```

### View Results
```bash
# Open analysis page
start docs/analysis/small_increasing_vs_decreasing.md

# View collapsed localizer plot
start docs/assets/plots/small_increasing_vs_decreasing/small_increasing_vs_decreasing-collapsed_localizer.png
```

---

## Summary: What Makes This Approach Scientific Gold

✅ **Unbiased** - GFP uses all channels, collapsed localizer uses all conditions
✅ **Transparent** - Every decision is algorithmic and documented
✅ **Replicable** - Another researcher gets identical results from your code
✅ **Defendable** - Prevents circular analysis, citations provided
✅ **Adaptive** - FWHM windows match actual component characteristics
✅ **Rigorous** - Errors raised if components can't be reliably detected

**This is publication-ready, peer-review-proof science.**

---

## Further Reading

- **GFP Tutorial**: Murray, M. M., Brunet, D., & Michel, C. M. (2008). Topographic ERP analyses: A step-by-step tutorial review. *Brain Topography*, 20(4), 249-264.

- **Circular Analysis**: Poldrack, R. A., & Mumford, J. A. (2009). Independence in ROI analysis: where is the voodoo? *Social Cognitive and Affective Neuroscience*, 4(2), 208-213.

- **ERP Experimental Design**: Luck, S. J. (2014). *An introduction to the event-related potential technique* (2nd ed.). MIT Press. [Chapters 6-7 on component measurement]

- **FWHM in Signal Processing**: Oppenheim, A. V., & Schafer, R. W. (2010). *Discrete-time signal processing* (3rd ed.). Prentice Hall. [Chapter 7 on spectral analysis]

---

*Last Updated: 2025-01-12*
*Pipeline Version: GFP-FWHM v1.0*
*Contact: [Your Name/Email]*
