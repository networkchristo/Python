#   1
#   11
#   111
#   1111
#   11111

def num(n):
    num = 1
    for i in range(0, n):
        num = 1
        for j in range(0, i+1):
            print(num, end="")
        print("\r")

n = 5
num(n)