# Plot Spacing Fix - Watermark Text Overlap ✅

## Problem Identified

The build stamp (watermark with config/date) at the bottom of plots was overlapping with the measurement window caption text, causing occlusion and reduced readability.

### Previous Layout:
```
[Plot area]
---
Caption text (window info) at y = 0.012
Build stamp at y = 0.002  ← TOO CLOSE! Overlapping!
```

---

## Solution Implemented

### Changes Made

**File:** `src/eeg/stats_plots.py`

#### 1. Increased Bottom Margin
- **Before:** `bottom=0.16` (for boxplot), `bottom=0.12` (for violin)
- **After:** `bottom=0.20` (both plots)

#### 2. Repositioned Caption Higher
- **Before:** `y=0.012` (boxplot), `y=0.01` (violin)
- **After:** `y=0.025` (both plots)

#### 3. Moved Build Stamp Lower
- **Before:** Always at `y=0.002`
- **After:** `y=-0.015` (when caption present), `y=0.002` (when no caption)

#### 4. Adjusted Tight Layout
- **Before:** `rect=(0, 0.02, 1, 1)`
- **After:** `rect=(0, 0.03, 1, 1)` (when caption present)

### New Layout:
```
[Plot area - expanded vertically at bottom]
---
Caption text at y = 0.025 (higher)
    ↕ Clear separation
Build stamp at y = -0.015 (much lower)
```

---

## Visual Changes

### Spacing Metrics:

**Before:**
- Caption at y=0.012
- Stamp at y=0.002
- **Separation:** 0.010 units (TOO SMALL)
- Plot height: ~1805 pixels

**After:**
- Caption at y=0.025
- Stamp at y=-0.015
- **Separation:** 0.040 units (4× larger!)
- Plot height: ~1836 pixels (expanded by 31 pixels)

---

## Code Changes

### Boxplot (`plot_boxplot` function):

```python
# Before
fig.text(0.5, 0.012, caption, ...)  # Caption
plt.subplots_adjust(bottom=0.16)
fig.text(0.995, 0.002, build_stamp, ...)  # Stamp
plt.tight_layout(rect=(0, 0.02, 1, 1))

# After
fig.text(0.5, 0.025, caption, ...)  # Caption HIGHER
plt.subplots_adjust(bottom=0.20)  # MORE bottom margin
stamp_y = -0.015 if bottom_used else 0.002  # Stamp MUCH LOWER
fig.text(0.995, stamp_y, build_stamp, ...)
bottom_rect = 0.03 if bottom_used else 0.02
plt.tight_layout(rect=(0, bottom_rect, 1, 1))
```

### Violin Plot (`plot_violin` function):

Same changes applied for consistency.

---

## Benefits

### 1. No More Overlapping
- ✅ Caption text fully readable
- ✅ Build stamp (config/date) clearly visible
- ✅ Both texts well-separated

### 2. Better Readability
- ✅ Caption easier to read (higher position)
- ✅ Build stamp not obscured
- ✅ Professional appearance

### 3. Adaptive Spacing
- ✅ When caption present: Large bottom margin
- ✅ When no caption: Normal margin (no wasted space)

---

## Testing

### Test Case: 12_13 Analysis
```bash
python scripts/run_statistics.py --config [test_config]
```

**Results:**
- ✅ Boxplots generated successfully
- ✅ Violin plots generated successfully
- ✅ Plot height increased from 1805 → 1836 pixels
- ✅ No text overlap observed
- ✅ Both caption and build stamp clearly readable

---

## Files Modified

1. **`src/eeg/stats_plots.py`**
   - `plot_boxplot()` - Lines 335-364
   - `plot_violin()` - Lines 464-490

---

## Backward Compatibility

✅ **Fully backward compatible:**
- Plots without captions: No change in appearance
- Plots with captions: Improved spacing (slightly taller)
- All existing code continues to work

---

## Re-Running Analyses

To regenerate all plots with improved spacing:

```bash
# Single analysis
python scripts/run_statistics.py --config configs/statistics/default.yaml

# All analyses
python scripts/run_all_statistics.py
```

**All boxplots and violin plots will have:**
- Clear separation between caption and build stamp
- Better readability
- Professional appearance

---

## Technical Details

### Coordinate System:
- Figure coordinates: (0, 0) = bottom-left, (1, 1) = top-right
- Caption at 0.025 = 2.5% from bottom
- Stamp at -0.015 = 1.5% BELOW bottom edge (inside expanded margin)

### Layout Strategy:
1. **Detect caption**: Track if caption is added (`bottom_used` flag)
2. **Adjust stamp position**: Place stamp lower if caption exists
3. **Expand margin**: Increase `subplots_adjust(bottom=...)` value
4. **Adjust tight_layout**: Modify rect to accommodate both texts

---

## Example Output

**Before Fix:**
```
┌─────────────────────────┐
│     [Plot Area]         │
│                         │
└─────────────────────────┘
Caption: N1 Latency measured...
Config: 2025-01-17 | table←Overlapping!
```

**After Fix:**
```
┌─────────────────────────┐
│     [Plot Area]         │
│                         │
│                         │ ← Expanded
└─────────────────────────┘
Caption: N1 Latency measured...

Config: 2025-01-17 | table...  ← Clear separation
```

---

## Summary

**Problem:** Build stamp overlapping with caption text
**Solution:** Expand bottom margin, move caption up, move stamp down
**Result:** Clear, readable plots with no text occlusion
**Status:** ✅ Implemented and tested

**Your plots now have proper spacing at the bottom with no overlapping text!** 🎉
