# Online Ad Slot Allocation — Project Report

This repository contains a small project demonstrating a hybrid approach to online ad slot allocation that combines Greedy selection, Kruskal-like conflict avoidance, and Knapsack-inspired capacity constraints.

Contents
- `src/ad_scheduler.py` — core algorithms (Ad class, greedy_by_ratio, greedy_by_bid, brute_force_optimal).
- `run_scheduler.py` — CLI/demo runner for the sample dataset.
- `Main_website/index.html` — simple browser UI to visualize greedy allocation.
- `tests/test_scheduler.py` — pytest tests comparing greedy vs brute-force on the sample input.
- `requirements.txt` — pytest dependency.

How to run
1. Install dependencies (optional, for tests):

   pip install -r requirements.txt

2. Run demo runner:

   python run_scheduler.py

3. Run tests:

   python -m pytest -q

Design notes
- Greedy strategy sorts ads by bid/duration ratio (value density) similar to fractional knapsack, then selects ads that do not overlap with already-chosen ones — this enforces conflict-free allocation (Kruskal-style).
- Brute-force checks all subsets and is used only for verification on small inputs.
- Time complexity: sorting O(n log n) + O(n^2) conflict checks in the naive greedy; brute-force is O(2^n).

Future improvements
- Implement interval trees or balanced segment trees to reduce conflict checks to O(n log n).
- Add a DP solution when capacity is small (0/1 knapsack with interval constraints is more complex).
- Add more robust UI and interactive input.
