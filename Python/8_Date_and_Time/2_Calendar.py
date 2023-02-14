# https://www.hackerrank.com/challenges/calendar-module/problem
# https://docs.python.org/3/library/calendar.html

#* You are given a date as a string in 'MM DD YYYY' format.
#* Your task is to find what the day is on that date.

import calendar

#? Initial approach

# ''if __name__ == '__main__':
#     text = input('Date: ').strip()
#     date_day = []
#     year = int(text[-4:])
#     month = int(text[:2])
#     day = int(text[3:5])
#     cal = calendar.Calendar()
#     for i in cal.itermonthdays2(year, month):
#         if i[0] == 0:
#             continue
#         else:
#             date_day.append(i)
    
#     day_of_week = date_day[day - 1][1]
    
#     if day_of_week == 0:
#         print("MONDAY")
#     elif day_of_week == 1:
#         print('TUESDAY')
#     elif day_of_week == 2:
#         print('WEDNESDAY')
#     elif day_of_week == 3:
#         print('THURSDAY')
#     elif day_of_week == 4:
#         print('FRIDAY')
#     elif day_of_week == 5:
#         print('SATURDAY')
#     elif day_of_week == 6:
#         print('SUNDAY')

#? Shorter code with more relevant, compact methods

if __name__ == '__main__':
    text = input('Date: ').strip()
    date_list = text.split()
    day = calendar.weekday(int(date_list[2]), int(date_list[0]), int(date_list[1]))
    day = calendar.day_name[day]
    print(day.upper())