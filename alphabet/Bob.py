#!/usr/bin/python
import sys, pygame
from time import sleep
from pygame import key
import random
import string

#SIZE='tiny'
SIZE='large'
#SIZE='long'
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

ball = pygame.image.load("ball.bmp")

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

def PaintOne(screen, char, horiz,line):
  #check if to get a new Symbol
  One = _Symbol_(screen, char)
  One.__fallOne__(horiz,line)
  
def Paint_1(screen, char):
  One = _Symbol_(screen, "A")
  One.__falling__()

def LoadBackground(screen, ball):
  print "LoadBackground"
  ballrect = ball.get_rect()
  screen.fill(black)
  screen.blit(ball, ballrect)
  pygame.display.flip()

def main(argv):

  pygame.init()
  size = width, height = RES[SIZE]['w'],RES[SIZE]['h']
  speed = [2, 2]

  screen = pygame.display.set_mode(size)
  #ball = pygame.image.load("ball.bmp")

  
  clock = pygame.time.Clock()
  ch = 'x'

  line = 0
  horiz = random.randint(10, RES[SIZE]['w'] - 10)
  while 1:
    line = line + 1
    for event in pygame.event.get():
      #print "Get Key : %s "% event
      if event.type == pygame.QUIT: 
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        print "pressed: %s" % event.dict['unicode']
        pressed = event.dict['unicode']
        if pressed == ch:
          line = 0

#      ballrect = ballrect.move(speed)
#      if ballrect.left < 0 or ballrect.right > width:
#        speed[0] = -speed[0]
#      if ballrect.top < 0 or ballrect.bottom > height:
#        speed[1] = -speed[1]

       #LoadBackground(screen, ball)
#      FullScreen(screen)
    
    if line == 0 :
      print "to get a new symbol"
      ch = random.choice(string.lowercase)
      horiz = random.randint(10, RES[SIZE]['w'] - 10)
    PaintOne(screen, ch.upper(), horiz, line % RES[SIZE]['h'])
    sleep(0.3)

    print "Animation"
    #sleep(2.0)
    #clock.tick(TIME)
    
    #Paint_1(screen, 'X')
    #Paint(screen, 'X')

if __name__ == '__main__':
  sys.exit(main(sys.argv))
else:
  print "Import case"


