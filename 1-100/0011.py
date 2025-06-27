year1 = float(input(">> Enter the cost for the first year: "))
year2 = float(input(">> Enter the cost for the second year: "))

inflation_rate = (year2 - year1) / year1
year3 = year1 + (year2 * inflation_rate)

print(f">> Inflation rate is: %{inflation_rate}\n>> The price for the next year: {year3}")