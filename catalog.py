# -*- coding: utf-8 -*-
import re
import datetime
import shutil
import time
import matplotlib.pyplot as plt

#catalog UpDate function (from file to dictionary)  
def prodUD(cat):
    try:
        with open('catalogDB', 'r') as file:
            
            for l in file:
                val = {}
                key = int(l[:l.find('|')])
                val['Brand'], val['Model'], val['Name'], val['Color'], val['Pick'], val['Strings'], val['Hand'], val['Price'], val['Stock'], val['n'] = l[l.find('|')+1:].split('|')
                cat[key] = val
    except FileNotFoundError:
        with open('catalogDB', 'x') as file:
            print("\nOoopsie there's nothing in here...")
    except:
        print("Ooopsie there's nothing in here...\n")
        
#Print Catatlog
def printProdDB(search, name):
    print("\014")
    sortPos()
    if search:
        searchRes = False
    cat = {}
    print("Catalog: \n")
    prodUD(cat)
    head = " {0:<5}| {1:<10}| {2:<14}| {3:<18}| {4:<14}| {5:<8}| {6:<8}| {7:<5}| {8:<10}| {9:<6}|"
    head = head.format("ID", "Brand", "Model", "Name", "Color", "PickUps", "Strings", "Hand", "Price $", "Stock")
    hSep = " =====|===========|===============|===================|===============|=========|=========|======|===========|=======|"
    bSep = hSep.replace('=', '-')
    print(head)
    print(hSep)
    if not search:
        for k in cat.keys():
            bOut = " {0:<5}| {1:<10}| {2:<14}| {3:<18}| {4:<14}| {5:<8}| {6:<8}| {7:<5}| {8:<10}| {9:<6}|"
            bOut = bOut.format(k, (cat[k]['Brand'])[:9], (cat[k]['Model'])[:13], (cat[k]['Name'])[:17], (cat[k]['Color'])[:13], (cat[k]['Pick'])[:7], (cat[k]['Strings'])[:7], (cat[k]['Hand'])[:4], (cat[k]['Price'])[:9], (cat[k]['Stock'])[:7], cat[k]['n'])
            print(bOut)
            print(bSep)
    else:
        
        for k in cat.keys():
            if re.search(name, cat[k]['Brand'].lower()) or re.search(name, cat[k]['Model'].lower()):
                searchRes = True
                bOut = " {0:<5}| {1:<10}| {2:<14}| {3:<18}| {4:<14}| {5:<8}| {6:<8}| {7:<5}| {8:<10}| {9:<6}|"
                bOut = bOut.format(k, (cat[k]['Brand'])[:10], (cat[k]['Model'])[:14], (cat[k]['Name'])[:18], (cat[k]['Color'])[:14], (cat[k]['Pick'])[:8], (cat[k]['Strings'])[:8], (cat[k]['Hand'])[:5], (cat[k]['Price'])[:10], (cat[k]['Stock'])[:6], cat[k]['n'])
                print(bOut)
                print(bSep)
        if not searchRes:
            print(" Looks like we don't have any positions with this name right now :(")

    
    cat.clear()

#add catolg position    
def addPos():
    try:
        cat = {}
        val = {}
        prodUD(cat)
        lKeys = list(cat.keys())
        list.sort(lKeys)
        freeKey = 0
        
        for k in range(len(lKeys)-1):
            if lKeys[k+1] - lKeys[k] > 1:
                freeKey = lKeys[k]   
        if freeKey == 0:
            freeKey = lKeys[-1]
        key = freeKey + 1
    except IndexError:
        key = 1000
        
    time.sleep(0.2)    
    val['Brand'] = input(" Enter a Brand: ")
    val['Model'] = input(" Enter a Model: ")
    val['Name'] = input(" Enter a Name: ")
    val['Color'] = input(" Enter a Color: ")
    val['Pick'] = input(" Enter a Picks: ")
    val['Strings'] = input(" Enter a Strings: ")
    val['Hand'] = input(" Enter a Hand: ")
    val['Price'] = input(" Enter a Price(Just Int part): ") + ".00"
    val['Stock'] = input(" Enter a Stock: ")
    val['n'] = "\n"
    cat[key] = val
    
    with open('catalogDB', 'a') as file:
        
        apLine = ("{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}|{10}")
        apLine = apLine.format(key,val['Brand'],val['Model'],val['Name'],val['Color'],val['Pick'],val['Strings'],val['Hand'],val['Price'],val['Stock'],val['n'])
        file.write(apLine)
        
        print("\n" + apLine)
        print (" New item was added")
    sortPos()
    finalSinc()
    print("\014")
    printProdDB(False, "")
    return

#Delete catalog position    
def delPos():
    cat = {}
    prodUD(cat)
    time.sleep(0.2)
    posToDel = input("Enter ID to delete position: ")
    if int(posToDel) in list(cat.keys()):
        with open('catalogDB', 'r+') as file:
            lTemp = []
            
            for line in file:
                lTemp.append(line)
            file.truncate(0)
            file.seek(0)
            
            for el in lTemp:
                if el[0:4] == posToDel:
                    lTemp.remove(el)
            #print(lTemp)
            file.writelines(lTemp)
    
        #print("\014")
        printProdDB(False, "")
    else:
        print("\n No position with this ID")
    finalSinc()

#Sorting by ID in catalog file        
def sortPos():
    try:
        with open('catalogDB', 'r') as file:
            line = file.read()
        if line != "":
            with open('catalogDB', 'r+') as file:
                lTemp = []
                for line in file:
                    lTemp.append(line)
                lTemp[-1] = lTemp[-1]
                lTemp.sort()
                file.truncate(0)
                file.seek(0)
                file.writelines(lTemp)
        else:
            pass
    except FileNotFoundError:
        with open('catalogDB', 'w') as file:
            sortPos()

      
def searchPos():
    time.sleep(0.2)
    searchName = input(" Enter the name of Brand or Model you want to find: ").lower()
    if searchName != " ":
        printProdDB(True, searchName)

def changeProd():
    cat = {}
    prodUD(cat)
    
    try:
        #stock val
        time.sleep(0.2)
        idNum = eval(input("Enter ID: "))
        print("\n Enter integer numbers or '-' to save previous number")
        print(" Position #", idNum)
        lKeys = dict(cat[idNum]).keys()
        
        for k in lKeys:
            if k != 'n':
                inLine = (" {0}: ").format(k)
                temp = input(inLine)
                if temp != '-':
                    cat[idNum][k] = temp

        sincProd(cat)
        sincWithProd()
        
    except KeyError:
        print("Storage is empty!")

#storage UpDate function (from file to dictionary)    
def stgUD(stg):    
    try:
        with open("currentLog", 'r') as file:
            fileName = file.readline()
        with open(fileName, 'r') as file:
            
            for l in file:
                val = {}
                key = int(l[:l.find('|')])
                val['Delivery'], val['Stock'], val['Bought'], val['Price'], val['n'] = l[l.find('|')+1:].split('|')
                stg[key] = val
                
    except FileNotFoundError:
        with open("firstLog", 'r') as file:
            fileName = file.readline()
            time.sleep(0.5)
        with open(fileName, 'r') as file:
            
            for l in file:
                val = {}
                key = int(l[:l.find('|')])
                val['Delivery'], val['Stock'], val['Bought'], val['Price'], val['n'] = l[l.find('|')+1:].split('|')
                stg[key] = val
            print("\n Ooopsie there's nothing in here...")  
    except ValueError:
        pass
    
#main function (works with storage files, and function of Search and Change
        
def statFunc(op, idNum, mode):
    print("\nWherehouse:")
    print(" [" + mode + " statistics update]")
    cat = {}
    prodUD(cat)
    with open ("currentLog", 'r') as file:
        check = file.read()
    cDate = datetime.date.today()
    #cDate = datetime.date(2024,2,1)
    
    # cDate = datetime.date(2024,4,25) /this gives us an
    # apartunity to change data and test this function (you set it on 1 of february to see the update)
    
    cDay = cDate.day

    

    with open("firstLog", 'r') as file:
        firstFileName = file.readline()
    with open("currentLog", 'r') as file:
        fileName = file.readline()
    
    #every ("day of delivery") day of a moth fileName updates
    if cDay == 1:
        fileName = "stgStat" + cDate.strftime("(%d;%m;%y)")
        with open("currentLog", 'w') as file:
            file.write(fileName)
    
    #FSYSFILE
    if op == -1:
        if cDay == 1 and firstFileName != "":
            stg = {}
            stgUD(stg)
            
            # manual
            if mode == 'manual':
                stgUD(stg)
                print(fileName + "MAN")
                with open(fileName, 'w') as file:
                    time.sleep(0.2)
                    for k in cat:
                        print(" Enter the delivery on Position #", k, end = ' ')
                        delivAm = eval(input(": "))
                        stockAm = delivAm + int(stg[k]['Stock']) 
                        #id|stock(1st day od a month)|stock(left)|bought
                        file.write(("{0}|{1}|{2}|{3}|{4}|\n").format(k, delivAm, stockAm, 0, cat[k]['Price']))
                
                with open("firstLog", 'w') as file:
                    file.write(fileName)
                sincWithProd()
                    
                return " New log file has been created " + fileName
            
            # auto     
            elif mode == 'auto':
                try: 
                    with open(fileName, 'r') as file:
                        pass
                    print(" Last log" + firstFileName)
                    print(" Main log" + fileName)
                    #shutil.copy(firstFileName, fileName)
                    
                    #with open("firstLog", 'w') as file:
                        #file.write(fileName)
                    if fileName != firstFileName:
                        statFunc(-1, 0, 'manual')
                except:
                    statFunc(-1, 0, 'manual')
                        
                #
                
                prodUD(cat)
                stgUD(stg)
                if stg.keys() != cat.keys():    
                    print("It looks like there are some new positions on the list\n")    
                    statFunc(-1, 0, 'manual') #
                    
                #return " New log file has been created " + fileName
                return " Statistics are up to date"
        
            if firstFileName == "" and check == "":
                fileName = "stgStat" + cDate.strftime("(%d;%m;%y)")
                # manual
                with open(fileName, 'w') as file:
                    time.sleep(0.2)
                    for k in cat:
                        print(" Enter the stock amout on Position #", k, end = ' ')
                        stockAm = input(": ")
                        #id|stock(1st day od a month)|stock(left)|bought
                        file.write(("{0}|{1}|{2}|{3}|{4}|\n").format(k, stockAm, stockAm, 0, cat[k]['Price']))
            #with open("firstLog", 'w') as file:
                #file.write(fileName)
            with open("currentLog", 'w') as file:
                file.write(fileName)    
            return " First log file has been created " + fileName
            finalSinc()
        
        else:
            #you can update it once a month on "delivary date"
            return " Everything up to date. You can't update log today: " + cDate.strftime("(%d.%m.%y)")
   
    
   
    #FSEARCH
    if op == 0 and check != "":
        
        graphStg('Stock')
        graphStg('Delivery')
        graphStg('Bought')
        
        #from file to dict
        stg = {}
        stgUD(stg)
        #sincAdd()
        
        print("\014")
        printProdDB(False, "")
        with open("currentLog", 'r') as file:
            fileName = file.readline()

        searchRes = False
        head = " {0:<5}| {1:<10}| {2:<14}| {3:<18}| {4:<14}|"
        head = head.format("ID", "Delivery", "Stock", "Bought", "Price")
        hSep = " =====|===========|===============|===================|===============|"
        bSep = hSep.replace('=', '-')
        print(head)
        print(hSep)
        if idNum == 0:
            for k in stg.keys():
                bOut = " {0:<5}| {1:<10}| {2:<14}| {3:<18}| {4:<14}|"
                bOut = bOut.format(k, stg[k]['Delivery'], stg[k]['Stock'], stg[k]['Bought'], stg[k]['Price'], stg[k]['n'])
                print(bOut)
                print(bSep)
        else:
            for k in cat.keys():
                if k == idNum:
                    searchRes = True
                    bOut = " {0:<5}| {1:<10}| {2:<14}| {3:<18}| {4:<14}|"
                    bOut = bOut.format(k, stg[k]['Delivery'], stg[k]['Stock'], stg[k]['Bought'], stg[k]['Price'], stg[k]['n'])
                    print(bOut)
                    print(bSep)
            if not searchRes:
                print(" Looks like we don't have any positions with this name right now :(")
        finalSinc()    
        
    #FCHANGE
    elif op == 1 and check != "":
        
        stg = {}
        stgUD(stg)
        print("\014")
        try:
            #stock val
            print("\n Enter integer numbers or '-' to save previous number")
            print(" Position #", idNum)
            lKeys = dict(stg[idNum]).keys()
            
            time.sleep(0.2)
            for k in lKeys:
                if k != 'n' and k != 'Price':
                    inLine = (" {0}: ").format(k)
                    temp = input(inLine)
                    if temp != '-':
                        stg[idNum][k] = temp
    
            sincStg(stg, fileName)
            sincWithProd()

            printProdDB(False, "")    
        except KeyError:
            print("Storage is empty!")

    else:
        print("\n Some unpredictable error has accured :( ")
        print("\n Try to add some positions first ")
        
#sinc stirage dictionary with file
def sincStg(stg, fileName):
    outList = []
    for k in stg:
        outLine = "{0}|{1}|{2}|{3}|{4}|\n"
        outLine = outLine.format(k, stg[k]['Delivery'], stg[k]['Stock'], stg[k]['Bought'], stg[k]['Price'])
        outList.append(outLine)
    with open(fileName, "w") as file:
        file.writelines(outList)


#sinc storage data with Stock status in catalog
def sincWithProd():
    cat = {}
    stg = {}
    prodUD(cat)
    stgUD(stg)
    with open("currentLog", 'r') as file:
        fileName = file.readline()
    
    for k in cat:
        try:
            if int(stg[k]['Stock']) != 0:
                cat[k]['Stock'] = 'In'
            else:
                cat[k]['Stock'] = 'Out'
        except KeyError:
            pass
            #print("KeyError -> Sinc\n")
            
    for k in cat:
        try:
            if int(cat[k]['Price']) != stg[k]['Price']:
                stg[k]['Price'] = cat[k]['Price']
            else:
                pass
        except KeyError:
            print("KeyError -> Sinc\n")
            finalSinc()
        except ValueError:
            pass
    sincProd(cat)
    sincStg(stg, fileName)

#Sinc Cat dictionary with file
def sincProd(cat):
    outList = []
    for k in cat:
        outLine = ("{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}|\n")
        outLine = outLine.format(k,cat[k]['Brand'],cat[k]['Model'],cat[k]['Name'],cat[k]['Color'],cat[k]['Pick'],cat[k]['Strings'],cat[k]['Hand'],cat[k]['Price'],cat[k]['Stock'])
        outList.append(outLine)
    
    with open('catalogDB', "w") as file:
        #print(cat)
        file.writelines(outList)
 
def hardSinc():
    cat = {}
    stg = {}
    prodUD(cat)
    stgUD(stg)
    
    with open("currentLog", 'r') as file:
        fileNameStg = file.readline()
    with open('catalogDB', 'r') as file:
        catFirstLine = file.readline()
    with open(fileNameStg, 'r') as file:
        stgFirstLine = file.readline()
        
    if stgFirstLine == "" and catFirstLine != "":
        with open(fileNameStg, 'w') as file:
            lKeys = list(cat.keys())
            k = lKeys[0]
            time.sleep(0.2)
            print(" Enter the delivery on the new position", k, end = ' ')
            delivAm = eval(input(": "))
            stockAm = delivAm
            #id|stock(1st day od a month)|stock(left)|bought
            file.write(("{0}|{1}|{2}|{3}|{4}|\n").format(k, delivAm, stockAm, 0, cat[k]['Price']))
        #sincAdd()
    elif stgFirstLine != "" and catFirstLine == "":
        with open(fileNameStg, 'w') as file:
           print("STG CLEARED")

def finalSinc():
    print("SINC")
    cat = {}
    stg = {}
    prodUD(cat)
    stgUD(stg)
    
    lKeysStg = list(stg.keys())
    lKeysCat = list(cat.keys())
    
    with open("currentLog", 'r') as file:
        fileName = file.readline()
    
    #cat empty nd stg empty
    if not lKeysCat and not lKeysStg:
        print("\n Storage is empty")
        
    #cat empty stg not    
    elif (not lKeysCat) == True and (not lKeysStg) == False:
        #clear stg    
        with open(fileName, 'w') as file:
            pass
        
    #stg empty cat not
    elif (not lKeysStg) == True and (not lKeysCat) == False:
        time.sleep(0.2)
        for k in lKeysCat:
            if k not in lKeysStg:
                with open(fileName, 'a') as file:
                    print(" Enter the delivery on the new position", k, end = ' ')
                    delivAm = eval(input(": "))
                    stockAm = delivAm
                    #id|stock(1st day od a month)|stock(left)|bought
                    file.write(("{0}|{1}|{2}|{3}|{4}|\n").format(k, delivAm, stockAm, 0, cat[k]['Price']))
    else:
        if len(lKeysCat) > len(lKeysStg):
            time.sleep(0.2)
            for k in lKeysCat:
                if k not in lKeysStg:
                    with open(fileName, 'a') as file:
                        print(" Enter the delivery on the new position", k, end = ' ')
                        delivAm = eval(input(": "))
                        stockAm = delivAm
                        #id|stock(1st day od a month)|stock(left)|bought
                        file.write(("{0}|{1}|{2}|{3}|{4}|\n").format(k, delivAm, stockAm, 0, cat[k]['Price']))
        
        elif len(lKeysCat) < len(lKeysStg):
            for k in lKeysStg:
                if k not in lKeysCat:
                    stg.pop(k)
                print("sinc STG")
                sincStg(stg, fileName)
    sortStg()
    sincWithProd()
    #print("\014")
    #printProdDB(False, "")           
 
def sortStg():
    with open("currentLog", 'r') as file:
        fileName = file.readline()
    try:
        with open(fileName, 'r') as file:
            line = file.read()
        if line != "":
            with open(fileName, 'r+') as file:
                lTemp = []
                for line in file:
                    lTemp.append(line)
                lTemp[-1] = lTemp[-1]
                lTemp.sort()
                file.truncate(0)
                file.seek(0)
                file.writelines(lTemp)
        else:
            pass
    except FileNotFoundError:
        with open(fileName, 'w') as file:
            sortPos()    
 
def graphStg(mode):
    try:
        stg = {}
        stgUD(stg)
        labels = list(stg.keys())
        lTemp = []
        plt.title(mode + " Stats")
        if mode == 'Delivery':
            for k in stg:
                lTemp.append(int(stg[k]['Delivery']))
        elif mode == 'Stock':
            for k in stg:
                lTemp.append(int(stg[k]['Stock']))
        elif mode == 'Bought':
            for k in stg:
                lTemp.append(int(stg[k]['Bought']))
        if (not lTemp) == False:
            sizes = lTemp
            explode = (0.1, 0, 0, 0)
            plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%')
            plt.axis('equal')
            plt.show()
        else:
            print("\n This line is empty")
    except ValueError:
        pass
    
 
print(__name__)
if __name__ == '__main__':
    #printProdDB(0,"")
    #sincAdd()
    #sincAdd()
    #addPos()
    #changeProd()

    #sortStg()
    #printProdDB(0,"")
    statFunc(1, 2001, "")
    
    graphStg('Stock')
    graphStg('Delivery')
    graphStg('Bought')
    #finalSinc()
    