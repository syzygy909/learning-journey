''' # Train Example 2 for list
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
'''

printYeahhh