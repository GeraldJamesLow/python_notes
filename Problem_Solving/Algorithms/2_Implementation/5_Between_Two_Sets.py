
#* There will be two arrays of integers. Determine all integers that satisfy the following two conditions:
#*  1. The elements of the first array are all factors of the integer being considered
#*  2. The integer being considered is a factor of all elements of the second array

#* These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

a1 = [2, 3, 6]
b1 = [42, 84]


def getTotalX(a, b):

    initial_numbers = list(range(max(a), min(b)+1))
    for i in range(len(initial_numbers)):
        for j in range(len(a)):
            if initial_numbers[i] % a[j] != 0:
                initial_numbers[i] = 0
                continue

    if 0 in initial_numbers:
        initial_numbers = list(set(initial_numbers))[1:]
    else:
        initial_numbers = list(set(initial_numbers))

    print('first loop results:',initial_numbers) #? for troubleshooting


    for i in range(len(initial_numbers)):
        for j in range(len(b)):
            if b[j] % initial_numbers[i] != 0:
                initial_numbers[i] = 0
                break

    if 0 in initial_numbers:
        initial_numbers = list(set(initial_numbers))[1:]
    else:
        initial_numbers = list(set(initial_numbers))

    print('second loop results:',initial_numbers) #? for troubleshooting
    
    return len(initial_numbers)


# print(getTotalX(a1,b1))
# first loop results: [36, 6, 42, 12, 18, 24, 30]
# second loop results: [42, 6]
# 2

#? More elegant, compact solution below

def getTotalX_two(a, b):
    # Write your code here
    factors = []
    for i in range(a[-1], b[0]+1):
        #? if ((number % element == 0) for all element in a) and
        #?    ((element % number == 0) for all element in b)
        if all(i % x == 0 for x in a) and all( x % i == 0 for x in b):
            factors.append(i)
    print(factors) #? for troubleshooting
    return len(factors)

print(getTotalX_two(a1,b1))