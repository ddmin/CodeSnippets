quadrant = lambda x, y: abs(((x!=0 and y!=0)) * ((x<0) - 4*(y<0) + (y>0)))

import random

# Zero Coordinates return zero
print("Points on Axes")
print(quadrant(0, 0))
print(quadrant(0, random.randint(1, 100)))
print(quadrant(random.randint(1, 100), 0))
print(quadrant(0, -random.randint(1, 100)))
print(quadrant(-random.randint(1, 100), 0))

# First Quadrant
print("First Quadrant")
print(quadrant(random.randint(1, 100), random.randint(1, 100)))
print(quadrant(random.randint(1, 100), random.randint(1, 100)))
print(quadrant(random.randint(1, 100), random.randint(1, 100)))

# Second Quadrant
print("Second Quadrant")
print(quadrant(-random.randint(1, 100), random.randint(1, 100)))
print(quadrant(-random.randint(1, 100), random.randint(1, 100)))
print(quadrant(-random.randint(1, 100), random.randint(1, 100)))

# Third Quadrant
print("Third Quadrant")
print(quadrant(-random.randint(1, 100), -random.randint(1, 100)))
print(quadrant(-random.randint(1, 100), -random.randint(1, 100)))
print(quadrant(-random.randint(1, 100), -random.randint(1, 100)))

# Fourth Quadrant
print("Fourth Quadrant")
print(quadrant(random.randint(1, 100), -random.randint(1, 100)))
print(quadrant(random.randint(1, 100), -random.randint(1, 100)))
print(quadrant(random.randint(1, 100), -random.randint(1, 100)))
