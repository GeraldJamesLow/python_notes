# https://www.hackerrank.com/challenges/kangaroo/problem
#* You are choreographing a circus show with various animals. For one act, you are
#* given two kangaroos on a number line ready to jump in the positive direction
#* (i.e, toward positive infinity).
#* The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
#* The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
#* You have to figure out a way to get both kangaroos at the same location at the same time as part of the show.
#* If it is possible, return YES, otherwise return NO.

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if (x1 < x2 and v1 > v2):
        return 'YES' if ((x2 - x1) / (v1 - v2)) == ((x2 - x1) // (v1 - v2)) else 'NO'
    elif (x2 < x1 and v2 > v1):
        return 'YES' if ((x1 - x2) / (v2 - v1)) == ((x1 - x2) // (v2 - v1)) else 'NO'
    elif (x1 == x2) and (v1 == v2):
        return 'YES'
    else:
        return 'NO'



print(kangaroo(0, 3, 4, 2))
# YES
print(kangaroo(0, 2, 5, 3))
# NO