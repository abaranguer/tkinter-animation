#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import math

class Animation:
    root = None
    canvas = None
    scale = None
    sign = None
    rb1 = None
    poly = None
    points = None
    center = [0, 0]
    tick = 50.0 # ms
    omega = 0.0
    theta = 0.0
    maxX = 0.0
    maxY = 0.0

    def calculePoints(self, a):
        N = 6.0
        self.points = []
        
        for i in range(0, 6):
            x0 = int(100.0 * math.cos( (2.0 * math.pi / N) * i + a))
            y0 = int(100.0 * math.sin( (2.0 * math.pi / N) * i + a))            
            x1 = int(180.0 * math.cos( (2.0 * math.pi / N) * i + (math.pi / N) + a))
            y1 = int(180.0 * math.sin( (2.0 * math.pi / N) * i + (math.pi / N) + a))

            self.points.append(x0 + self.center[0])
            self.points.append(y0 + self.center[1])
            self.points.append(x1 + self.center[0])
            self.points.append(y1 + self.center[1])
        
    def initialize(self):
        self.canvas = tk.Canvas(self.root,
                                bg="light blue",
                                width = self.maxX,
                                height = self.maxY - 100)
        self.theta = 0
        self.calculePoints(self.theta)
        self.poly = self.canvas.create_polygon(self.points,
                                               outline='black',
                                               fill='light green',
                                               width=10)
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
        
        self.scale = tk.Scale(self.root,
                              from_= 170,
                              to = 10000,
                              orient = tk.HORIZONTAL)
        self.scale.pack(fill=tk.X)

        self.sign = tk.IntVar()

        self.rb1 = tk.Radiobutton(self.root,
                                  text="clock wise",
                                  variable = self.sign,
                                  value = 1)
        self.rb1.pack(anchor=tk.W)
        
        tk.Radiobutton(self.root,
                       text="anti clock wise",
                       variable = self.sign,
                       value = -1).pack(anchor=tk.W)
        self.rb1.invoke()
        
    def animation(self):        
        self.omega = self.sign.get() *  2 * math.pi / self.scale.get()
        self.theta = self.theta + (self.omega * self.tick)
        self.calculePoints(self.theta)
        self.canvas.delete(self.poly)
        self.poly = self.canvas.create_polygon(self.points,
                                               outline='black',
                                               fill='light green',
                                               width=10)
        # update canvas
        self.canvas.update()
    
        # rearm trigger
        self.root.after(int(self.tick), self.animation)
        
    def __init__(self):
        #tkinter
        self.root = tk.Tk()
        #root.attributes("-fullscreen", True)
        self.root.title("rotating star")
        self.maxY = self.root.winfo_screenheight() * 0.75
        self.maxX = self.root.winfo_screenwidth() * 0.75
        self.posY = (self.root.winfo_screenheight() - self.maxY) / 2
        self.posX = (self.root.winfo_screenwidth() - self.maxX) / 2
        self.center = [self.maxX / 2, self.maxY / 2]
        self.root.geometry("%dx%d+%d+%d" % (self.maxX, self.maxY, self.posX, self.posY))
        self.root.resizable(False, False)
        self.initialize()
        self.root.after(0, self.animation)
        self.root.mainloop()

if __name__ == "__main__":
    Animation()
