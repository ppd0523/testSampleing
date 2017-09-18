'''
Created on 2017. 8. 23.

@author: em
'''
import numpy as np

class Queue:
    window = 0
    raw = []
    rms = 0
    avg = 0
    def __init__(self, window):
        self.index = 0
        self.window = window
        self.raw = [] * window
    
    def input(self, data):
        self.raw[self.index] = data
        self.index = (self.index+1) % self.window
    
    def avg(self):
        result= 0
        for value in self.raw:
            result += value
        return result/self.window;