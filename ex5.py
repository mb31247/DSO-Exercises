''''
Ask the user for a string and print out
whether this string is a palindrome or not.
(A palindrome is a string that reads the same
forwards and backwards.)
'''

word_random = input("Enter a random word: ")
word_random = str(word_random)
word_reversed = word_random[::-1]
print(word_reversed)

if word_random == word_reversed:
    print("Your word is a palindrome!")
else:
    print("Your word is NOT a palindrome!")