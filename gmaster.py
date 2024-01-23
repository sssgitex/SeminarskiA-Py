# -*- coding: utf-8 -*-
import datetime
import time

def masterGet():
    try:
        cDate = datetime.date.today()
        fileName = "masDBC" + cDate.strftime("%d%m%y")
        with open(fileName, 'a') as file:
            mas = tuple()
            time.sleep(0.2)
            date = eval(input("\n Enter a date you would like to reserve\n (DaymMonth all integer numbers without separation): "))
            desc = input("Describe your problem(Brand,Model,Problem): ")
            line = ("{0}|{1}|\n").format(date, desc)
            mas = [tuple(line.split('|'))]
        
            line = ("{0}|{1}|\n").format(date, desc)
            file.write(line)
            
        print(mas)
    except FileNotFoundError:
        with open(fileName, 'w') as file:
            masterGet()


        

def masterUD():
    cDate = datetime.date.today()
    try:
        fileName = "masDBC" + cDate.strftime("%d%m%y")
        with open(fileName, 'r') as file:
            lines = file.readlines()
            mas = [tuple(line.split('|')) for line in lines]
        
        return mas  
     
    except FileNotFoundError or TypeError:
        cDate = datetime.date.today()
        fileName = "masDBC" + cDate.strftime("%d%m%y")
        with open(fileName, 'w') as file:
            file.write("||\n")
            return 0
        
    except:
        print("Ooopsie there's nothing in here...\n")

def printMasterDB():
    
    mas = masterUD()
    if mas != 0:
        head = " {0:<9}| {1:<79}|"
        head = head.format("Date", "Description")
        hSep = " =========|================================================================================|"
        bSep = hSep.replace('=', '-')
        
        cDate = datetime.date.today()
        fileName = "masDBC" + cDate.strftime("%d%m%y")
        print("\n ", fileName)
        print(head)
        print(hSep)
        for el in mas:
            bOut = " {0:<9}| {1:<79}|"
            bOut = bOut.format(el[0], el[1])
            print(bOut)
            print(bSep)
    else:
        printMasterDB()
            
        
print(__name__)    
if __name__ == '__main__':
    #masterGet()
    printMasterDB()     