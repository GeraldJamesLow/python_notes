
# https://www.hackerrank.com/challenges/apple-and-orange/problem

#* All values lie on the x-axis
#* s = start value (incl) of house relative to origin
#* t = end value (incl) of house relative to origin
#* a = position of apple tree relative to origin
#* b = position of orange tree relative to origin
#* apples = array of final position of dropped apples relative to apple tree
#* oranges = array of final position of dropped oranges relative to orange tree

#? Initial approach

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    a_positions = [x+a for x in apples]
    o_positions = [y+b for y in oranges]
    def withinRange(ar,start,end):
        for fruit_index in range(len(ar)):
            if ar[fruit_index] >= start and ar[fruit_index] <= end:
                ar[fruit_index] = 1
            else:
                ar[fruit_index] = 0
        return sum(ar)
    print(withinRange(a_positions, s, t))
    print(withinRange(o_positions, s, t))


# countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
# 1
# 1

#? Inner function can reference variables in enclosing function as shown below
#? Therefore negating the need of the start, end variables in the inner f(x)

def countApplesAndOranges_two(s, t, a, b, apples, oranges):
    # Write your code here
    a_positions = [x+a for x in apples]
    o_positions = [y+b for y in oranges]
    def withinRange(ar):
        for fruit_index in range(len(ar)):
            if ar[fruit_index] >= s and ar[fruit_index] <= t:
                ar[fruit_index] = 1
            else:
                ar[fruit_index] = 0
        return sum(ar)
    print(withinRange(a_positions))
    print(withinRange(o_positions))


countApplesAndOranges_two(7, 11, 5, 15, [-2, 2, 1], [5, -6])
# 1
# 1