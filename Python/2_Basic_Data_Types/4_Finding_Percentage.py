# https://www.hackerrank.com/challenges/finding-the-percentage/problem
# https://www.w3schools.com/python/ref_string_format.asp#:~:text=The%20format()%20method%20formats,method%20returns%20the%20formatted%20string.
#*The provided code stub will read in a dictionary containing key/value pairs
#* of name:[marks] for a list of students. Print the average of the marks array
#* for the student name provided, showing 2 places after the decimal.


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    score_list = student_marks.get(query_name)
    total_score = sum(score_list)
    no_of_scores = len(score_list)
    avg_score = '{:.2f}'.format(total_score / no_of_scores)
    print(avg_score)