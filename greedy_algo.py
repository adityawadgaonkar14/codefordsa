# Fractional Knapsack using Greedy Algorithm

def fractional_knapsack(weights, profits, capacity):
    n = len(weights)
    ratio = []

    # Step 1: Calculate profit/weight ratio
    for i in range(n):
        ratio.append(profits[i] / weights[i])

    # Step 2: Combine and sort by ratio (descending order)
    items = list(zip(weights, profits, ratio))
    items.sort(key=lambda x: x[2], reverse=True)

    total_profit = 0
    remaining_capacity = capacity

    print("\nSelected items (weight, profit, taken fraction):")

    # Step 3: Pick items greedily
    for w, p, r in items:
        if remaining_capacity >= w:
            total_profit += p
            remaining_capacity -= w
            print(f"({w}, {p}, 1.0)")
        else:
            fraction = remaining_capacity / w
            total_profit += p * fraction
            print(f"({w}, {p}, {fraction:.2f})")
            break

    return total_profit


# -------- MAIN PROGRAM --------
n = int(input("Enter number of parcels: "))
weights = []
profits = []

for i in range(n):
    w = float(input(f"Enter weight of parcel {i+1}: "))
    p = float(input(f"Enter profit of parcel {i+1}: "))
    weights.append(w)
    profits.append(p)

capacity = float(input("Enter truck capacity: "))

print("\nWeights:", weights)
print("Profits:", profits)

max_profit = fractional_knapsack(weights, profits, capacity)

print(f"\nMaximum profit that can be earned: {max_profit:.2f}")
