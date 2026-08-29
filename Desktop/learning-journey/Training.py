''' # Function for finding prime numbers in a given range
def judge(n) -> bool:
    for x in range(2, int((n ** 0.5) // 1) + 1):
        if n % x == 0:
            return False
    return True


for i in range(2, 100):
    if judge(i):
        print(i)
'''


def judge(a, b, c) -> bool:
    if a + b > c and b + c > a and a + c > b:
        return True

def calc_P(a, b, c):
    P = a + b + c


a, b, c = (input("The lengths for a triangle: "))
if judge(a, b, c) == True:
    print(f"The perimeter of the triangle is {judge(a, b, c)}")
else:
    print("a + b > c and b + c > a and a + c > b, hence please give a new input data set")