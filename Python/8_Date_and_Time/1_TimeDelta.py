# https://www.hackerrank.com/challenges/python-time-delta/problem
#TODO This problem

a = 'Sun 10 May 2015 01:00:40 -0200'
b = 'Sun 10 May 2015 13:54:36 -0000'


def time_delta(t1, t2):
    def epochCalc(time):
        epoch_year = (int(time[11:16]) - 1970) * 365 * 24 * 60 * 60

        match time[7:10]:
            case 'Jan':
                epoch_month = 0
            case 'May':
                pass
        
        if time[-5] == '-': #? e.g. -0700
            epoch_hour = (int(time[-14:-12]) - int(time[-4:-2])) * 60 * 60
            epoch_minute = (int(time[-11:-9]) - int(time[-2:])) * 60

        else: #? e.g. +0700
            epoch_hour = (int(time[-14:-12]) + int(time[-4:-2])) * 60 * 60
            epoch_minute = (int(time[-11:-9]) + int(time[-2:])) * 60


        epoch_second = (int(time[-8:-6]))
        print(epoch_year, epoch_hour, epoch_minute, epoch_second)
        

        

    
    epochCalc(t1)
        
        

time_delta(a, b)