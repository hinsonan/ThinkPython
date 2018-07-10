# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 10:52:20 2018

@author: hinson

Write a function called sed that takes as arguments a pattern string, a replacement
string, and two filenames; it should read the first file and write the contents into the second file
(creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced
with the replacement string.
If an error occurs while opening, reading, writing or closing files, your program should catch the
exception, print an error message, and exit
"""

def sed(patternString, replacementString, fin, fout):
    
    inputFile = open(fin)
    
    outputFile = open(fout, 'w')
    
    for line in inputFile:
        if patternString in line:
            newString = line.replace(patternString, replacementString)
            outputFile.write(newString)
        else:
            outputFile.write(line)
    
    inputFile.close()
    outputFile.close()
            
def main():
    fileOne = 'input.txt'
    fileTwo = 'output.txt'
    sed('dog', 'cat', fileOne, fileTwo)
    
main()