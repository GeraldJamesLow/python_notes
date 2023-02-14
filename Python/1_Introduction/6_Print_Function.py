# https://www.hackerrank.com/challenges/python-print/problem
#* The included code stub will read an integer, n, from STDIN.
#* 
#* Without using any string methods, try to print the following:
#* 123...n
#* Note that "..." represents the consecutive values in between.




if __name__ == '__main__':
    n = int(input('number: ')) #? Added input parameter for clarity
    numbers = [i for i in range(1, n+1)]
    print(*numbers, sep='') #? Print all elements in the list 'numbers' on a single line
                            #? With separation '' (no separation)
                            #? Alternatively, you can print with sep='\n' for newline after each element