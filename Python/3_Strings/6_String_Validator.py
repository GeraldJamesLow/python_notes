# https://www.hackerrank.com/challenges/string-validators/problem

#* You are given a string S.
#* Your task is to find out if the string S contains: alphanumeric characters,
#* alphabetical characters, digits, lowercase or uppercase characters.

if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for letter in s:  
        if letter.isalnum():
            alnum = True
        if letter.isalpha():
            alpha = True
        if letter.isdigit():
            digit = True
        if letter.islower():
            lower = True
        if letter.isupper():
            upper = True
    
    print(alnum, alpha, digit, lower, upper, sep='\n')