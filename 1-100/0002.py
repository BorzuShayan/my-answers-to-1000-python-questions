radius = float(input(">> Radius: "))
height = float(input(">> Height: "))
pi = 22 / 7

volume = radius**2 * pi * height
surface =  (2 * pi * radius * height) + 2 * (pi * (radius**2))

print(">> Volume: %f | Surface: %f (PS: PI: %f)" % (volume, surface, pi))