# https://www.hackerrank.com/challenges/the-minion-game/problem

#* Both players are given the same string, S.
#* Both players have to make substrings using the letters of the string S.
    #* Stuart has to make words starting with consonants.
    #* Kevin has to make words starting with vowels.
#* The game ends when both players have made all possible substrings.
#* A player gets +1 point for each occurrence of the substring in the string S.

#? Words formed from string[index] = len(string) - index
#? B: 6 word(s) B, BA, BAN, BANA, BANAN, BANANA
#? A: 5 word(s) A, AN, ANA, ANAN, ANANA
#? N: 4 Word(s) N, NA, NAN, NANA
#? A: 3 Word(s) A, AN, ANA
#? N: 2 Word(s) N, NA
#? A: 1 Word(s) A



def minion_game(string):
    # your code goes here
    st = 0
    ke = 0
    
    for i in range(len(string)):
        if string[i].upper() in 'AEIOU':
            ke += len(string) - i
        else:
            st += len(string) - i
            
    if st == ke:
        print('Draw')
    elif st > ke:
        print('Stuart', st)
    else:
        print('Kevin', ke)

    
    
minion_game('BAANANA')
