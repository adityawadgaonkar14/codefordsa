class Parcel:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
        self.ratio = profit / weight

def fractional_knapsack(parcels, capacity):
    parcels.sort(key=lambda x: x.ratio, reverse=True)
    total_profit = 0.0
    remaining_capacity = capacity

    for p in parcels:
        if p.weight <= remaining_capacity:
            total_profit += p.profit
            remaining_capacity -= p.weight
        else:
            total_profit += p.profit * (remaining_capacity / p.weight)
            break
    return total_profit

# Example
n = int(input("Enter number of parcels: "))
parcels = []
for i in range(n):
    w = float(input(f"Weight of parcel {i+1}: "))
    p = float(input(f"Profit of parcel {i+1}: "))
    parcels.append(Parcel(w, p))

capacity = float(input("Enter truck capacity: "))
max_profit = fractional_knapsack(parcels, capacity)
print("Maximum Profit:", round(max_profit, 2))

