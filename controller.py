from Tkinter import *
from ftplib import FTP
from time import gmtime, strftime
from os import remove

def update():
    comando = strftime("[%H:%M:%S]  ", gmtime()) + command.get()
    mylist.insert(END, comando)
    name_file = "command.txt"
    f = open(name_file, "wb")
    f.write(command.get())
    f.close()
    ftp.delete(name_file)
    file = open(name_file,'rb')
    ftp.storbinary('STOR command.txt', file)
    file.close()
    remove(name_file)



global ftp
ftp = FTP('url_ftp')
ftp.login("mioutente", "miapassword")
root = Tk()
root.title("RemoteControl Server")
root.resizable(False,False)
root.geometry("440x300")
root.configure(bg = "white")
scrollbar = Scrollbar(root, bg = "white")
ltext = Label(root, text = "RemoteControl Server",font = ("Arial", 20, "bold"), bg = "white")
mylist = Listbox(root, yscrollcommand = scrollbar.set, bg = "white", width = 50)
l1 = Label(root, text =  "Inserisci il comando:", bg = "white")
command = StringVar(value = "")
e1 = Entry(root, textvariable = command, bg = "white", width = 39)
bt1 = Button(root, text = "Send", bg = "white", command = update)

ltext.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
scrollbar.grid(row = 1, column = 3, pady = 10, sticky = W, ipady = 68)
mylist.grid(row = 1, column = 0, columnspan = 3, pady = 10, sticky = E)
scrollbar.config(command= mylist.yview)
#l1.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = E)
e1.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = W)
bt1.grid(row = 2, column = 2, padx = 10, pady = 10, sticky = W)
root.mainloop()
