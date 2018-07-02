# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:17:03 2018

@author: hinson

Give me a word with three consecutive double letters. I’ll give you a couple of words
that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-ip-p-i.
If you could take out those i’s it would work. But there is a word that has three
consecutive pairs of letters and to the best of my knowledge this may be the only word.
Of course there are probably 500 more but I can only think of one. What is the word?

"""

with open('words.txt', 'r') as fd:
    word_list = fd.read().split()
    
    
def is_trip_pair(wordList):
    for word in wordList:
        i = 0
        pairCount = 0
        while i < len(word) - 1:
            if word[i] == word[i + 1]:
                pairCount += 1
                if pairCount == 3:
                    print(word)
                i += 2
            else:
                pairCount = 0
                i += 1

is_trip_pair(word_list)
