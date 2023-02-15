# https://www.hackerrank.com/challenges/python-string-split-and-join/problem
#* You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    # write your code here
    split_text = line.split(' ')
    joined_text = '-'.join(split_text)
    return joined_text

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)