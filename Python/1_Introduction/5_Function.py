# https://www.hackerrank.com/challenges/write-a-function/problem

#* In the Gregorian calendar, three conditions are used to identify leap years:
#* 
    #* The year can be evenly divided by 4, is a leap year, unless:
        #* The year can be evenly divided by 100, it is NOT a leap year, unless:
            #* The year is also evenly divisible by 400. Then it is a leap year.
#* This means that in the Gregorian calendar, the years 2000 and 2400 are leap years,
#* while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

#* Given a year, determine whether it is a leap year. If it is a leap year, return
#* the Boolean True, otherwise return False.

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
                
    return leap

year = int(input('Year: ')) #? Added input parameter for clarity
print('Is leap year?', is_leap(year)) #? Added output statement to be printed
# Year: 2024
# Is leap year? True