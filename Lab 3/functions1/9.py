import math
def volume(radius):
    return (4/3) * math.pi * pow(radius, 3)

r = int(input('Enter the radius: '))
print(volume(r))