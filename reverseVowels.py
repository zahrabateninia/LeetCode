"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both 
lower and upper cases, more than once.
"""
s = "hello"
vowels = ['a','e','o','u','i']
newS = ''
vowelsOfS= []

for letter in s:
    for vowel in vowels:
        if vowel == letter:
            vowelsOfS += letter
print(vowelsOfS)


