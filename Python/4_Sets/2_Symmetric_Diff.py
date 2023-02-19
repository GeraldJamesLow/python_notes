
#* Output the symmetric difference integers in ascending order, one per line.

if __name__ == '__main__':
    def str_to_set(s):
        s = s.split(' ')
        s = set(s)
        return s
    
    m = int(input('m: '))
    m_set = str_to_set(input('m values: '))
    n = int(input('n: '))
    n_set = str_to_set(input('n values: '))

    symmetric_diff = list(m_set.symmetric_difference(n_set))
    symmetric_diff = list(map(int,symmetric_diff))
    symmetric_diff.sort()
    for number in symmetric_diff:
        print(number)

# Input
# 4
# 2 4 5 9
# 4
# 2 4 11 12

# Output
# 5
# 9
# 11
# 12