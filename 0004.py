from math import tan, pi

side_nums = int(input(">> Number of sides: "))
one_side_length = int(input(">> Length of one side: "))

surface = (side_nums * (one_side_length**2)) / (4 * (tan(pi / side_nums)))

print(">> Surface: %f" % surface)
