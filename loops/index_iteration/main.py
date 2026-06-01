prices = [29.99, 45.50, 12.75, 38.20]
discounts = [.10, .20, .15, .05]

for i in range(len(prices)):
    prices[i] = prices[i] * (1 - discounts[i])

for p in range(len(prices)):
    print(f"Updated price for item {p + 1}:", f"${prices[p]:.2f}")
