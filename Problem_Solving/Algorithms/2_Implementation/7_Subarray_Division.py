# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
# TODO: Submit on Hackerrank (Site is down / Unable to submit 27/02/2023)

n = 5
numbers = [1, 2, 1, 3, 2]

def birthday(s, d, m):
    # Write your code here
    counter = 0
    if n <= m: #? If len(s) / list size is smaller or equal to segment size
        counter = 1 if sum(s) == d else 0
        return counter
    else:
        for i in range(n-m+1):
            sub_list = s[i:i+m]
            if sum(sub_list) == d:
                counter += 1
    return counter



print(birthday(numbers, 3, 2))