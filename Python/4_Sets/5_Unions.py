# https://www.hackerrank.com/challenges/py-set-union/problem

if __name__ == '__main__':
    en = int(input())
    en_no = set(input().strip().split())
    fr = int(input())
    fr_no = set(input().strip().split())
    
    min_one_sub = en_no.union(fr_no)
    print(len(min_one_sub))