
#* HackerLand University has the following grading policy:
#* Every student receives a grade in the inclusive range from 0 to 100.
#* Any grade less than 40 is a failing grade.
#* Sam is a professor at the university and likes to round each student's grades according to these rules:
#* If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
#* If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.


a = [73, 67, 38, 33]

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] < 38:
            continue
        else:
            if grades[i] % 5 < 3: #? If remainder (modulo) of division by 5 is less than 3
                continue
            else:
                grades[i] = (grades[i] // 5) * 5 + 5 #? grade = floor divisor (result rounded down to nearest integer)
    return grades                                    #? of grades divided by 5 multiplied by 5 and add 5

print(gradingStudents(a))
# [75, 67, 40, 33]