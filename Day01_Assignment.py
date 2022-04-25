
#patterns

for i in range(5, 0, -1):
    for k in range(6-i, 1, -1):
        print(" ", end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()
for i in range(2, 6):
     for k in range(1, 6 - i):
            print(" ", end="")
     for j in range(i, 0, -1):
            print(j, end=" ")
     print()

# 1.pattern 01

count=1
for i in range(1, 6):
    for j in range(1,i):
        print(count, end="")
        if count==9:
            count=0
        else:
            count=count+1
    print()

# 1.pattern  02
for i in range(1,6):
    for j in range(0,i):
        print(i,end="")
    print()

# 1.pattern 03

for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k, end=" ")
    print()
for i in range(5,0,-1):
    for j in range(0,6-i):
        print(" ",end="")
    for k in range(1,i):
        print(k,end=" ")
    print()

# 2.write a code to generate fibonacci series

print("_"*40)

n = int(input("enter the num of terms:"))
n1, n2 = 0, 1
count = 0
if n ==1:
    print(n1)
else:
    print("Fibonacci series:")
    while count < n:
        print(n1)

        n3 = n1 + n2
        n1 = n2
        n2= n3
        count += 1

print("_"*40)


# prime number
cntr = 0
for i in range(150, 49, -1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
         print(i, end=" ")
         cntr += 1
print(f"\nthere are {cntr} prime numbers between 150 and 50")

# 3
factorial = [1, 1, 2, 6, 24, 120,
             720, 5040, 40320, 362880]


def isStrong(N):

    num = str(N)

    sum = 0

    for i in range(len(num)):
        sum += factorial[ord(num[i]) -
                         ord('0')]

    if sum == N:
        return True
    else:
        return False

def printStrongNumbers(N):

    for i in range(1, N + 1):

        if (isStrong(i)):
            print(i, end=" ")

if __name__ == "__main__":

    N = 2000

    printStrongNumbers(N)

# 5.problem--- greedy code

cntr = 0
j = 1
while cntr < 6:
    num = j
    flag = False
    lst = []
    for i in range(3):
        if (num - 1) % 3 ==0:
            res = (num -1) // 3 + 1
            lst.append(res)
            num = num - res
            if i == 2:
                flag = True
        else:
            break
    if flag and num and num % 3 == 0:
        print("Total {} --> remaining {} --> father distributes {} to each daughter".format(j, num, num//3))
        print("\t\tDaughter #1 --> {}\n\t\tDaughter #2 --> {}\n\t\tDaughter #3 --> {}".format(lst[0], lst[1], lst[2]))
        cntr +=1
    j += 1
