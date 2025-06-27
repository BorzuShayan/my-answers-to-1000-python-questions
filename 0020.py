numbers = list(map(int,input(">> Enter R1, R2, R3: ").split()))

resistance = (numbers[0] * numbers[1] + numbers[0] * numbers[2] + numbers[1] * numbers[2]) / (numbers[0] * numbers[1] * numbers[2])

print(f">> The resistance is: {resistance}")