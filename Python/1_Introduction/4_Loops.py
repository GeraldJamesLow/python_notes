# https://www.hackerrank.com/challenges/python-loops/problem

#* The provided code stub reads an integer, n, from STDIN.
#* For all non-negative integers i < n, print i^2.

if __name__ == '__main__':
    n = int(input('n: ')) #? Added input parameter for clarity
    for number in range(n):
        print(number ** 2) #? number 'raised to the power of' 2