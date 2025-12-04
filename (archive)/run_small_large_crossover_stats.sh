#!/bin/bash
# Script to run statistics for all Small vs Large vs Crossover analyses

echo "============================================"
echo "Running Statistics for Small vs Large vs Crossover"
echo "============================================"

# Create stats config YAMLs for each analysis
echo ""
echo "Creating statistics configuration files..."
python scripts/create_stat_configs.py

# WITH "1" - Increasing Direction
echo ""
echo "[1/8] Running statistics: Increasing (with 1) - ALL trials..."
python scripts/run_statistics.py --config configs/statistics/increasing_large_vs_small_vs_crossover.yaml

echo ""
echo "[2/8] Running statistics: Increasing (with 1) - ACC1 only..."
python scripts/run_statistics.py --config configs/statistics/increasing_large_vs_small_vs_crossover_ACC1.yaml

# WITH "1" - Decreasing Direction
echo ""
echo "[3/8] Running statistics: Decreasing (with 1) - ALL trials..."
python scripts/run_statistics.py --config configs/statistics/decreasing_large_vs_small_vs_crossover.yaml

echo ""
echo "[4/8] Running statistics: Decreasing (with 1) - ACC1 only..."
python scripts/run_statistics.py --config configs/statistics/decreasing_large_vs_small_vs_crossover_ACC1.yaml

# WITHOUT "1" - Increasing Direction
echo ""
echo "[5/8] Running statistics: Increasing (without 1) - ALL trials..."
python scripts/run_statistics.py --config configs/statistics/increasing_large_vs_small_vs_crossover_without_1.yaml

echo ""
echo "[6/8] Running statistics: Increasing (without 1) - ACC1 only..."
python scripts/run_statistics.py --config configs/statistics/increasing_large_vs_small_vs_crossover_without_1_ACC1.yaml

# WITHOUT "1" - Decreasing Direction
echo ""
echo "[7/8] Running statistics: Decreasing (without 1) - ALL trials..."
python scripts/run_statistics.py --config configs/statistics/decreasing_large_vs_small_vs_crossover_without_1.yaml

echo ""
echo "[8/8] Running statistics: Decreasing (without 1) - ACC1 only..."
python scripts/run_statistics.py --config configs/statistics/decreasing_large_vs_small_vs_crossover_without_1_ACC1.yaml

echo ""
echo "============================================"
echo "All statistical analyses complete!"
echo "============================================"
echo ""
echo "Results are in: docs/assets/stats/<analysis_name>/"
echo ""
echo "KEY COMPARISONS FOR YOUR HYPOTHESIS:"
echo "1. Compare WITH '1' vs WITHOUT '1' for Small-Large differences"
echo "2. Look for reduced/eliminated effects when '1' is removed"
echo "3. Check P3b amplitude patterns across conditions"
echo ""
