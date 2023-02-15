# https://www.hackerrank.com/challenges/python-lists/problem
#* The first line contains an integer, n, denoting the number of commands.
#* Each line i of the n subsequent lines contains one of the commands described above.
#* Iterate through each command in order and perform the corresponding operation on your list.


#? Can't use match case on hackerrank, replaced with if elif statement
if __name__ == '__main__':
    numbers = []
    N = int(input())
    for _ in range(N):
        command, *values = input().split()
        values = list(map(int, values))

        if command == 'insert':
            numbers.insert(values[0], values[1]) #? Insert (second value)) at index (first value)
        elif command == 'print':
            print(numbers)
        elif command == 'remove':
            if values[0] in numbers:
                numbers.remove(values[0])
        elif command == 'append':
            numbers.append(values[0])
        elif command == 'sort':
            numbers.sort()
        elif command == 'pop':
            numbers.pop()
        elif command == 'reverse':
            numbers.reverse()