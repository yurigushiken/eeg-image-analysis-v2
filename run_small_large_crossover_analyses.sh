#!/bin/bash
# Script to run all Small vs Large vs Crossover analyses
# Testing hypothesis: "1" drives the small-large differences

echo "============================================"
echo "Running Small vs Large vs Crossover Analyses"
echo "Testing hypothesis: '1' is driving the effects"
echo "============================================"

# WITH "1" - Increasing Direction
echo ""
echo "[1/8] Running: Increasing (Small/Large/Crossover) - ALL trials..."
python scripts/run_analysis.py --config configs/analyses/increasing_large_vs_small_vs_crossover.yaml

echo ""
echo "[2/8] Running: Increasing (Small/Large/Crossover) - ACC1 only..."
python scripts/run_analysis.py --config configs/analyses/increasing_large_vs_small_vs_crossover_ACC1.yaml

# WITH "1" - Decreasing Direction
echo ""
echo "[3/8] Running: Decreasing (Small/Large/Crossover) - ALL trials..."
python scripts/run_analysis.py --config configs/analyses/decreasing_large_vs_small_vs_crossover.yaml

echo ""
echo "[4/8] Running: Decreasing (Small/Large/Crossover) - ACC1 only..."
python scripts/run_analysis.py --config configs/analyses/decreasing_large_vs_small_vs_crossover_ACC1.yaml

# WITHOUT "1" - Increasing Direction
echo ""
echo "[5/8] Running: Increasing WITHOUT '1' (Small/Large/Crossover) - ALL trials..."
python scripts/run_analysis.py --config configs/analyses/increasing_large_vs_small_vs_crossover_without_1.yaml

echo ""
echo "[6/8] Running: Increasing WITHOUT '1' (Small/Large/Crossover) - ACC1 only..."
python scripts/run_analysis.py --config configs/analyses/increasing_large_vs_small_vs_crossover_without_1_ACC1.yaml

# WITHOUT "1" - Decreasing Direction
echo ""
echo "[7/8] Running: Decreasing WITHOUT '1' (Small/Large/Crossover) - ALL trials..."
python scripts/run_analysis.py --config configs/analyses/decreasing_large_vs_small_vs_crossover_without_1.yaml

echo ""
echo "[8/8] Running: Decreasing WITHOUT '1' (Small/Large/Crossover) - ACC1 only..."
python scripts/run_analysis.py --config configs/analyses/decreasing_large_vs_small_vs_crossover_without_1_ACC1.yaml

echo ""
echo "============================================"
echo "All ERP analyses complete!"
echo "============================================"
echo ""
echo "Next step: Run statistics on each analysis"
echo "See: run_small_large_crossover_stats.sh"
echo ""
