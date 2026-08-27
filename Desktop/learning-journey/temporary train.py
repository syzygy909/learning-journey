''' # Find Prime number in range (1 to 100)
for x in range(0, 21):
    for y in range(0, 34):
        for z in range(0, 101, 3):
            if x + y + z == 100 and (5 * x) + (3 * y) + (z // 3) == 100:
                print(f"x = {x}, y = {y}, z = {z}")
'''


import random

n = int(input("Set of numbers: "))

for x in range (n):
    red = [i for i in range(1, 34)]
    blue = [random.randrange(1,17)]
    B = random.choice(blue)
    R = list(random.sample(red, 6))
    R.sort
    [print(f"\033[31m{x:0>2d}", end = " ") for x in R]
    print(f"\033[34m{B:0>2d}")
    print()


