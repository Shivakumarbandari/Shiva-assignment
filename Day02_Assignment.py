
# problem 01

n = int(input("enter the number:"))
matrix = [list(range(1 + n * i, 1 + n * (i + 1)))for i in range(n)]
print(" the matrix of {} * {}: ".format(n, n))
for m in matrix:
    print(m)

print("_"*40)

# problem 02

m = 1
n = 500
while m <= n:
    res = 0
    temp = m
    noOfDigit = 0

    while temp > 0:
        temp = int(temp/10)
        noOfDigit = noOfDigit + 1
    num = m
    while num > 0:
        rem = num % 10
        pow = 1
        i = 0
        while i <noOfDigit:
            pow = pow * rem
            i = i + 1
        res = res + pow
        num = int(num/10)
    if res == m:
        print(res)
    m = m + 1

print("_"*40)

