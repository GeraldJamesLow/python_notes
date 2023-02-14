# https://www.hackerrank.com/challenges/python-time-delta/problem
# https://www.w3schools.com/python/python_datetime.asp

#* You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
#* 
#* Day dd Mon yyyy hh:mm:ss +xxxx
#* 
#* Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.


from datetime import datetime
#? So that methods can be datetime.method()
#? If not methods need to be datetime.datetime.method()

a = 'Sat 24 Mar 2170 03:47:07 +0430'
b = 'Mon 30 Dec 2272 20:27:41 -1000'

def time_delta(t1, t2):
    t1 = datetime.timestamp(datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')) #? Check second link for reference
    t2 = datetime.timestamp(datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')) #? strptime() creates a datetime object
    return(str(abs(int(t1 - t2))))                                            #? timestamp() gets the seconds since epoch
                                                                              #? Epoch is 01/01/1970 00:00:00 UTC

print(time_delta(a, b))
# 3243222634