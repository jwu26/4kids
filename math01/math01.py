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

#ball = pygame.image.load("ball.bmp")
ball = pygame.image.load("ball.jpeg")

def FullScreen(screen):
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill((250, 250, 250))

class _Symbol_:
  '''Title
  Description'''
  def __init__(self, screen, name):
    self.name = name
    self.position = (0,0)
    self.font = pygame.font.Font(None, 40)
    self.text = self.font.render(name, 1, white)
    self.screen = screen
    print "Alphabel Name: " + self.name +" x.y : %d.%d" % self.position

  def __sayHi__(self):
      print "BoBo, My name is " + self.name

  def __del__(self):
      print "bye! "+ self.name

  def __setPosition__(value):
    print "set position: " % value
    self.position = value

  def __falling__(self):
    print "I am Falling"
    for i in range(0, RES[SIZE]['h']/6):
        #print i
      self.screen.fill(black)
      self.screen.blit(self.text, (100,i*4))
      pygame.display.flip()
      sleep(0.5)
  def __fallOne__(self, horiz ,line):
    print "line : %d"% line
    #self.screen.fill(black)
    LoadBackground(self.screen, ball)
    self.screen.blit(self.text, (horiz,line*4))
    pygame.display.flip()

class _Formula_:
  '''Title
  Formula in 0 - 100
  Description'''
  def __init__(self, screen, name):
    self.name = str(name)
    self.position = (0,0)
    self.font = pygame.font.Font(None, 40)
    self.screen = screen
    self.text = self.font.render(self.name, 1, misc)
    LoadBackground(self.screen, ball)
    #print "Alphabel Name: " + self.name +" x.y : %d.%d" % self.position

  def __sayHi__(self):
    print "BoBo, My name is " + self.name

  def __del__(self):
    #print "bye! "+ str(self.name)
    return

  def __setPosition__(value):
    print "set position: " % value
    self.position = value

  def __falling__(self):
    print "I am Falling"
    for i in range(0, RES[SIZE]['h']/6):
        #print i
      self.screen.fill(black)
      self.screen.blit(self.text, (100,i*4))
      pygame.display.flip()
      sleep(0.5)

  def __fallOne__(self, horiz ,line):
    #print "line : %d"% line
    #self.screen.fill(black)
    #LoadBackground(self.screen, ball)
    self.screen.blit(self.text, (horiz,line*4))
    pygame.display.flip()

def getFormula():
    print "get random formulat in 0- ", RANGE_MAX
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

def Paint(screen, char):
  print "Paint Text"
  message = char
  font = pygame.font.Font(None, 40)
  text = font.render(message, 1, white)

  for i in range(0, RES[SIZE]['h']/6):
    print i
    screen.fill(black)
    screen.blit(text, (100,i*4))
    pygame.display.flip()
    sleep(1)

def PaintFormula(screen, formula, horiz,line):
  #check if to get a new Symbol
  Four = _Formula_(screen, formula)
  Four.__fallOne__(horiz,line)

def PaintOne(screen, char, horiz,line):
  #check if to get a new Symbol
  One = _Symbol_(screen, char)
  One.__fallOne__(horiz,line)

def LoadBackground(screen, ball):
  #print "LoadBackground"
  ballrect = ball.get_rect()
  screen.fill(black)
  screen.blit(ball, ballrect)
  pygame.display.flip()

class _GetInputs_:
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
            print "Get Key : %s "% event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print "pressed: %s" % event.dict['unicode']
                name = event.dict['unicode']
                if event.unicode.isalpha():
                    name += event.unicode
                elif event.unicode.isdigit():
                    number = number*10 + int(event.unicode)
                    print "uni code: " , int(event.unicode)
                    print "number ", number
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                elif event.key == K_SPACE:
                    self.__reset__()
                    self.paused ^= 1
                elif event.key == K_RETURN:
                    name = ""
                    end = True

        self.__set__(name, number, end)
        return name, number, end

    def __del__(self):
        return

def main(argv):

    pygame.init()
    size = width, height = RES[SIZE]['w'],RES[SIZE]['h']
    pressed = ""

    screen = pygame.display.set_mode(size)
    inp = _GetInputs_()
    #ball = pygame.image.load("ball.bmp")

    #ch = 'xy'
    ch, answer = getFormula()
    print "init form"

    line = 0
    horiz = random.randint(10, RES[SIZE]['w'] - 60)
    while 1:

        name,number,end = inp.__getInput__()
        inp.__show__()
        if inp.paused == 1:
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
            else:
                STAT['error'] += 1

#      FullScreen(screen)
        if line == 0 :
            horiz = random.randint(10, RES[SIZE]['w'] - 60)
            ch, answer = getFormula()

        #print ch, horiz
        PaintFormula(screen, ch, horiz, line % RES[SIZE]['h'])
        sleep(SPEED)

    #print "Animation"

if __name__ == '__main__':
    sys.exit(main(sys.argv))
else:
    print "Import case"


