
#* Print ratio of positive/negative/zero numbers to total no. of numbers (elements in list)
#* in that order

a = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
    # Write your code here
    element_count = len(arr)
    plus_counter = 0
    minus_counter = 0
    zero_counter = 0
    for element in arr:
        if element > 0:
            plus_counter += 1
        elif element < 0:
            minus_counter += 1
        else:
            zero_counter += 1
    print(plus_counter / element_count)
    print(minus_counter / element_count)
    print(zero_counter / element_count)

plusMinus(a)
# 0.5
# 0.3333333333333333
# 0.16666666666666666