# https://www.hackerrank.com/challenges/python-tuples/problem
# https://docs.python.org/3/library/functions.html#hash
#! Must use Pypy3 language instead of Python 3 as hash returns
#! diff hash values for diff systems / sometimes same systems too

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integers = tuple(integer_list)
    print(hash(integers))