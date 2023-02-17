# https://www.hackerrank.com/challenges/python-string-formatting/problem
# https://www.w3schools.com/python/ref_string_format.asp


def print_formatted(number):
    # your code goes here
    width = len('{:b}'.format(number))

    for i in range(1, number + 1):
        i_dec = str(i)
        i_oct = '{:o}'.format(i)
        i_hex = '{:X}'.format(i)
        i_bin = '{:b}'.format(i)
        print(i_dec.rjust(width, ' ') , i_oct.rjust(width, ' ') , i_hex.rjust(width, ' ') , i_bin.rjust(width, ' '))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)