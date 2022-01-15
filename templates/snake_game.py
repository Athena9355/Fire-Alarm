#https://www.youtube.com/watch?v=XGf2GcyHPhc
import math
import random
import pygame
import thinker as tk
from tkthinker import message box
class cube (object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        pass
    def move(self, dirnx, dirny):
        pass
    def draw(self, surface, eyes=False):
        pass
class snake (object):
    #snake is built up by the cube oject defined above
    def __int__(self, color,pos):
        pass
    def move(self):
        pass
    def reset(self, pos):
        pass
    def addCube(self):
        pass
    def draw(self, surface):
        pass
def drawGrid(w, rows, surface):
    pass
def redrawWindow(surface):
    pass
def randomSnake(rows, items):
    pass
def message_box(subject, content):
    pass

def main():
    #purpose of main: set a main loop
    #width and height --> dimension of grid
    width = 500
    height = 500
    rows = 20 #number of rows. can be set to any number as long as it can be divided by the width and height evenly. i.e. 500 has to be the multiple of rows
    win = pygame.display.set_mode ((width, height)) #making a surface
    #setting up a snake object below

    pass

rows =
w =
h =

cube.rows = rows
cube.w = w
main()