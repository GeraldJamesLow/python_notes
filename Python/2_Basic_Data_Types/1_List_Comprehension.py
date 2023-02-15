# https://www.hackerrank.com/challenges/list-comprehensions/problem
# https://pythonexamples.org/python-list-comprehension-two-lists/
#* You are given three integers x, y and z representing the dimensions of a cuboid
#* along with an integer n. Print a list of all possible coordinates given by (i,j,k)
#* on a 3D grid where the sum of i + j + k is not equal to n. 
#* Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z.
#* Please use list comprehensions rather than multiple loops, as a learning exercise.
#* Print the list in lexicographic increasing order.


if __name__ == '__main__':
    x = int(input('x: '))
    y = int(input('y: '))
    z = int(input('z: '))
    n = int(input('n: '))
    
    def zeroToVar(var):
        var = [num for num in range(var + 1)]
        return var
    
    x = zeroToVar(x)
    y = zeroToVar(y)
    z = zeroToVar(z)
    
    arr = [[a,b,c] for a in x for b in y for c in z]
    filtered_arr = [element for element in arr if sum(element) != n]

    print(filtered_arr)
    