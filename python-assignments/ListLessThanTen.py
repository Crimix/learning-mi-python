import sys

l = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("Less than what number?")
number = input()
new_list = [i for i in l if (i < int(number))]

for i in new_list:
    print(i)


