# Time Complexity / Order of Growth defines the amount
# of time taken by any program with respect to the size
# of the input

# essentially specifies how the program would behave as the
# order of size of input is increased

# Constant Time Complexity
# O(1): constant running time

from array import array
from ctypes import BigEndianStructure
from re import S


def my_sum(a, b):
    return a+b

# print(my_sum(6,9))

"""
1 step to add a and b
Time complexity = 1

"""

# Linear Time Complexity
# O[n]: linear running time

def sum_of_list(my_list):
    result = 0
    for i in my_list:
        result += i
    return result

# daily_fruit_sales = [1, 2, 3, 4, 5, 6, 7]
# print(sum_of_list(daily_fruit_sales))

"""
1 step for initialising result
Loop over the list N times (N = 7)
1 step for return statement

Time Complexity = 1 + N + 1 = N + 2
As N becomes large, steps with constant time
have negligible effect on code running time
=> Time Complexity = N

"""


# Logarithmic Time Complexity
# O(log n): logarithmic running time

def power_of_two(a):
    x = 0
    while a > 1:
        a //= 2
        x += 1
    return x

# print(power_of_two(64))

"""
1 step for initialising x = 0
2 * (log2(N)) steps (2 steps in while loop
while loop runs log2(N) times)
1 step to return x

Time Complexity = 2 * log(N) + 2
=> TC = log(N)
"""

def binary_search(array, target, low, high):
    mid = (low + high) // 2
    if low > high:
        return -1
    elif array[mid] == target:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, low, mid - 1)
    else: # target > array[mid]
        return binary_search(array, target, mid + 1, high)


sorted_array = [1,2,4,8,16,32,64,128]

# print(binary_search(sorted_array, 0, 0, len(sorted_array) - 1))
#high = len(array) - 1 because the low is 0
# e.g. 3 elements [0,1,2], max index is A[2] and 2 = 3-1

def iterative_binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target: # target more than midpt
            low = mid + 1
        else: # array[mid] > target
            high = mid - 1
    return -1
            
iterative_array = [1,2,3,4,5,6,7,8]
# print(iterative_binary_search(iterative_array, 8))


#  Log-Linear Time Complexity
# O(Q log n): log-linear running time

# for i in sorted_array:
#     print(binary_search(sorted_array, i, 0, len(sorted_array) - 1))

"""
Running a function with O(log n) Q times (where Q increases linearly as
size of array increases
thus, O(Qlogn)

"""


#  Polynomial Time Complexity
# O(n^c): Polynomial running time (c is a constant)

# A = [1,2,3]
# for i in A:
#     for j in A:
#         print((i,j))

"""
Processing part (print(i,j)) is run N^2 times
thus, O(N^2)

"""

#  Exponential Time Complexity
# O(c^n): Exponential running time (c is a constant being
# raised to a power based on size of input)

def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)
