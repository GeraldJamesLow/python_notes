# https://www.hackerrank.com/challenges/merge-the-tools/problem
#* Given:
    #* string = string to be modified
    #* k = integer representing subsize (size of each subelement)

#* Print each substring on a separate line such that in each
#* substring, there is no duplicate character present


def merge_the_tools(string, k):
    # your code goes here
    split_str = [string[i:i+k] for i in range(0,len(string), k)]

    for i in range(len(split_str)):

        # try: #? try error block for troubleshooting
        #     print('used_char:', used_char)
        # except UnboundLocalError:
        #     used_char = None

        new_str = []
        used_char = []
        for j in range(k):
            if split_str[i][j] in used_char:
                continue
            else:
                new_str.append(split_str[i][j])
                used_char.append(split_str[i][j])

        new_str = ''.join(new_str)
        split_str[i] = new_str
        print(split_str[i])



if __name__ == '__main__':
    string, k = 'AAABCADDE', 3
    merge_the_tools(string, k)