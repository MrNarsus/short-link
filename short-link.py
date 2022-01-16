#!/bin/python3
# The Author: https://github.com/Mr-Narsus
import pyshorteners
import pyfiglet,os
Red="\033[0;31m" # Red
Green="\033[0;32m" # Green
Yellow="\033[0;33m" # Yellow
s = pyshorteners.Shortener()
class shorting:
    def __init__(self):
        print(Red + pyfiglet.figlet_format("SHORT - LINK",font='slant'))
        print(Green + "\t\t\tVersion 1.0.0")
        self.choice()
    def choice(self):
        self.mean()
        arch = input("Please Choose A Number: ")
        if arch == '1' or arch == '01' : self.Adf_ly()
        elif arch == '2' or arch == '02' : self.bitly()
        elif arch == '3' or arch == '03': self.chilp()
        elif arch == '4' or arch == '04': self.clickru()
        elif arch == '5' or arch == '05' : self.dagd()
        elif arch == '6' or arch == '06' : self.isgd()
        elif arch == '7' or arch == '07': self.NullPointer()
        elif arch == '8' or arch == '08': self.osdb()
        elif arch == "9" or arch == '09': self.qpsru()
        elif arch == '10' : self.tinyurl()
        elif arch == '11' : self.tinycc()
        elif arch == '10' : self.shortcm()
        else : print("Error !!, Please Write Number from 1 to 13")
    def mean(self):
        print('''
    [01] Adf.ly
    [02] Bit.ly
    [03] Chilp.it
    [04] Clck.ru
    [05] Da.gd
    [06] Is.gd
    [07] NullPointer
    [08] Os.db
    [09] Qps.ru
    [10] TinyURL.com
    [11] Tiny.cc
    [12] Short.cm\n''')
    def Adf_ly(self):
        try :
            f = open('adfly.txt','x+')
            api_key1 = input("Type Adf.ly API Key: ")
            id_user = input("Type Adf.ly User ID: ")
            f.write(api_key1);f.write('\n');f.write(id_user)
            adf_key = f.readline().strip('\n')
            adf_user = f.readline().strip('\n')
            f.close()
        except FileExistsError:
            f = open('adfly.txt','r')
            adf_key = f.readline().strip('\n')
            adf_user = f.readline().strip('\n')
        a2 = int(input("[1] default\n[2] q.gs\nChoose A Number: "))
        if a2 == 1 :
            domain2 = 'ad.fly'
        elif a2 == 2:
            domain2 = 'q.gs'
        else:
            print("Error !!, Choose number 1 or 2 ")
            exit()
        url2 = input("Enter Your URL: ")
        s = pyshorteners.Shortener(api_key=adf_key, user_id=adf_user,domain=domain2)
        d = s.adfly.short(url2)
        print ("shorted link is: ",d)
    def bitly(self):
        try :
            f = open('bitly.txt','x+')
            api_key1 = input("Type Bit.ly API Key: ")
            f.write(api_key1);bitl = f.readline();f.close()
        except FileExistsError:
            f = open('bitly.txt','r');bitl = f.readline();f.close()
        url = input("Enter Your URL: ")
        s = pyshorteners.Shortener(api_key=bitl)
        d = s.bitly.short(url)
        print("shorted URL is: ", d)
    def chilp(self):
        url = input("Enter Your URL: ")
        d = s.chilpit.short(url)
        print("Shorted link is: ",d)
    def clickru(self):
        url = input("Enter Your URL: ")
        d = s.clckru.short(url)
        print("Shorted link is: " , d )
    def dagd(self):
        url = input("Enter Your URL: ")
        d = s.dagd.short(url)
        print("Shorted link is: ",d)
    def isgd(self):
        url = input("Enter Your URL: ")
        d = s.isgd.short(url)
        print("Shorted link is: ",d)
    def NullPointer(self):
        a2 = int(input('[1] https://0x0.st\n[2] https://ttm.sh\nchoose a number:'))
        if a2 == 1 :
            domain2 = 'https://0x0.st'
        elif a2 == 2 :
            domain2 = 'https://ttm.sh'
        else:
            print ("Error !!, Please choose number 1 or 2 ") ; exit()
        s = pyshorteners.Shortener(domain=domain2)
        url = input("Enter Your URL: ")
        d = s.nullpointer.short(url)
        print("Shorted link is: ", d)
    def osdb(self):
        url = input("Enter Your URL: ")
        d = s.osdb.short(url)
        print("SHorted link is: ", d)
    def qpsru(self):
        url = input("Enter Your URL: ")
        d = s.qpsru.short(url)
        print("Shorted link is: ",d )
    def tinyurl(self):
        url = input("Enter Your URL: ")
        d = s.tinyurl.short(url)
        print("Shorted link is: ")
    def tinycc(self):
        try :
            f = open('tinycc.txt','x+')
            api_key1 = input("Type Tiny.cc API key: ")
            yiny_login = input("Type Login Tiny.cc: ")
            f.write(api_key1);f.write('\n');f.write(yiny_login)
            tin_key = f.readline().strip('\n')
            tin_login = f.readline().strip('\n') ; f.close()
        except FileExistsError:
            f = open('tincc.txt','r')
            tin_key = f.readline().strip('\n')
            tin_login = f.readline().strip('\n') ; f.close()
        s = pyshorteners.Shortener(api_key=tin_key, login=tin_login)
        url = input("Enter Your URL: ")
        d = s.tinycc.short(url)
        print("Shorted link is: ", d)
    def shortcm(self):
        try :
            f = open('shortcm.txt','x+')
            api_key1 = input("Type Short.cm API key: ")
            f.write(api_key1); short_key = f.readline();f.close()
        except FileExistsError:
            f = open('shortcm.txt','r');short_key = f.readline();f.close()
        s = pyshorteners.Shortener(api_key=short_key)
        url = input("Enter Your URL: ")
        d = s.shortcm.short(url)
        print("Shorted link is: ",d)
class unshort:
    ''' bitly, chilpit, clckru '''
    def __init__(self):
        os.system('clear');print(Red + pyfiglet.figlet_format("UNSHORT",font='slant')+ Yellow)
        self.choice()
    def choice(self):
        print (''' 
        [01] Bit.ly
        [02] Chilp.it
        [03] Clck.ru
        [04] Is.gd
        [05] NullPointer
        ''')
        a = input('Enter A Number: ')
        if a == '1' or a == '01' : self.bitly()
        elif a == '2' or a == '02' : self.chilpit()
        elif a == '3' or a == '03' : self.clckur()
        elif a == '4' or a == '04' : self.isgd()
        elif a == '5' or a == '05' : self.nullpointer()
        else : print("please choose a number from 1 to 5")
    def bitly(self):
        url = input('Enter The Link: ')
        unsh = s.bitly.expand(url)
        print (f'The Unshort link is: {unsh}')
    def chilpit(self):
        url = input('Enter The Link: ')
        unsh = s.chilpit.expand(url)
        print (f'The Unshort Link Is: {unsh} ')
    def clckur(self):
        url = input('Enter The Link: ')
        unsh = s.clckru.expand(url)
        print (f'The Unshort Link Is: {unsh} ')
    def isgd(self):
        url = input('Enter The Link: ')
        unsh = s.isgd.expand(url)
        print (f'The Unshort Link Is: {unsh} ')
    def nullpointer(self):
        url = input('Enter The Link: ')
        unsh = s.nullpointer.expand(url)
        print (f'The Unshort Link Is: {unsh} ')
def introdaction():
    os.system('clear')
    print(Red + pyfiglet.figlet_format("INTRO",font='slant')+ Yellow)
    arch = input(''' 
    [01] SHORTING LINK
    [02] UNSHORTING LINK
    [03] CLEAR HISTORY LOGINS
    
    Enter A Number: ''')
    if arch == '1' or arch == '01' : os.system('clear');shorting()
    elif arch == '2' or arch == '02' : unshort()
    elif arch == '3' or arch == '03': os.system('rm *.txt')
    else : print("please choose a number from 1 to 3 ")
introdaction()
