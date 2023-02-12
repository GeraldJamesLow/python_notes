
#* Function prints a right-aligned staircase of spaces ' ' and hashtags '#'
#* of row length n

def staircase(n):
    # Write your code here
    for row_number in range(1,n + 1):
        print(' '*(n-row_number) + '#'*(row_number))

staircase(4)