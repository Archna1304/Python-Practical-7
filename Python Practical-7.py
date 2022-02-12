""" Id : 20CE157 
Name : Archana Vyas

Git repository:

Aim: Lapindrome is defined as a string which when split in the middle, 
gives two halves having the same characters and same frequency of each character. 
If there are odd number of characters in the string, we ignore the middle character 
and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga 
have the same characters with same frequency. Also, abccab, rotor and xyzxy are a 
few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain 
the same characters but their frequencies do not match. Your task is simple. Given a string, 
you need to tell if it is a lapindrome."""


# Practical-6
# user input number of test case
testCases = int(input())
while testCases:
    testCases -= 1
    string = input()        # input is already in string format so no need to type-cast
    l = len(string)
    half = len(string) // 2
    # check whether length divisible by two or not if yes divde the strong in two halves
    if len(string) % 2 == 0:
        # comparing two half divided strings
        if sorted(string[:half]) == sorted(string[half:]):
            print('YES')
        else:
            print('NO')
    else:
        if sorted(string[:half]) == sorted(string[half + 1:]):
            print('YES')
        else:
            print('NO')
