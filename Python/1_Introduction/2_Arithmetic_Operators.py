# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
#* The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

    #* The first line contains the sum of the two numbers.
    #* The second line contains the difference of the two numbers (first - second).
    #* The third line contains the product of the two numbers.

#? Added input parameter for a and b below for clarity

if __name__ == '__main__':
    a = int(input('a: ')) 
    b = int(input('b: '))
    print(a + b)
    print(a - b)
    print(a * b)