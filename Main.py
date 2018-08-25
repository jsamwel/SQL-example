# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 18:25:04 2018

@author: JSamwel
"""

import tkinter as tk
from tkinter import ttk
from ttkthemes import themed_tk

from SQLConnection import Connection
         
class App: 
    hostname = 'localhost'
    username = 'postgres'
    password = 'WWPostgres'
    database = 'DataDevelopment'

    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(self.master)
        self.frame.pack()  
                
        self.master.title("SQL example")
        
        self.selection = tk.StringVar()
        self.selection.trace("w", self.ShowData)
        
        self.ConnectSQL() 
        self.FetchedData = self.SQLDB.Fetch()
        
        self.InitUI()
        
    def ConnectSQL(self):  
        self.SQLDB = Connection(self.hostname, self.username, self.password, self.database)
        self.SQLDB.Connect()
        
    def InitUI(self):
        #Create items for in the GUI
        self.label = ttk.Label(self.frame, text="Insert Data:")
        self.labelID = ttk.Label(self.frame, text="ID:")
        self.labelName = ttk.Label(self.frame, text="Name:")
        self.labelProducer = ttk.Label(self.frame, text="Producer")
        self.labelUseCase = ttk.Label(self.frame, text="Usecase:")
        
        self.Output1 = ttk.Label(self.frame, text="")
        self.Output2 = ttk.Label(self.frame, text="")
        
        self.Choice = ttk.OptionMenu(self.frame, self.selection, "", 
                                 command=self.ShowData)
        
        self.entry1 = ttk.Entry(self.frame)
        self.entry2 = ttk.Entry(self.frame)
        self.entry3 = ttk.Entry(self.frame)
        self.entry4 = ttk.Entry(self.frame)
        
        self.ButtonInsert = ttk.Button(self.frame, text="Insert", width=15, 
                                       command=self.InsertSQL)
        self.ButtonFetch = ttk.Button(self.frame, text="Fetch", width=15, 
                                      command=self.FetchSQL)        
        
        #Place items on screen
        self.label.grid(row=1, column=0, sticky='w', padx=5)        
        self.labelID.grid(row=0, column=1)
        self.labelName.grid(row=0, column=2)
        self.labelProducer.grid(row=0, column=3)
        self.labelUseCase.grid(row=0, column=4)
        
        self.Output1.grid(row=3, column=3)
        self.Output2.grid(row=3, column=4)
        
        self.Choice.grid(row=3, column=2)
        
        self.entry1.grid(row=1, column=1, padx=1)
        self.entry2.grid(row=1, column=2, padx=1)
        self.entry3.grid(row=1, column=3, padx=1)
        self.entry4.grid(row=1, column=4, padx=1)
        
        self.ButtonInsert.grid(row=1, column=5, sticky='e', padx=5)
        self.ButtonFetch.grid(row=3, column=5, sticky='e', padx=5)
        
        #Enlarge empty space between fetch and insert
        self.frame.grid_rowconfigure (2, minsize=20)
        
    def InsertSQL(self):
        Data = [self.entry1.get(), self.entry2.get(), self.entry3.get(), 
                self.entry4.get()]
        
        self.SQLDB.Insert(Data)
        
    def FetchSQL(self):
        self.selection.set('')        
        self.FetchedData = self.SQLDB.Fetch()
        
        self.Choice['menu'].delete(0, 'end')
        
        for choice in self.FetchedData:
            self.Choice['menu'].add_command(label=choice[1], command=tk._setit(self.selection, choice[1]))
        
        self.selection.set(self.FetchedData[0][1])
        
    def ShowData(self, *args):     
        for x in self.FetchedData:
            if x[1] == self.selection.get():
                self.Output1.config(text=x[2])
                self.Output2.config(text=x[3])          
                               
def main():
  
    root = themed_tk.ThemedTk()
    #root.geometry("250x150+300+300")
    Window = App(root)
    root.set_theme("equilux") 
    
    root.mainloop() 
    
    Window.SQLDB.DisConnect()
    
if __name__ == '__main__':
    main()  