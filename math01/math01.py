#!/usr/bin/python
import sys, pygame
from time import sleep
from pygame import key
import random
import string
from pygame.locals import *
import thread, time

#SIZE='tiny'
#SIZE='large'
SIZE='long'
SPEED=0.3
ERROR=0
RANGE_MIN=1
RANGE_MAX=50  #10 -  RANGE
STAT={  "error":0,
        "right":0,
        "score":0,
        "total":0
      }
RES={
        "tiny": {
            'w': 320,
            'h': 240
            },
        "small": {
            'w': 640,
            'h': 480
            },
        "large": {
            'w': 800,
            'h': 640
            },

        "long": {
            'w': 1020,
            'h': 400
            },
        }
#WIDTH = 640
#HEIGHT = 360
white = (255,255,255)
black = (0, 0, 0)
misc = (88, 181, 88)

sym = [" + "," - "]

pygame.init()

#load picture
#ball = pygame.image.load("ball.bmp")
img = pygame.image.load("./images/ball.jpeg")
score_panel=pygame.image.load("./images/score_panel.png")

def load_audio(wav):
    tmp=pygame.mixer.Sound(wav)
    tmp.set_volume(1)
    return tmp

#load audio
pygame.mixer.init()
grape = load_audio("audio/grape.wav")
low = load_audio("audio/low.wav")
high = load_audio("audio/high.wav")
pants = load_audio("audio/pants.wav")

class _Paint_(object):
    '''
    basic painting class
    '''
    def __init__(self, screen, name):
        self.font = pygame.font.Font(None, 40)
        self.screen = screen
        self.text = self.font.render(name, 1, misc)
        return

    def __background__(self, screen, img):
        imgrect = img.get_rect()
        screen.fill(black)
        screen.blit(img, imgrect)
        pygame.display.flip()
        return

    def __text__(self, font , text, location):
        self.text = self.font.render(text, 1, misc)
        self.screen.blit(self.text, location)
        pygame.display.flip()

    # Draw clock
    def __clock__(self):
        font = pygame.font.Font(None, 24)
        stat_text = "Right/Error: <" + str(STAT['right']) + "/" + str(STAT['error']) + "> Clock: <"+ str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2)+ ">"
        #stat_text = str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2)
        survivedtext = font.render(stat_text, True, black)
        #survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, black)
        self.screen.blit(survivedtext, (RES[SIZE]['w'] - 240, RES[SIZE]['h'] - 30))
        pygame.display.flip()

    def __HUD__(self):
        #draw the background for the bottom:
        self.screen.blit(score_panel, [0, RES[SIZE]['h'] - 60])
        self.__clock__()

    def __del__(self):
        #print "bye! "+ str(self.name)
        return

class _Equation_(_Paint_):
  '''Title
  Equation in 0 - 100
  Description'''
  def __init__(self, screen, name):
    super(_Equation_, self).__init__(screen, name)
    self.name = str(name)
    self.position = (0,0)
    #self.font = pygame.font.Font(None, 40)
    #self.screen = screen
    #self.text = self.font.render(self.name, 1, misc)
    super(_Equation_, self).__background__(screen, img)
    #print "Alphabel Name: " + self.name +" x.y : %d.%d" % self.position

  def __del__(self):
    super(_Equation_, self).__del__()
    #print "bye! "+ str(self.name)
    return

  def __setPosition__(value):
    print "set position: " % value
    self.position = value

  def __fallOne__(self, horiz ,line):
    #print "line : %d"% line
    #self.screen.fill(black)
    self.screen.blit(self.text, (horiz,line*4))
    pygame.display.flip()

def getEquation():
    print "get random equation in 0- ", RANGE_MAX
    x = random.randint(RANGE_MIN, RANGE_MAX)
    y = random.randint(RANGE_MIN, RANGE_MAX)
    s = sym[random.randint(33, 99)%2]
    fm = str(x) + s + str(y) + " = "
    if s == sym[1]:
        #print "minus"
      if x < y:
        fm = str(y) + s + str(x) + " = "
        value = y - x
      else:
        value = x - y
    else:
        #print "add"
        value = x + y
    STAT['total'] += 1
    return fm,value

def PaintEquation(screen, equation, horiz,line):
  #check if to get a new Symbol
  Four = _Equation_(screen, equation)
  Four.__fallOne__(horiz,line)
  #print horiz,line
  Four.__clock__()
  #Four.__HUD__()

class _GetInputs_:
    '''
    handle num inputs
    '''
    def __init__(self):
        self.name = ""
        self.number = 0
        self.end = False
        self.paused = 0
        return

    def __set__(self, name, number, end):
        self.name = name
        self.number = number
        self.end = end
        return
    def __reset__(self):
        self.__set__("", 0, False)
        return
    def __show__(self):
        #print "---> ", self.name, "---> ", self.number, " ---> ", self.end
        return

    def __getInput__(self):
        #print "id ", inp
        '''
        input numbers and paused
        '''
        name = self.name
        number = self.number
        end = self.end
        for event in pygame.event.get():
            #print "Get Key : %s "% event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #print "pressed: %s" % event.dict['unicode']
                name = event.dict['unicode']
                if event.unicode.isalpha():
                    name += event.unicode
                elif event.unicode.isdigit():
                    number = number*10 + int(event.unicode)
                    #print "uni code: " , int(event.unicode)
                elif event.key == K_BACKSPACE:
                    name = self.name[:-1]
                elif event.key == K_SPACE:
                    self.__reset__()
                    self.paused ^= 1
                    print "SPACE"
                elif event.key == K_RETURN:
                    name = ""
                    end = True

        self.__set__(name, number, end)
        return name, number, end

    def __del__(self):
        return

def main(argv):

    size = width, height = RES[SIZE]['w'],RES[SIZE]['h']
    pressed = ""

    screen = pygame.display.set_mode(size)
    inp = _GetInputs_()
    #img = pygame.image.load("img.bmp")

    #ch = 'xy'
    ch, answer = getEquation()
    print "init form"

    line = 0
    horiz = random.randint(10, RES[SIZE]['w'] - 80)
    while 1:

        name,number,end = inp.__getInput__()
        inp.__show__()
        if inp.paused == 1:
#            print "paused"
            continue

        line = line + 1
        if end == True:
            print "Enter Digtal: ",answer
            inp.__show__()
            inp.__reset__()
            if number == answer:
                #if pressed == ch:
                line = 0
                STAT['right'] += 1
                print "Clever Boy!! Correct !! : ",STAT['right']
                if STAT['right'] % 3 == 0:
                    print "Right 3/6/9"
                    pants.play()
                elif STAT['right'] % 2 == 0:
                    print "Right 2/4/8"
                    low.play()
                elif STAT['right'] % 5 == 0:
                    high.play()
                else:
                    grape.play()
            else:
                STAT['error'] += 1
                pants.play()
                if STAT['error'] == 0:
                    pants.play()

        if line == 0 :
            horiz = random.randint(10, RES[SIZE]['w'] - 80)
            ch, answer = getEquation()

        #print ch, horiz
        PaintEquation(screen, ch, horiz, line % (RES[SIZE]['h']/4))
        sleep(SPEED)

    #print "Animation"

if __name__ == '__main__':
    sys.exit(main(sys.argv))
else:
    print "Import case"

