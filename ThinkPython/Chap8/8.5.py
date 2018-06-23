# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 09:49:06 2018

@author: hinson

A Caesar cypher is a weak form of encryption that involves “rotating” each letter by
a fixed number of places. To rotate a letter means to shift it through the alphabet, wrapping around
to the beginning if necessary, so ’A’ rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’.
To rotate a word, rotate each letter by the same amount. For example, “cheer” rotated by 7 is “jolly”
and “melon” rotated by -10 is “cubed”. In the movie 2001: A Space Odyssey, the ship computer
is called HAL, which is IBM rotated by -1.
Write a function called rotate_word that takes a string and an integer as parameters, and returns
a new string that contains the letters from the original string rotated by the given amount.
You might want to use the built-in function ord, which converts a character to a numeric code, and
8.13. Exercises 81
chr, which converts numeric codes to characters. Letters of the alphabet are encoded in alphabetical
order, so for example:
>>> ord('c') - ord('a')
2
Because 'c' is the two-eth letter of the alphabet. But beware: the numeric codes for upper case
letters are different.


"""

def make_letter_fit_numeric_signature(letterSignature: int, lowerBound: int, upperBound: int) -> int:
    while letterSignature > upperBound:
        letterSignature -= 26
        
    while letterSignature < lowerBound:
        letterSignature += 26
        
    return letterSignature

def rotate_word(word: str, integerToRotateBy: int):
    rotatedWord = ''
    for letter in word:
        if letter.islower():
            rotatedWord += chr(make_letter_fit_numeric_signature(ord(letter) + integerToRotateBy, 97, 122))
        else:
            rotatedWord += chr(make_letter_fit_numeric_signature(ord(letter) + integerToRotateBy, 65, 90))
    print(rotatedWord)
            
        
rotate_word('AbZ', -30)
