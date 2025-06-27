radius = float(input(">> Radius: "))
pi = 22 / 7

surface = 4 * pi * (radius**2)
volume = (4/3) * (pi * (radius**3))

print(">> Surface: %f | Volume: %f (PS: PI: %f)" % (surface, volume, pi))