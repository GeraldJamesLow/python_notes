# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
#* Given an array, return average (sum of distinct val / number of distinct val)

ar = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]

def average(array):
    # your code goes here
    tree_set = set(array)
    total_height = sum(tree_set)
    distinct_tree = len(tree_set)
    return round(total_height / distinct_tree, 3)

print(average(ar))
# 169.375