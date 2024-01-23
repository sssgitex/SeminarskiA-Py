# -*- coding: utf-8 -*-
import keyboard
import re


from login import *
from catalog import *
from gmaster import *
from cart import *
from day import *

def main():
    dayUD()
    quit = 1;
    while quit:
        print("\014")
        print('Log in:')
        time.sleep(0.2)
        name = input("UserName: ")
        psw = input("Password: ")
        logStatus = logIn(name,psw)
        #print(logStatus)
        if logStatus == 'admin':
            print("Admin")
            quit = menuAdmin()
        elif logStatus == 'client':
            print("Client")
            quit = menuClient(name)
        elif logStatus == 'unreg':
            print("Unreg")
            quit = menuReg()
    time.sleep(0.2)
    print("\nHave a good day!")

def printAdminMenu():
    time.sleep(0.1)
    print("\n")
    print(" 1 - Product DB")
    print(" 2 - Master Schedule")
    print(" 3 - Day Stats")
    print(" 0 - Log Out")
    time.sleep(0.1)
    print("Choose a command (Press a number 0 - 4)\n")
    time.sleep(0.1)            

def menuAdmin():
    quit = 1
    while quit:
        time.sleep(0.1)
        printAdminMenu()
        time.sleep(0.2)
        print(statFunc(-1, 0, 'auto'))
        time.sleep(0.2)
        while True:
            if keyboard.is_pressed("0"):
                print("Pressed 0 - Quit")
                print("\014")
                return 0
                break
            if keyboard.is_pressed("1"):
                print("Pressed 1")
                print("\014")
                printProdDB(0," ")
                time.sleep(0.2)
                menuCatA()
                break
            elif keyboard.is_pressed("2"):
                print("Pressed 2")
                print("\014")
                printMasterDB()
                break
            elif keyboard.is_pressed("3"):
                print("Pressed 3")
                printDay()
                break
            elif re.search("[a-z]", keyboard.read_key()):
                print("There's no such command")
                break
        
    return 0     
    
        
def printClientMenu():
    print("\014")
    time.sleep(0.1)
    print("\n")
    print(" 1 - Catalog")
    print(" 2 - Guitar Master")
    #print(" 3 - Cart")
    print(" 0 - Log Out")
    time.sleep(0.1)
    print(" Choose a command (Press a number 0 - 10)\n")
    time.sleep(1)

def menuClient(name):
    quit = 1
    while quit:
        time.sleep(0.1)
        printClientMenu()
        time.sleep(0.2)
        while True:
            if keyboard.is_pressed("0"):
                print("\014")
                return 0
                break
            elif keyboard.is_pressed("1"):
                # Catalog
                print("Pressed 1")
                print("\014")
                printProdDB(0," ")
                time.sleep(0.2)
                menuCatC(name)
                break
            elif keyboard.is_pressed("2"):
                #Master
                print("\014")
                print("\n Fill the form please and we will cntact you in 1 hour: ")
                masterGet()
                break
            elif keyboard.is_pressed("3"):
                printProdDB(False, "")
                break
            elif re.search("[a-z]", keyboard.read_key()):
                print("There's no such command")
                break
        
    return 0    

def menuReg():
    #print("\014")
    time.sleep(0.1)
    print("Wrong UserName or Password (If you don't have an account please registrate)")
    print("Press 'y' - to try again")
    print("Press 'r' - to registrate")
    print("Press 'n' - to quit")
    time.sleep(0.2)
    while True:
        if keyboard.is_pressed('y' or 'Y'):
            return 1
        if keyboard.is_pressed('r' or 'R'):
            print('Registration:')
            time.sleep(0.2)
            name = input("UserName: ")
            psw = input("Password: ")
            reg(name, psw)
            return 1
        if keyboard.is_pressed('n' or 'N'):
            print("\014")
            return 0

def printCatMenuA():
    #print("\014")
    time.sleep(0.1)
    print("\n")
    print(" 1 - Add a new position")
    print(" 2 - Delete position")
    print(" 3 - Change position")
    print(" 4 - Search")
    print(" 5 - Storage stats")
    print(" 0 - Back")
    time.sleep(0.1)
    print("Choose a command (Press a number 0 - 5)\n")
    time.sleep(0.2)            

def menuCatA():
    sincWithProd()
    finalSinc()
    sincWithProd()
    quit = 1
    while quit:
        time.sleep(0.1)
        printCatMenuA()
        time.sleep(0.2)
        while True:
            if keyboard.is_pressed("0"):
                print("Pressed 0 - Quit")
                print("\014")
                quit = 0
                break
            elif keyboard.is_pressed("1"):
                #Add Position
                addPos()
                break
            elif keyboard.is_pressed("2"):
                #Delete position
                delPos()
                break
            elif keyboard.is_pressed("3"):
                #Stock control
                changeProd()
                break
            elif keyboard.is_pressed("4"):
                #Search
                searchPos()
                break
            elif keyboard.is_pressed("5"):
                #Storage stats
                menuStat()
                break
            #elif keyboard.read_key() in str():
            elif re.search("[a-z]", keyboard.read_key()):
                print("There's no such command")
                break
            
def printCatMenuC():
    #print("\014")
    print("\n 1 - Search")
    print(" 2 - Add or Remove (to|from) the Cart")
    print(" 3 - Cart")
    print(" 4 - Buy")
    print(" 5 - Clear the Cart")
    print(" 0 - Back")
    time.sleep(0.1)
    print("Choose a command (Press a number 0 - 4)\n")
    time.sleep(0.2)            

def menuCatC(name):
    quit = 1
    while quit:
        time.sleep(0.1)
        printCatMenuC()
        time.sleep(0.2)
        while True:
            if keyboard.is_pressed("0"):
                print("Pressed 0 - Quit")
                print("\014")
                quit = 0
                break
            elif keyboard.is_pressed("1"):
                #Search
                time.sleep(0.2)
                searchPos()
                break
            elif keyboard.is_pressed("2"):
                #Add/Remove Cart
                cartAdd(name)
                break
            elif keyboard.is_pressed("3"):
                #Cart Print
                printReceipt(1, name,'c')
                break
            elif keyboard.is_pressed("4"):
                #Buy
                payFunc(name)
                break
            elif keyboard.is_pressed("5"):
                #Clear Cart
                cartClear(name)
                break
            #elif keyboard.read_key() in str():
            elif re.search("[a-z]", keyboard.read_key()):
                print("There's no such command")
                break
            
def menuStat():
    sincWithProd()
    quit = 1
    while quit:
        time.sleep(0.1)
        printMenuStat()
        time.sleep(0.2)
        while True:
            if keyboard.is_pressed("0"):
                print("Pressed 0 - Quit")
                print("\014")
                printProdDB(False, "")
                quit = 0
                break
            if keyboard.is_pressed("1"):
                #Stat update
                print(statFunc(-1, 0, 'auto'))
                break
            if keyboard.is_pressed("2"):
                #Stat update
                time.sleep(0.3)
                idNum = eval(input(" Enter ID or 0 to read all: "))
                statFunc(0, idNum, '')
                break
            if keyboard.is_pressed("3"):
                #Stat update
                time.sleep(0.3)
                idNum = eval(input(" Enter ID: "))
                statFunc(1, idNum, '')
                break
        
def printMenuStat():
    time.sleep(0.1)
    print("\n 1 - Statistics update (New log file)")
    print(" 2 - Read")
    print(" 3 - Change")
    print(" 0 - Back")
    time.sleep(0.1)
    print(" Choose a command (Press a number 0 - 4)\n")
    time.sleep(0.2)
    
   
print(__name__)    
if __name__ == '__main__':
    main()
