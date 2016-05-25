#!/usr/bin/python
import sys, pygame
from time import sleep

WIDTH = 640
HEIGHT = 360
white = (255,255,255)
black = (0, 0, 0)

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
    for i in range(0, HEIGHT/6):
      print i 
      self.screen.fill(black)
      self.screen.blit(self.text, (100,i*4))
      pygame.display.flip()
      #sleep(1)


def Paint(screen, char):
  print "Paint Text"
  message = char
  font = pygame.font.Font(None, 40)
  text = font.render(message, 1, white)

  for i in range(0, HEIGHT/6):
    print i 
    screen.fill(black)
    screen.blit(text, (100,i*4))
    pygame.display.flip()
    sleep(1)

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
  size = width, height = WIDTH, HEIGHT
  speed = [2, 2]

  screen = pygame.display.set_mode(size)

  ball = pygame.image.load("ball.bmp")
  #ballrect = ball.get_rect()
  
  clock = pygame.time.Clock()

  while 1:
    for event in pygame.event.get():
      print "Get Key"
      if event.type == pygame.QUIT: 
        sys.exit()

#      ballrect = ballrect.move(speed)
#      if ballrect.left < 0 or ballrect.right > width:
#        speed[0] = -speed[0]
#      if ballrect.top < 0 or ballrect.bottom > height:
#        speed[1] = -speed[1]

      LoadBackground(screen, ball)
#      FullScreen(screen)

    print "Animation"
   # sleep(1)
    clock.tick(600)
    
    Paint_1(screen, 'X')
    #Paint(screen, 'X')
    

if __name__ == '__main__':
  sys.exit(main(sys.argv))
else:
  print "Import case"


