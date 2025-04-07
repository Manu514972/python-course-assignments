import math

rad = input("Enter the radius of the circle:")
rad_num = float(rad)
circle_area = math.pi*(rad_num**2.0)
circle_circum = math.pi*2.0*rad_num
print("The area of the circle =", circle_area)
print("The circumference of the circle =", circle_circum)