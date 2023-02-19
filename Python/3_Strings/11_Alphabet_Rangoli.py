# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
# https://stackoverflow.com/questions/23199733/convert-numbers-into-corresponding-letter-using-python


def print_rangoli(size):
    # your code goes here

    if size == 1:
        print('a')
    else:
        width = (size * 2 - 1) * 2 - 1
        row_pattern = [chr(ord('`') + size)]

        def prevLetters(num_before_initial):
            return chr(ord(row_pattern[0]) - num_before_initial)
        
        #? First Line
        print(chr(ord('`') + size).center(width, '-'))

        #? Second to Middle Line
        for i in range(1, size):
            reversed_row = [element for element in row_pattern]
            reversed_row.reverse()
            row_pattern.append(prevLetters(i))
            final_pattern = row_pattern + reversed_row
            final_pattern = '-'.join(final_pattern)
            print(final_pattern.center(width, '-'))

        #? Mid + 1 to Second Last Line
        for j in range(size-1, 1, -1):
            final_pattern = final_pattern.split('-')
            final_pattern.pop(j-1)
            final_pattern.pop(j-1)
            final_pattern = '-'.join(final_pattern)
            print(final_pattern.center(width, '-'))

        #? Last Line
        print(chr(ord('`') + size).center(width, '-'))


    
print_rangoli(3)


#? ord('unicode_character') gets the corresponding integer to the unicode character
#? chr('int') gets the corresponding unicode character to the integer
def numToLetter(letter_number):
    #? return (Big Letter, Small Letter)
    return (chr(ord('@') + letter_number), chr(ord('`') + letter_number))


# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)

#? Compact solution from hackerrank
def sol(n):
    for i in range(n):
        s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
        print((s+s[::-1][1:]).center(n*4-3, '-'))

    for i in range(n-1):
        s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
        print((s+s[::-1][1:]).center(n*4-3, '-'))

# sol(4)


#? to check the actual output of the compact solution
def ababa(a):
    for i in range(a):
        s = "-".join(chr(ord('a')+a-j-1) for j in range(i+1))
        print(s, s[::-1][1:])

# ababa(4)