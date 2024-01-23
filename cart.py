# -*- coding: utf-8 -*-
from catalog import prodUD
from catalog import stgUD
from catalog import sincStg
import time
import datetime

#adding items to cart
def cartFill():
    try:
        stg = {}
        cat = {}
        stgUD(stg)
        prodUD(cat)
        cartList = {}
        
        idList = list(cat.keys())
        idNum = 1
        
        while idNum != 0:
            print("\n Enter ID's you'd like to add (0 when you're done)")
            time.sleep(0.2)
            idNum = eval(input(" Enter ID: "))
            if idNum in idList and idNum != 0 and idNum not in cartList.keys():
                time.sleep(0.2)
                qt = eval(input(" How many would you like to buy(0 to remove): "))
                if qt != 0 and qt <= int(stg[idNum]['Stock']):
                    cartList[idNum] = cat[idNum]
                    cartList[idNum].pop('n')
                    cartList[idNum]['QT'] = qt
                    cartList[idNum]['n'] = '\n'
                else:
                    if qt != 0:
                        print("\n |-------------------------------------------|")
                        print(" Looks like we don't have so many of these :(")
                        print(" All we have is ", stg[idNum]['Stock'])
                        print(" Try to enter again")
                    
            else:
                if idNum in cartList.keys():
                    print(" This item is in your cart already")
                if idNum not in idList or idNum == 0:
                    print(" [There's no such id]")
        #print(cartList)
        
    except:
        print("Some error occured :(")

    return(cartList)        

#adding items from cart to file
def cartAdd(name):
    cartList = cartFill()
    
    fileName = name + "-Cart"
    with open(fileName,'a') as file:
        outList = []
        for k in cartList.keys():
            outLine = "{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}|\n"
            outLine = outLine.format(k, cartList[k]['Brand'], cartList[k]['Model'], cartList[k]['Name'], cartList[k]['Color'], cartList[k]['Pick'], cartList[k]['Strings'], cartList[k]['Hand'], cartList[k]['Price'], cartList[k]['QT'])
            outList.append(outLine)
        
        file.writelines(outList)
     
    return outList

#update function    
def cartUD(cartList, name):
    try:
        fileName = name + "-Cart"
        with open(fileName,'r') as file:
            for l in file:
                val = {}
                key = int(l[:l.find('|')])
                val['Brand'], val['Model'], val['Name'], val['Color'], val['Pick'], val['Strings'], val['Hand'], val['Price'] , val['QT'], val['n'] = l[l.find('|')+1:].split('|')
                cartList[key] = val
                
        
    except:
        with open(fileName,'w') as file:
            print("\n Cart is empty")
            
# Print Cart and Receipt function           
def printReceipt(stat, name, mode):
    if stat == 1:        
        cartList = {}
        cartUD(cartList, name)
    elif stat == 0:
        return 0
    
    if mode == 'c':
        total = 0
        print("\014")
        print("\n Cart:")
        head = " {0:<4} {1:<45}| {2:<10}| {3:<5}|"
        head = head.format("Item","", "Price $", "QT.")
        hSep = " ==================================================|===========|======|"
        bSep = hSep.replace('=', '-')
        print(head)
        print(hSep)
        for k in cartList.keys():
            line = "{0},{1},{2},{3},{4}"
            line = line.format((cartList[k]['Brand'])[:8], (cartList[k]['Model'])[:8], (cartList[k]['Color'])[:8], (cartList[k]['Strings'])[:2], (cartList[k]['Hand'])[:2])
            bOut = " {0:<50}| {1:<10}| {2:<5}|"
            bOut = bOut.format(line, (cartList[k]['Price'])[:9], cartList[k]['QT'])
            print(bOut)
            print(bSep)
            total = total +  float(cartList[k]['Price']) * int(cartList[k]['QT'])
        print("\n Your total is ", total)
            
        return 1
    elif mode == 'r':
        total = 0
        print("\014")
        print("\n Here's your Receipt:")
        head = " {0:<4} {1:<45}| {2:<10}| {3:<5}|"
        head = head.format("Item","", "Price $", "QT.")
        hSep = " ==================================================|===========|======|"
        bSep = hSep.replace('=', '-')
        print(head)
        print(hSep)
        for k in cartList.keys():
            line = "{0},{1},{2},{3},{4}"
            line = line.format((cartList[k]['Brand'])[:8], (cartList[k]['Model'])[:8], (cartList[k]['Color'])[:8], (cartList[k]['Strings'])[:2], (cartList[k]['Hand'])[:2])
            bOut = " {0:<50}| {1:<10}| {2:<5}|"
            bOut = bOut.format(line, (cartList[k]['Price'])[:9], cartList[k]['QT'])
            print(bOut)
            print(bSep)
            total = total +  float(cartList[k]['Price']) * int(cartList[k]['QT'])
        print("\n Your total is ", total)
    
        stg = {}
        stgUD(stg)
        for k in list(cartList.keys()):
            stg[k]['Bought'] = int(stg[k]['Bought']) + int(cartList[k]['QT'])
            stg[k]['Stock'] = int(stg[k]['Stock']) - int(cartList[k]['QT'])
        
        with open("currentLog", 'r') as file:
            fileName = file.readline()
        sincStg(stg, fileName)    
            
        cDate = datetime.date.today()
        fileName = "dayStat" + cDate.strftime("(%d;%m;%y)")
        with open(fileName,'a') as file:
            outList = []
            for k in cartList.keys():
                outLine = "{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}|\n"
                outLine = outLine.format(k, cartList[k]['Brand'], cartList[k]['Model'], cartList[k]['Name'], cartList[k]['Color'], cartList[k]['Pick'], cartList[k]['Strings'], cartList[k]['Hand'], cartList[k]['Price'], cartList[k]['QT'])
                outList.append(outLine)
            file.writelines(outList)

#*Payment func*
def payFunc(name):
    
    fileName = name + "-Cart"
    with open(fileName,'r') as file:
        checkLine = file.read()
    if checkLine != "":
        printReceipt(1, name,'c')
        quit = 1
        time.sleep(0.2)
        conf = input("\n You confirm that this Receipt(y/n)? :")
        
        while quit:
            if conf == 'y' or conf == 'Y':
                print("\n Payment in process", end = "")
                for n in range(0,5):
                    time.sleep(0.2)
                    print(".", end = "")
                    time.sleep(0.2)
                    print(".", end = "")
                    time.sleep(0.2)
                    print(".", end = "")
                    time.sleep(0.2)
                print("\n Payment succeded! Thank You for your purchase)")    
                printReceipt(1, name,'r')
                cartClear(name)
                
                #quit = 0
                return 0
                
            elif conf == 'n' or conf == 'N':
                print("\n Back to catalog...")
                time.sleep(0.5)
                quit = 0
                printReceipt(0,name,'c')
                
            elif conf != 'n' or conf != 'N' or conf != 'y' or conf != 'Y':
                time.sleep(0.2)
                conf = input("\n You confirm that this Receipt(y/n)?: ")
    else:
         print("\n Your cart is empty")

# clear cart function         
def cartClear(name):
    fileName = name + '-Cart'
    with open(fileName,'w') as file:
        print(' Cart was cleared')

print(__name__)    
if __name__ == '__main__':
    #cartList = {}
    #cartClear('viktor')
    cartAdd('viktor')
    #cartUD(cartList, 'viktor')
    #printReceipt(1)
    payFunc('viktor')
    