# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:07:22 2025

@author: IITM
"""
import mysql.connector

myDB = mysql.connector.connect(host = 'localhost', user = 'root', 
                               password = 'root', database = 'testdatabase')

print(myDB)

cursor = myDB.cursor()

#%% Display tables in the selected database
cursor.execute('SHOW TABLES;')

print('Table names:')
for i in cursor:
    print(i)

print('========================')

#%%
try:
    cursor.execute ('CREATE TABLE studentDetails (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(150), department CHAR(5));')
    cursor.execute ('ALTER TABLE studentDetails ADD COLUMN address VARCHAR(150);')  

except:
    pass

#%%
cursor.execute('ALTER TABLE studentDetails AUTO_INCREMENT = 1;')

cursor.execute("INSERT INTO studentDetails(name, department, address) VALUES ('Uramichi','PE', 'Japan')" )

#%%
sqlStatement = 'INSERT INTO studentDetails (name, department, address) VALUES (%s, %s, %s)'
values = [('Lawliet','EEE', 'Sweden'),
          ('Marie','ME', 'Denmark'),
          ('Holmes','CE', 'UK')]

cursor.executemany(sqlStatement, values)

myDB.commit()

print(cursor.rowcount, ' rows were inserted.')

#%%

cursor.execute("INSERT INTO studentDetails(name, department, address) VALUES ('Kita Shinsuke','PE', 'Japan')" )

myDB.commit()

print('1 record inserted. ID: ', cursor.lastrowid)



