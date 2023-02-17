# https://www.hackerrank.com/challenges/designer-door-mat/problem
#* Mr. Vincent works in a door mat manufacturing company.
#* One day, he designed a new door mat with the following specifications:
    #* Mat size must be N X M. ( N is an odd natural number, and M is 3 times N.)
    #* The design should have 'WELCOME' written in the center.
    #* The design pattern should only use |, . and - characters.



if __name__ == '__main__':
    values = input('N M: ').strip().split()
    n = int(values[0])
    m = int(values[1])
    dot_pattern = '.|.'
    #? Top Triangle
    for i in range((n - 1) // 2):
        print((dot_pattern * (i * 2 + 1)).center(m, '-'))
    
    #? WELCOME
    print('WELCOME'.center(m, '-'))
    
    #? Bottom Triangle
    for i in range(((n - 1) // 2) - 1, -1, -1):
        print((dot_pattern * (i * 2 + 1)).center(m, '-'))