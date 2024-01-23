# -*- coding: utf-8 -*-
import datetime

def dayUD():
    try:
        cDate = datetime.date.today()
        fileName = "dayStat" + cDate.strftime("(%d;%m;%y)")
        with open(fileName,'r') as file:
            lines = file.readlines()
            dayList = [tuple(line.split('|')) for line in lines]
            return dayList
                 
    except:
        with open(fileName,'w') as file:
            print("\n Cart is empty")
            
def printDay():
    dayTuple = dayUD()
    
    cDate = datetime.date.today()
    
    total = 0
    print("\014")
    print("Today's Statistics' " + (cDate.strftime("(%d.%m.%y)")) + ":")
    head = " {0:<4} {1:<45}| {2:<10}| {3:<5}|"
    head = head.format("Item","", "Price $", "QT.")
    hSep = " ==================================================|===========|======|"
    bSep = hSep.replace('=', '-')
    print(head)
    print(hSep)
    
    for el in dayTuple:
        line = "{0},{1},{2},{3},{4}"
        line = line.format((el[1])[:8], (el[2])[:8], (el[4])[:8], (el[6])[:2], (el[7])[:2])
        bOut = " {0:<50}| {1:<10}| {2:<5}|"
        bOut = bOut.format(line, (el[8])[:9], (el[9]))
        print(bOut)
        print(bSep)
        

print(__name__)    
if __name__ == '__main__':
    printDay()