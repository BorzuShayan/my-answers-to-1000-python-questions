number = int(input(">> Enter a two digit number: "))

firstD = number // 10
secondD = number % 10

print(f">> {firstD} + {secondD} = {firstD + secondD}\n>> Reverse: {secondD}{firstD}")
