# -*- coding: utf-8 -*-    
def dataUpdate(log):
    try:
        with open('loginDB', 'r') as file:
            for l in file:   
                key, val = l.split('|')
                val = val[0:-1]
                log[key] = val
    except ValueError:
            pass
def reg(name, psw):
    quit = 1
    log = {}
    try:
        dataUpdate(log)
        while quit:
            if name in log.keys() or name == "":
                print("This username is taken, choose the other one please)")    
                name = input('UserName:')
            else:
                quit = 0
        with open('loginDB', 'a') as file:
            line = name + "|" + psw
            print(line)
            file.write(line+"\n")
            
    except:
        with open('loginDB', 'w') as file:
            line = name + "|" + psw
            file.write(line+"\n")
    
def logIn(name,psw):
    log = {}
    try:    
        dataUpdate(log)
        if name == 'admin' and psw == 'root':
            return 'admin'
        elif name in log.keys() and psw == log.get(name):
            return 'client'
        else:
            return 'unreg'
    except FileNotFoundError:
        with open('loginDB', 'w') as file:
            file.write("0|0")
            reg(name, psw)
            return 'unreg'
    
       
    
    
#print(__name__)      


