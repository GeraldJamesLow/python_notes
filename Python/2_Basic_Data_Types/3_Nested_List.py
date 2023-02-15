# https://www.hackerrank.com/challenges/nested-list/problem
#* Given the names and grades for each student in a class of N students, store them
#* in a nested list and print the name(s) of any student(s) having the second lowest
#* grade.

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        entry = [name, score]
        records.append(entry)
    
    records = sorted(records, key= lambda x: (x[1], x[0]))
    
    lowest_grade = records[0][1]
    records = [record for record in records if record[1] != lowest_grade]

    lowest_grade = records[0][1]
    records = [record for record in records if record[1] == lowest_grade]
    for name, score in records:
        print(name)