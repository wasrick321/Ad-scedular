from dataclasses import dataclass
from typing import List, Tuple
import itertools


@dataclass
class Ad:
    id: int
    start: int
    end: int
    bid: float

    def __post_init__(self):
        self.duration = self.end - self.start
        # protect division by zero
        self.ratio = self.bid / self.duration if self.duration > 0 else float('inf')


def overlap(a: Ad, b: Ad) -> bool:
    return not (a.end <= b.start or b.end <= a.start)


def _is_conflict_free(subset: List[Ad]) -> bool:
    for i in range(len(subset)):
        for j in range(i + 1, len(subset)):
            if overlap(subset[i], subset[j]):
                return False
    return True


def greedy_by_ratio(ads: List[Ad], capacity: int) -> Tuple[List[Ad], float]:
    ads = sorted(ads, key=lambda x: x.ratio, reverse=True)
    schedule: List[Ad] = []
    total_time = 0
    total_profit = 0

    for ad in ads:
        conflict = False
        for s in schedule:
            if overlap(ad, s):
                conflict = True
                break
        if not conflict and total_time + ad.duration <= capacity:
            schedule.append(ad)
            total_time += ad.duration
            total_profit += ad.bid

    return schedule, total_profit


def greedy_by_bid(ads: List[Ad], capacity: int) -> Tuple[List[Ad], float]:
    ads = sorted(ads, key=lambda x: x.bid, reverse=True)
    schedule: List[Ad] = []
    total_time = 0
    total_profit = 0

    for ad in ads:
        if all(not overlap(ad, s) for s in schedule) and total_time + ad.duration <= capacity:
            schedule.append(ad)
            total_time += ad.duration
            total_profit += ad.bid

    return schedule, total_profit


def brute_force_optimal(ads: List[Ad], capacity: int) -> Tuple[List[Ad], float]:
    best_profit = 0
    best_subset: List[Ad] = []

    n = len(ads)
    for r in range(1, n + 1):
        for comb in itertools.combinations(ads, r):
            subset = list(comb)
            total_time = sum(a.duration for a in subset)
            if total_time > capacity:
                continue
            if not _is_conflict_free(subset):
                continue
            profit = sum(a.bid for a in subset)
            if profit > best_profit:
                best_profit = profit
                best_subset = subset

    best_subset = sorted(best_subset, key=lambda x: x.start)
    return best_subset, best_profit


def format_schedule(schedule: List[Ad]) -> str:
    lines = []
    for a in sorted(schedule, key=lambda x: x.start):
        lines.append(f"Ad {a.id}: [{a.start}-{a.end}] Bid=₹{a.bid} Duration={a.duration}")
    return "\n".join(lines)


if __name__ == "__main__":
    sample_ads = [
        Ad(1, 1, 3, 50),
        Ad(2, 2, 5, 60),
        Ad(3, 4, 6, 70),
        Ad(4, 6, 9, 90),
        Ad(5, 8, 10, 40),
    ]
    cap = 10
    s, p = greedy_by_ratio(sample_ads, cap)
    print("Greedy (ratio) schedule")
    print(format_schedule(s))
    print("Total Profit: ₹", p)

    opt_s, opt_p = brute_force_optimal(sample_ads, cap)
    print("\nBrute force optimal schedule")
    print(format_schedule(opt_s))
    print("Total Profit: ₹", opt_p)
