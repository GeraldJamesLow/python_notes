# https://www.hackerrank.com/challenges/python-division/problem
#* The provided code stub reads two integers, a and b, from STDIN.
#* 
#* Add logic to print two lines. 
#* The first line should contain the result of integer division, a // b.
#* The second line should contain the result of float division, a / b.
#* No rounding or formatting is necessary.

#? Added input parameter for a and b below for clarity

if __name__ == '__main__':
    a = int(input('a: '))
    b = int(input('b: '))
    print(a // b)
    print(a / b)
