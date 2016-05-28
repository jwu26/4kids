#!/usr/bin/python
import sys, pygame
from time import sleep
import random
import string


THR = 100
#THR = 200
WOO=[]

def main(argv):
    file_object = open('dic.sql')
    a_asc = ord("a") - 1 # A's ASC11 - 1
    score = 0
    NUM = 0

    for line in file_object:
        #print line
        words = line.split('\',\'')
        #print words[1]
        #words[1] = "abcd"
        for i, ch in enumerate(words[1]):
            if ch == " ":
                #print "quit"
                score = 0
                break;
            score += ord(ch) - a_asc
            #print ord(ch), a_asc, score
        if score == THR:
            #print "Score Of <<< ", words[1], ">>> == ", THR
            WOO.append(words[1])
            NUM += 1
        else:
            #print "Go Ahead!!"
            pass
        score = 0
        
    print WOO
    print "Total Num " , NUM
    file_object.close()
    return

if __name__ == '__main__':
  sys.exit(main(sys.argv))
else:
  print "Import case"

