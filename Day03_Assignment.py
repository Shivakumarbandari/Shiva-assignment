# prob01  Day03
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic4 = {}

dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)

print(dic4)

# problem 02
print(40 * "-")
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def is_key_present(a):
    if a in d:
        print("key is present")
    else:
        print("key is not present")
res1 = is_key_present(6)
res2 = is_key_present(7)

# problem 03 using for loops
print(40 * "-")
d1 = {'a':'alpha', 'b':'bravo', 'c':'charlie', 'd':'delta'}
for key, value in d1.items():
    print(key,  value)

# problem 04
print(40 * "-")
n=5
dict = dict()
for i in range(1, n+1):
    dict[i]= i*i
print(dict)

# problem 05
print(40 * "-")
d1 = {'a':10, 'b':15, 'c':25, 'd':10, 'e':15, 'f':20}
temp =[]
res = {}
for key, value in d1.items():
    if value not in temp:
        temp.append(value)
        res[key] = value
    print(res)

# problem 06
print(40 * "-")

dict = {'Abs': 10, 'if': 2, 'cd':10, 'gks': 8, 'nm': 2}

print(min(dict, key=dict.get))

# problem 07

print(40 * "-")

list =[1, 2, 3, 4, 5, 6, 7, 8]
list.reverse()
print(list)

# problem 08
print(40 * "-")

l = [0, 1, 2, 3, 1, 0, 0, 0, 1, 1]
val = 0

try:
    while True:
        l.remove(val)
except ValueError:
   pass
print(l)

# or
print(40 * "-")
l = [0, 1, 2, 3, 1, 0, 0, 0, 1, 1]
val = 0
l=[i for i in l if i != val ]
print(l)

# problem 09
print(40 * "-")

A = [1, 2, 3, 4, 5]
sum = sum(A)
print(f"sum :{sum}")

print("-"*40)

sum = 0
for i in A:
    sum += i
print(f"sum :{sum}")

# problem 10
print(40 * "-")
list = [20, 30, 40, 25, 10, 60, 50, 55]

list.sort()
print(list[-2])

# problem 11
print(40 * "-")

list = [20, 30, 40, 25, 10, 60, 50, 55]

list.sort()
print(list[1])

# problem 12
print(40 * "-")
sample_list =[10, 20, 30, 40, 20, 50, 60, 40]
print(sample_list)
my_set = set(sample_list)
converted_list=(my_set)
print(converted_list)


# problem 13
def countX(list, x):
    return list.count(x)

list=[10, 20, 30, 40, 20, 50, 60, 40]

x = 20
print(countX(list, x))

# problem 14
l1=[1,2,3,4,5,6]
l2=[2,4,5,6,7,8]

common_ele=set(l1).intersection(set(l2))
print(common_ele)

# problem 15

def list_count(list_A):
    return len(list_A)

list_A=[[1,3],[5,7],[9,10],[13,15,19]]
print(list_count(list_A))
