# https://www.hackerrank.com/challenges/py-set-add/problem


if __name__ == '__main__':
    s = set()
    N = int(input())
    for line_no in range(N):
        s.add(input().strip())
    print(len(s))

# Input
# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France 

# Output
# 5