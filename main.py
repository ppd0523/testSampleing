'''
Created on 2017. 8. 4.

@author: em
'''

import matplotlib.pyplot as plt
import numpy as np
import math as m

rf = open("./sample.txt",'r')
wf = open("./sample2.txt",'w')

lhs = rf.readline()
cnt = 0
while lhs:
    t = cnt / 10
    y1 = m.sin(t)
    y2 = m.cos(t)
    line = lhs[:-1] + ',' + str( abs(int(round(y1*100))) ) + ',' + str( abs(int(round(y2*100))) )+'\n'
    wf.writelines(line)

    print(line)
    lhs = rf.readline()
    cnt += 1
    
rf.close()
wf.close()