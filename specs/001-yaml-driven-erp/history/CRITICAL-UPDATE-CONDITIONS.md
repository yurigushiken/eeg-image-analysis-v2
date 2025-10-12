# CRITICAL UPDATE: Condition Definitions

**Date**: 2025-10-11
**Status**: ⚠️ **SUPERSEDES** previous terminology in CLARIFICATIONS-2025-10-11.md Section 7

---

## ❌ **INCORRECT PREVIOUS UNDERSTANDING** (NOW DEPRECATED)

In `CLARIFICATIONS-2025-10-11.md` Section 7, we incorrectly documented:
```
Condition = Metadata column value (e.g., "iSS", "dLL", "NC")
```

This was based on `previous-study.txt` which described a **DIFFERENT project** (15 participants, grouped analysis).

## ✅ **CORRECT UNDERSTANDING FOR THIS PROJECT**

### **This Project: Individual Condition Codes (24 participants)**

**Condition codes are NUMERIC pairs** representing specific trial types:

```
Observed Condition codes (from README.md):
11, 12, 13, 14, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 36,
41, 42, 43, 44, 45, 46, 52, 53, 54, 55, 56, 63, 64, 65, 66
```

**Structure**: Each condition code is a **two-digit number**:
- **First digit**: Starting number (1-6)
- **Second digit**: Ending number (1-6)
- **Examples**:
  - `12` = Started with 1 dot, changed to 2 dots (Increasing Small-to-Small)
  - `32` = Started with 3 dots, changed to 2 dots (Decreasing Small-to-Small)
  - `44` = Started with 4 dots, stayed at 4 dots (No Change Large)
  - `46` = Started with 4 dots, changed to 6 dots (Increasing Large-to-Large)
  - `63` = Started with 6 dots, changed to 3 dots (Decreasing Large-to-Small crossover)

### **Metadata Structure** (from README.md line 40-46):

```python
# Epoch metadata columns:
- Condition: "11", "12", "13", ..., "66"  # Two-digit string codes
- direction: "I" (Increasing), "D" (Decreasing), "NC" (No Change)
- change_group: "iSS", "dSS", "iLL", "dLL", "iSL", "dLS", "NC"  # Derived categories
- size: "SS" (Small-to-Small), "LL" (Large-to-Large), "cross" (crossover), "NC"
- Target.ACC: 1 (correct), 0 (incorrect)
```

### **KEY DISTINCTION FOR THIS PROJECT**

**We are NOT using the grouped categories** (`change_group`, `direction`, `size`).

**We ARE analyzing individual condition codes** (e.g., `12`, `32`, `44`).

This allows:
- Fine-grained analysis of specific numerical transitions
- Direct comparison of condition pairs (e.g., 12 vs 21, 45 vs 54)
- Flexible grouping in YAML configs without pre-imposed categories

---

## 📝 **Updated Terminology**

| Term | Definition | Example Usage |
|------|------------|---------------|
| **Condition** | Two-digit numeric code for a specific trial type | `Condition="12"` means 1→2 transition |
| **Group** | Analysis-defined collection of conditions via YAML | `"From1"` group = conditions starting with 1 (11, 12, 13, 14) |
| **Metadata filter** | YAML syntax to select conditions | `filter: {Condition: ["12", "13", "14"]}` |
| **Transition** | The numerical change in a trial | 1→2 is an increasing transition |

---

## 📊 **Example YAML Configurations**

### **Example 1: Analyze Transitions "From 1" to Any Other Number**

```yaml
selection:
  response: "ACC1"  # Only correct responses (Target.ACC==1)
  min_epochs_per_group: 8

  include_groups:
    # Group: Transitions starting from 1
    - name: "From1_to_2"
      filter: {Condition: ["12"]}

    - name: "From1_to_3"
      filter: {Condition: ["13"]}

    - name: "From1_to_4"
      filter: {Condition: ["14"]}

    # Note: "11" (1→1) is No Change, excluded implicitly
```

### **Example 2: Compare Increasing vs Decreasing (Using `direction` Metadata)**

While we don't use `change_group`, we CAN still use the `direction` column:

```yaml
selection:
  include_groups:
    - name: "Increasing"
      filter: {direction: "I"}  # Selects all increasing transitions

    - name: "Decreasing"
      filter: {direction: "D"}  # Selects all decreasing transitions

  exclude:
    - filter: {direction: "NC"}  # Exclude No Change trials
```

This would group:
- **Increasing**: 12, 13, 14, 21, 23, 24, 25, 31, 32, 34, 35, 36, 41, 42, 43, 45, 46, 52, 53, 54, 56, 63, 64, 65
- **Decreasing**: 21, 31, 32, 41, 42, 43, 51, 52, 53, 54, 61, 62, 63, 64, 65

### **Example 3: Analyze Specific Condition Pairs**

```yaml
selection:
  include_groups:
    - name: "1to2"
      filter: {Condition: ["12"]}

    - name: "2to1"
      filter: {Condition: ["21"]}

    - name: "4to5"
      filter: {Condition: ["45"]}

    - name: "5to4"
      filter: {Condition: ["54"]}
```

This allows direct comparison of:
- Increasing vs Decreasing within Small range (1↔2)
- Increasing vs Decreasing within Large range (4↔5)

---

## 🔄 **Required Documentation Updates**

### **Files Requiring Updates**:

1. ✅ **spec.md**:
   - Update User Story examples to use numeric condition codes
   - Update FR-006 examples to use `Condition: ["12", "13"]` instead of `direction: "I"`
   - Update clarifications section (remove references to "iSS", "dLL" categories)

2. ✅ **CLARIFICATIONS-2025-10-11.md**:
   - Replace Section 7 "Terminology Clarification" entirely
   - Link to this document for correct definitions

3. ✅ **contracts/peak-detection-algorithm.md**:
   - Update example YAML snippets to use numeric conditions
   - Update comments referencing "Increasing vs Decreasing" to clarify they use `direction` metadata OR explicit condition lists

4. ✅ **tasks.md**:
   - Update T101 sample YAML to use correct condition syntax
   - Update task descriptions referencing "Increasing vs Decreasing" to clarify implementation

5. ✅ **plan.md**:
   - Update YAML schema examples (line 85-88, 98-103)
   - Clarify that `include_groups` uses either:
     - Explicit condition lists: `{Condition: ["12", "13", "14"]}`
     - Derived metadata: `{direction: "I"}` (still valid!)

6. ✅ **environment.yml**:
   - Already correct (no condition-specific references)

7. ✅ **README.md**:
   - Already correct (user updated line 40 with accurate condition codes)
   - Update line 15: `conda activate numbers-eeg` → `conda activate eeg-image`

---

## 🔧 **Montage File Path Update**

### **Current Path** (Verified via Glob):
```
assets/net/AdultAverageNet128_v1.sfp
```

### **User Request**: Move to `assets/` root

**Status**: File is currently at `assets/net/AdultAverageNet128_v1.sfp`

**Action Required**:
```bash
# If you want to move it:
mv assets/net/AdultAverageNet128_v1.sfp assets/AdultAverageNet128_v1.sfp
rmdir assets/net  # If empty
```

### **All References to Update**:
| File | Current Reference | New Reference |
|------|------------------|---------------|
| spec.md FR-008, FR-019 | `net/AdultAverageNet128_v1.sfp` | `assets/AdultAverageNet128_v1.sfp` |
| plan.md (multiple) | `net/AdultAverageNet128_v1.sfp` | `assets/AdultAverageNet128_v1.sfp` |
| tasks.md T012 | `net/AdultAverageNet128_v1.sfp` | `assets/AdultAverageNet128_v1.sfp` |
| CLARIFICATIONS-2025-10-11.md F003 | `net/AdultAverageNet128_v1.sfp` | `assets/AdultAverageNet128_v1.sfp` |
| contracts/peak-detection-algorithm.md | (no references) | N/A |

**Recommendation**: Keep at current path `assets/net/` to maintain subdirectory organization (montages are a specific asset type). Update documentation to reflect `assets/net/`.

**Alternative**: If you prefer `assets/` root for simplicity, move the file and update all references.

---

## 📋 **Summary of Changes**

### **What Changed**:
1. ❌ **Removed**: References to grouped condition categories ("iSS", "dLL", "NC") as if they were raw condition codes
2. ✅ **Added**: Correct understanding that `Condition` = numeric codes (12, 32, 44, etc.)
3. ✅ **Clarified**: Metadata columns (`direction`, `change_group`, `size`) are **derived features**, not primary condition identifiers
4. ✅ **Emphasized**: This project analyzes **individual condition codes**, not pre-grouped categories
5. ✅ **Created**: `manuscript/works-cited.txt` with Kriegeskorte et al. (2009) and Luck (2014) full citations and quotes

### **What Stayed The Same**:
- ✅ LOPO peak detection algorithm (still correct)
- ✅ Environment specification (eeg-image with Python 3.12)
- ✅ Smoothing specification (boxcar, reflection padding)
- ✅ Tasks.md structure (correct for this project)
- ✅ Success criteria (SC-001 through SC-004)

---

## 🎯 **Impact on Implementation**

### **No Changes Required for**:
- Phase 1 (Setup): Directory structure, environment.yml (✅ already uses eeg-image)
- Phase 2 (Foundational): Core library modules (config.py, io.py, erp.py, plots.py, report.py)
  - `src/eeg/select.py` will handle BOTH:
    - Explicit condition lists: `{Condition: ["12", "13", "14"]}`
    - Metadata filters: `{direction: "I"}` (uses epochs.metadata query)

### **Minor Updates Required for**:
- T101 (Sample YAML): Use correct condition syntax in example
- T104 (Linestyles verification): Clarify that linestyles map to conditions OR derived categories
- Documentation polish tasks (TX01): Update terminology in README, quickstart

---

## ✅ **Action Items**

- [x] Created `manuscript/works-cited.txt` with Kriegeskorte and Luck papers
- [ ] Move montage file: `assets/net/AdultAverageNet128_v1.sfp` → `assets/AdultAverageNet128_v1.sfp` (user decision)
- [ ] Update spec.md with correct condition examples
- [ ] Update CLARIFICATIONS-2025-10-11.md Section 7 (link to this document)
- [ ] Update plan.md YAML examples (use numeric conditions)
- [ ] Update tasks.md T101 sample YAML (use numeric conditions)
- [ ] Update contracts/peak-detection-algorithm.md examples
- [ ] Update README.md line 15: `numbers-eeg` → `eeg-image`

---

Archived copy exists under `specs/001-yaml-driven-erp/history/CRITICAL-UPDATE-CONDITIONS.md`.

**This document supersedes**: CLARIFICATIONS-2025-10-11.md Section 7 "Terminology Clarification"
