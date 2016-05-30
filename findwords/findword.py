#!/usr/bin/python
import sys, pygame
from time import sleep
import random
import string


THR = 100
#THR = 200
WOO=[]
LINE=False
#LINE=True

def main(argv):
    file_object = open('dic.sql')
    a_asc = ord("a") - 1 # A's ASC11 - 1
    score = 0
    NUM = 0
    sc = "-"

    print "\n\n\t ======== Find Score == 100 Words In All 36673 " 

    for line in file_object:
        words = line.split('\',\'')
        #print words[1]
        for i, ch in enumerate(words[1]):
            if ch == " " or ch == "-":
                score = 0
                break;
            score += ord(ch) - a_asc
            #print ord(ch), a_asc, score
        if score == THR:
            #print "Score Of <<< ", words[1], ">>> == ", THR
            if words[1][0] != sc:
                sc = words[1][0]
                print "\n\"%c\": %d" %(sc,ord(sc) - a_asc)
            print words[1],

            WOO.append(words[1])
            NUM += 1
        else:
            #print "Go Ahead!!"
            pass
        score = 0

    print "\n\n\t ======== Find Score == 100 Words (%d) In 36673 " % NUM
    #print WOO
    if LINE == True:
        #print words as line
        i = 0
        for w in range((len(WOO)+7)/8):
           #print w
           print  w + 1,":" , WOO[8*w:8*(w+1)]

    file_object.close()

    return

if __name__ == '__main__':
  sys.exit(main(sys.argv))
else:
  print "Import case"

