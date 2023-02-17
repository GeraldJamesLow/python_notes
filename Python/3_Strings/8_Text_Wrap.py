# https://www.hackerrank.com/challenges/text-wrap/problem
# https://www.hackerrank.com/challenges/text-wrap/tutorial
# https://www.w3schools.in/python/examples/text-wrapping-in-python

#* You are given a string S and width w.
#* Your task is to wrap the string S into a paragraph of width w.

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)