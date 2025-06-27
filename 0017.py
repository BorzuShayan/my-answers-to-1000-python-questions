cost = float(input(">> Enter the cost: "))
rate = float(input(">> Enter the rate: "))
year = float(input(">> For how many year(s): "))

futureCost = cost * (1+(0.01 *rate)) ** year

print(f">> Future cost is: {futureCost}")