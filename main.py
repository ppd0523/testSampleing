'''
Created on 2017. 8. 4.

@author: em
'''
 
import matplotlib.pyplot as plt
import myfunction as my
from matplotlib.pyplot import figure
 
list1 = list()
list2 = list()
list3 = list()
fig = figure()
with open("./EMGsample.txt", 'r') as rf:
    print("")
    data = [0, 0, 0, 0]
    i = 0
    while True:
        i += 1
        line = rf.readline()
        if not line:
            break
        if i == 20000:
            break
         
        raw = line.split('\t')
        data = [value for value in raw]
        mav = my.mav(float(data[0]))
        sd = my.sd(float(data[0]))
        list1 = list1+[data[0]]
        list2 = list2+[mav]
        list3 = list3+[sd]
         
        
    plt.plot(list1)
    plt.plot(list2)
    plt.plot(list3)
 
    plt.show()