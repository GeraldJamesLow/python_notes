
#* Given the participants' score sheet for your University Sports Day,
#* you are required to find the runner-up score. You are given n scores.
#* Store them in a list and find the score of the runner-up.
#* The first line contains n. The second line contains an array A[] of
#* n integers each separated by a space.
# 5
# 2 3 6 6 5

if __name__ == '__main__':
    n = int(input('no. of scores: '))
    arr = map(int, input('scores sep by space: ').split())
    arr = list(arr)
    unique_arr = list(dict.fromkeys(arr))
    unique_arr.sort()
    print(unique_arr[-2])