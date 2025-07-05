
# Algorithm for a Palindrome(A palindrome is a word, sentence, verse, or even number that reads the same backward or forward)

def isPalindrome(str):
    startIndex = 0
    endIndex = len(str)-1
    for x in str:
        if str[startIndex]!=str[endIndex]:
            return False
    return True
str = input('\nEnter a string to check if it is Palindrome : ')
print(f'is {str} palindrome ? {isPalindrome(str)}')
