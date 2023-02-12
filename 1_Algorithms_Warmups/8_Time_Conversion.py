
#* convert time from 12 hour to 24 hour time

c = '07:05:45PM'
d = '12:05:45PM'

def timeConversion(s):
    # Write your code here
    if s[-2:] == 'AM': #? If last two characters are AM
        if s[:2] == '12':
            return '00' + s[2:-2]
        else:
            return s[:-2]
    else: #? If last two characters are PM
        if s[:2] == '12': #? e.g. 12.07pm
            return s[:-2]
        else:     
            hour = str(int(s[:2]) + 12)
            return hour + s[2:-2]

print(timeConversion(c))
# 19:05:45
print(timeConversion(d))
# 12:05:45