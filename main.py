from tkinter import *
from time import sleep
from random import randint, choice
from turtle import heading
import copy

class Field:
    def __init__(self, c, n, m, width, height, walls=False):
        '''
       c - canvas instance
       n - number of rows
       m - number of columns
       width - width of game field in pixels
       height - width of game field in pixels
       walls - if True matrix should have 0's surrounded by 1's (walls)
       example
       1 1 1 1
       1 0 0 1
       1 1 1 1
       '''
        self.c = c
        self.a = []
        self.n = n + 2
        self.m = m + 2
        self.width = width
        self.height = height
        self.count = 0

        for i in range(self.n):
            self.a.append([])
            for j in range(self.m):
                self.a[i].append(0)
        self.a = [[randint(0, 2) for i in range(width)] for j in range(height)]
        self.draw()

    
    def step(self):
        self.cop = copy.deepcopy(self.a)
        
        for i in range(1, self.n+1):
            for j in range(1, self.m+1):
                self.neighbor = 0
                if self.cop[i+1][j] == 1:
                    self.neighbor += 1
                if self.cop[i+1][j+1] == 1:
                    self.neighbor+=1
                if self.cop[i][j+1] == 1:
                    self.neighbor+=1
                if self.cop[i-1][j+1] == 1:
                    self.neighbor+=1
                if self.cop[i-1][j] == 1:
                    self.neighbor+=1
                if self.cop[i-1][j-1] == 1:
                    self.neighbor+=1
                if self.cop[i][j-1] == 1:
                    self.neighbor += 1
                if self.cop[i+1][j-1] == 1:
                    self.neighbor += 1
                
                if self.neighbor not in (2, 3):
                    self.a[i][j] = 0
                elif self.neighbor == 3:
                    self.a[i][j] = 1

    def print_field(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.a[i][j], end="")
            print()

    def draw(self):
        '''
       draw each element of matrix as a rectangle with white background and wall rectangle should have dark grey
        background
       '''
        color = "#a9a9a9"
        sizen = self.width // (self.n - 2)
        sizem = self.height // (self.m - 2)
        c = [[randint(0, 1) for i in range(self.width)] for j in range(self.height)]
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if (self.a[i][j] == 1):
                    color = "#696969" # sheeps
                elif(self.a[i][j] == 2):
                    color = "#FFB6C1" # wolves
                else:
                    color = "#228B22"
                self.c.create_rectangle((i - 1) * sizen, (j - 1) * sizem, (i) * sizen, (j) * sizem, fill=color)
        self.step()
        self.c.after(100, self.draw)


root = Tk()
root.geometry("800x700")
c = Canvas(root, width=900, height=700)
c.pack()

f = Field(c, 100, 100, 800, 700)
f.print_field()
root.mainloop()
