# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 12:58:42 2018

@author: hinson
"""

def all_anagrams(wordlist):
    d=dict()
    for word in wordlist:
        a=list(word)
        a.sort()
        a=tuple(a)
        d[a]=d.get(a,[])+[word]
    return d

def stored_anagrams(d):
    a=raw_input('read or write? ')
    import pickle
    if a == 'write':
        f=open('anagram.db','w')
        f.write(pickle.dumps(d))
    elif a=='read':
        f=open('anagram.db')
        s=''.join(f.readlines())
        s=pickle.loads(s)
        for x in s:
            d[x]=s[x]
    f.close()


def read_anagrams(word,d='a'):
    import pickle
    if type(word)!=str:
        return 'only strings please'
    if d=='a':
        f=open('anagram.db')
        s=''.join(f.readlines())
        d=pickle.loads(s)
    letters=list(word)
    letters.sort()
    try:
        anagrams=d[tuple(letters)][:]
        anagrams.remove(word)
    except:
        return "sorry %s not a word" % word
    return anagrams