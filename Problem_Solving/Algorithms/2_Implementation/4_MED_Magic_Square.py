# https://www.hackerrank.com/challenges/magic-square-forming
# https://en.wikipedia.org/wiki/Magic_square#For_any_magic_square

#* We define a magic square to be a n x n matrix of distinct positive integers from 
#* 1 to n^2 where the sum of any row, column, or diagonal of length n is always equal
#* to the same number: the magic constant. You will be given a 3x3 matrix of integers
#* in the inclusive range [1,9]. We can convert any digit a to any other digit b in the
#* range [1,9] at cost of |a - b|. Given s, convert it into a magic square at minimal
#* cost. Print this cost on a new line.

#* Note: The resulting magic square must contain distinct integers in the inclusive
#* range [1-9].

#? Magic constant is 15 for 3x3 grid

initial = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 5]
]


def formingMagicSquare(s):
    # Write your code here
    def subtractArray(ar1, ar2): #? Inner function to subtract two arrays and
        array_difference = []    #? Sum the absolute value of the differences
        difference_counter = 0
        for element in list(zip(ar1, ar2)):
            array_difference.append([element[0][i] - element[1][i] for i in range(3)])
        
        for element in array_difference:
            for i in range(len(element)):
                element[i] = abs(element[i])
                difference_counter += element[i]
        
        return difference_counter
    
    def rotate(original): #? Inner function to rotate 2D array by 90 degrees clockwise
        return list(zip(*original[::-1]))
    
    #? There are 8 trivially distinct squares which can be formed from range [1-9] when
    #? all integers are distinct.
    #? The below code accounts for one such instance and its mirror, and the rest of the
    #? squares can be accessed by rotating 1-3 times in the same direction
    arr1 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    arr2 = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]

    def rotateSubtract(a):
        smallest_difference = subtractArray(a, s)
        for i in range(3):
            a = rotate(a)
            diff_to_compare = subtractArray(a,s)
            smallest_difference = min(smallest_difference, diff_to_compare)
        return smallest_difference
    
    return min(rotateSubtract(arr1), rotateSubtract(arr2)) #? Return smallest difference

print(formingMagicSquare(initial))
# 1

#? Subtract array without numpy

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] ]

b = [
    [4, 4, 4],
    [4, 4, 4],
    [4, 4, 4]
]

def subtractArray(ar1, ar2):
    array_difference = []
    difference_counter = 0
    for element in list(zip(ar1, ar2)):
        array_difference.append([element[0][i] - element[1][i] for i in range(3)])
    
    for element in array_difference:
        for i in range(len(element)):
            element[i] = abs(element[i])
            difference_counter += element[i]
    print(array_difference)
    
    return difference_counter

# print(subtractArray(a,b))
# 21

#? Rotate 2D Array
# https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
def rotate(original):
    return list(zip(*original[::-1]))

# print(rotate(a))
# [(7, 4, 1), (8, 5, 2), (9, 6, 3)]