import math
import sys

rad = float(sys.argv[1])
circle_area = math.pi * (rad ** 2)
circle_circum = math.pi * 2 * rad
print("The area of the circle =", circle_area)
print("The circumference of the circle =", circle_circum)
