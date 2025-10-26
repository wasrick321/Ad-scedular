import pytest
from src.ad_scheduler import Ad, greedy_by_ratio, brute_force_optimal


def make_sample():
    return [
        Ad(1, 1, 3, 50),
        Ad(2, 2, 5, 60),
        Ad(3, 4, 6, 70),
        Ad(4, 6, 9, 90),
        Ad(5, 8, 10, 40),
    ]


def test_bruteforce_optimal_on_sample():
    ads = make_sample()
    capacity = 10
    schedule, profit = brute_force_optimal(ads, capacity)
    # Expected from problem statement
    assert profit == 210
    ids = sorted([a.id for a in schedule])
    assert ids == [1, 3, 4]


def test_greedy_ratio_matches_optimal_on_sample():
    ads = make_sample()
    capacity = 10
    schedule, profit = greedy_by_ratio(ads, capacity)
    # On this small example greedy_by_ratio should find the optimal
    assert profit == 210
