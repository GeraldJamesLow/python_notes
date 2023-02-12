
#* Given five positive integers, find the minimum and maximum values that can be calculated by summing
#* exactly four of the five integers. Then print the respective minimum and maximum values as a single
#* line of two space-separated long integers.

a = [501893267, 649027153, 379408215, 452968170, 487530619]

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min_value = sum(arr[:4])
    max_value = sum(arr[1:])
    print(min_value, max_value)

miniMaxSum(a)

# 1821800271 2091419209

#* syntax
#* arr[start_value(incl):end_value(excl):step]
#! remember that indexing starts at 0