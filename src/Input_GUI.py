#!/usr/bin/env python

from Tkinter import *
import os
import webbrowser
 
class GUIDemo(Frame,Canvas):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.i = None
        self.userinput = ""
        self.result = ""
        '''
        self.voclist = []
        self.f = open("voc.data", "r")
        for row in self.f:
            s = row[:-1]
            self.voclist.append(s)
        for i in range(len(self.voclist)):
            self.voclist[i].lower()
        '''
 
    def createWidgets(self):
        self.inputText = Label(self)
        self.inputText["text"] = "Input:"
        self.inputText.grid(row=0, column=0)
        self.inputField = Entry(self)
        self.inputField["width"] = 50
        self.inputField["bg"] = "White"
        self.inputField.grid(row=0, column=1, columnspan=6)

        self.search = Button(self)
        self.search["text"] = "Search"
        self.search.grid(row=1, column=0)
        self.search["command"] =  self.searchMethod
        self.search["bg"] = "CornflowerBlue"
        self.search["fg"] = "White"
        
        self.clear = Button(self)
        self.clear["text"] = "Clear"
        self.clear.grid(row=1, column=1)
        self.clear["command"] =  self.clearMethod
        self.clear["bg"] = "CornflowerBlue"
        self.clear["fg"] = "White"

        
        self.URL = Label(self)
        self.URL["text"] = "URL:"
        self.URL.grid(row=2, column=0)
        self.URL = Entry(self)
        self.URL["width"] = 50
        self.URL["bg"] = "White"
        self.URL.grid(row=2, column=1, columnspan=3)

        self.TransText = Label(self)
        self.TransText["text"] = "Translation:"
        self.TransText.grid(row=3, column=0)
        self.TransMSG = Text(self)
        self.TransMSG.insert(1.0,'I am genius :D')
        self.TransMSG["width"] = 50
        self.TransMSG["bg"] = "White"
        self.TransMSG.grid(row=3, column=1)
        
    

    def searchMethod(self):
        self.userinput = self.inputField.get()
        self.URL.delete(0,END)
        self.result = 'http://google.com'
        webbrowser.open(self.result)
        self.URL.insert(0,self.result)
        '''
        temp = self.userinput.split(' ')
        temp2=[]
        for i in range(len(temp)):
            temp[i].lower()
        for i in range(len(temp)):
            check = 0
            for j in range(len(self.voclist)):
                if temp[i] == self.voclist[j]:
                    check = 1
            if check == 0 :
                temp2.append(temp[i])
        br = ' '
        for i in range(len(temp2)-1):
            temp2[i] += br
        for i in range(len(temp2)):
            check = 0
            if temp2[i] == ' ':
                check = 1
            if check == 1:
                del temp2[i]
        str1 = ''.join(temp2)
        self.URL.insert(1.0,str1)
        '''
    
        
    def clearMethod(self):
        self.userinput = ""
        self.inputField.delete(0, 200)
        self.URL.delete(0,END)
        self.TransMSG.delete(1.0,END)

if __name__ == '__main__':
    root = Tk()
    root.option_add("*background", "SteelBlue")
    app = GUIDemo(master=root)
    app.mainloop()
