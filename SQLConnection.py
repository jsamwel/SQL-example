# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 18:30:02 2018

@author: JSamwel
"""

import psycopg2

class Connection:
    def __init__(self, Host, user, password, database):        
        self.hostname = Host
        self.username = user
        self.password = password
        self.DB = database
        
    def Insert(self, Data=[]):    
        sql = """INSERT INTO products VALUES(%s, %s, %s, %s);"""
        
        self.cur.execute(sql, (int(Data[0]), Data[1], Data[2], Data[3]))
        
        self.conn.commit()
        
    def Fetch(self):
        self.cur.execute("SELECT * FROM products")
        rows = self.cur.fetchall()
        
        return rows
    
    def Connect(self):
        self.conn = psycopg2.connect(database=self.DB, user=self.username, 
                                     password=self.password)
        self.cur = self.conn.cursor()        
        
    def DisConnect(self):
        self.conn.close()
        