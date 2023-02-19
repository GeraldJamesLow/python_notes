# https://www.hackerrank.com/challenges/capitalize/problem
#* You are asked to ensure that the first and last names of people begin with
#* a capital letter in their passports. For example, alison heck should be
#* capitalised correctly as Alison Heck.
#* Note: in a word only the first character is capitalized. Example 12abc
#* when capitalized remains 12abc.

a = '1 w 2 r 3g'
b = 'hello   world  lol'

def solve(s):
    for word in s.split():
        s = s.replace(word, word.capitalize())

    return s

print(solve(b))