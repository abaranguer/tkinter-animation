#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import pygame as py

class Animation:
    root = None
    canvas = None
    circle = None
    x = 0
    y = 0
    incx = 4
    incy = 3
    maxX = 0
    maxY = 0

    def initialize(self):
        self.canvas = tk.Canvas(self.root, bg="gray")
        self.circle = self.canvas.create_oval(self.x, self.y, self.x + 20, self.y + 20, fill="white")
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
        
    def animation(self):
        # move circle
        (self.x, self.y, x1, y1) = self.canvas.coords(self.circle)

        if (self.x > self.maxX - 20) or (self.x < 0):
            self.incx = - self.incx
            self.boing()
            

        if (self.y > self.maxY - 20) or (self.y < 0):
            self.incy = - self.incy
            self.boing()

        self.canvas.move(self.circle, self.incx, self.incy)
        
        # update canvas
        self.canvas.update()
    
        # rearm trigger
        self.root.after(1000 / 20, self.animation)

    def boing(self):
        self.boingSound.play()
        
    def __init__(self):
        # pygame
        py.init()
        self.boingSound  = py.mixer.Sound("assets/boing_x.wav")

        #tkinter
        self.root = tk.Tk()
        #root.attributes("-fullscreen", True)
        self.root.title("running circle")
        self.maxY = self.root.winfo_screenheight() * 0.8
        self.maxX = self.root.winfo_screenwidth() * 0.8
        self.posY = self.root.winfo_screenheight() - self.maxY
        self.posX = self.root.winfo_screenwidth() - self.maxX
        self.root.geometry("%dx%d+%d+%d" % (self.maxX, self.maxY, self.posX, self.posY))
        self.root.resizable(False, False)
        self.initialize()
        self.root.after(0, self.animation)
        self.root.mainloop()

if __name__ == "__main__":
    Animation()

    

        
