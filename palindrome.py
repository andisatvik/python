# Check if a word is palindrome

word = input("Enter word to check: ")

if(word == word[::-1]):
    print(word + " is a Palindrome")
else:
    print(word + " is not a Palindrome")
