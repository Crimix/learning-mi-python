import sys


def even(num):
    return (num % 2 == 0)

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_list = [i for i in a if even(i)]

for i in even_list:
    print(i)