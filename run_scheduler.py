"""Simple runner to demonstrate the ad allocation algorithms."""
from src.ad_scheduler import Ad, greedy_by_ratio, greedy_by_bid, brute_force_optimal, format_schedule


def demo():
    ads = [
        Ad(1, 1, 3, 50),
        Ad(2, 2, 5, 60),
        Ad(3, 4, 6, 70),
        Ad(4, 6, 9, 90),
        Ad(5, 8, 10, 40),
    ]
    capacity = 10

    print("Sample ads:")
    for a in ads:
        print(f"Ad {a.id}: [{a.start}-{a.end}] Bid=₹{a.bid} Duration={a.duration}")

    print("\nRunning greedy_by_ratio...")
    schedule, profit = greedy_by_ratio(ads, capacity)
    print(format_schedule(schedule))
    print(f"Total Profit (Greedy ratio): ₹{profit}")

    print("\nRunning greedy_by_bid...")
    schedule2, profit2 = greedy_by_bid(ads, capacity)
    print(format_schedule(schedule2))
    print(f"Total Profit (Greedy bid): ₹{profit2}")

    print("\nComputing brute-force optimal (small input)...")
    opt_schedule, opt_profit = brute_force_optimal(ads, capacity)
    print(format_schedule(opt_schedule))
    print(f"Total Profit (Optimal): ₹{opt_profit}")


if __name__ == "__main__":
    demo()
