number = int(input(">> Enter the X: "))

# 31 * x - 17 * x + 5
search4y = ((number << 5) - number) - ((number << 4) + number) +5 

print(f">> If Y was 31 * x - 17 * x + 5 and X was {number}\n>> The answer is: {search4y}")