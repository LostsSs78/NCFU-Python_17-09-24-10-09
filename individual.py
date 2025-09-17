base_small = int(input("Enter first base (smaller):\n>"))
base_big = int(input("Enter second base (bigger):\n>"))
height = int(input("Enter height:\n>"))

base_right_anlge_triangle = (base_big - base_small) / 2
hypotenuse = (height**2 + base_right_anlge_triangle**2)

perimetr = (hypotenuse * 2) + base_big + base_small

print(f"Perimetr of trapezoid: {perimetr}")
