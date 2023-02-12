
#* Compare two lists of equal length

Alice = [1,3,2]
Bob = [2,3,1]
def compareTriplets(a, b):
    # Write your code here
    a_counter = 0
    b_counter = 0
    if len(a) == len(b):
        for number in range(len(a)):
            if a[number] > b[number]:
                a_counter += 1
            elif a[number] < b[number]:
                b_counter += 1
            else:
                continue
    return [a_counter, b_counter]

#* Alternative using zip(a,b) function which returns [(a[0],b[0]), (a[1,b[1]),...]

def compareTripletsZip(a, b):
    # Write your code here
    a_counter = 0
    b_counter = 0
    zipped_list = zip(a,b)
    for element in zipped_list:
        if element[0] > element[1]:
            a_counter += 1
        elif element[0] < element[1]:
            b_counter += 1
        else:
            continue
    return [a_counter,b_counter]

print(compareTriplets(Alice,Bob))
print(compareTripletsZip(Alice,Bob))
# [1,1]