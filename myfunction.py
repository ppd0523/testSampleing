'''
Created on 2017. 8. 22.

@author: em
'''
from math import sqrt

WINDOW = 10

# moving average(MA)
def ma(new):
    avg = ma.oldAvg + (new - ma.list[0]) / WINDOW
    ma.oldAvg = avg 
    ma.list = ma.list[1:9] + [new]
    return avg
ma.list = [0] * WINDOW    
ma.oldAvg = 0

# batch root mean square error
# def rmse(new):
#     avg = ma(new)
#     result = sqrt( (new-avg)*(new-avg) )
#     return result

# root mean square(RMS)
def rms(new):
    rms2 = (new + rms.list[0]) * (new - rms.list[0]) / WINDOW + rms.oldRms2
    rms.oldRms2 = rms2
    rms.list = rms.list[1:-1] + [new]
    return sqrt(rms2)
rms.list = [0] * WINDOW
rms.oldRms2 = 0

# mean absolute value(MAV)
def mav(new):
    data = abs(new)
    absMa = mav.oldMav + (data - mav.list[0]) / WINDOW
    mav.oldMav = absMa
    mav.list = mav.list[1:9] + [data]
    return absMa
mav.list = [0] * WINDOW
mav.oldMav = 0

# standard deviation(SD)
def sd(new):
    sd2 =  ( (new + sd.list[0])*(new - sd.list[0])-2*ma(new)*(new - sd.list[0]) )/(WINDOW-1) + sd.oldSd2
    sd.oldSd2 = sd2
    sd.list = sd.list[1:9] + [new]
    return sd2
sd.list = [0] * WINDOW
sd.oldSd2 = 0