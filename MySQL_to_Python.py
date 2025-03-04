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

cursor.execute("INSERT INTO studentDetails(name, department, address) VALUES ('Uramichi','PE', 'Japan');" )

#%%
sqlStatement = 'INSERT INTO studentDetails (name, department, address) VALUES (%s, %s, %s);'
values = [('Lawliet','EEE', 'Sweden'),
          ('Marie','ME', 'Denmark'),
          ('Holmes','CE', 'UK')]

cursor.executemany(sqlStatement, values)

myDB.commit()

print(cursor.rowcount, ' rows were inserted.')

#%%

cursor.execute("INSERT INTO studentDetails(name, department, address) VALUES ('Kita Shinsuke','PE', 'Japan');" )

myDB.commit()

print('1 record inserted. ID: ', cursor.lastrowid)

#%%

cursor.execute('SELECT * FROM studentDetails;')

allFetched = cursor.fetchall()

for i in allFetched:
    print(i)
    
"""
Output:
(1, 'Uramichi', 'PE', 'Japan')
(2, 'Lawliet', 'EEE', 'Sweden')
(3, 'Marie', 'ME', 'Denmark')
(4, 'Holmes', 'CE', 'UK')
(5, 'Kita Shinsuke', 'PE', 'Japan')
"""

#%%

cursor.execute('SELECT name, department FROM studentDetails;')

check = cursor.fetchall()

for i in check:
    print(i)

"""
Output:
('Uramichi', 'PE')
('Lawliet', 'EEE')
('Marie', 'ME')
('Holmes', 'CE')
('Kita Shinsuke', 'PE')

"""
#%%

cursor.execute('ALTER TABLE studentDetails ADD COLUMN gpa FLOAT(4);')

myDB.commit()

cursor.execute('SELECT * FROM studentDetails;')

allCols = cursor.fetchall()

for i in allCols:
    print(i)

"""
Output:
(1, 'Uramichi', 'PE', 'Japan', None)
(2, 'Lawliet', 'EEE', 'Sweden', None)
(3, 'Marie', 'ME', 'Denmark', None)
(4, 'Holmes', 'CE', 'UK', None)
(5, 'Kita Shinsuke', 'PE', 'Japan', None)
"""

#%%
cursor.execute('SELECT * FROM studentDetails;')

x = cursor.fetchone()

print(x)

"""
Output:
(1, 'Uramichi', 'PE', 'Japan', None)
"""

#%%
cursor.execute('SELECT * FROM studentDetails WHERE address = "UK";')

x = cursor.fetchall()

for i in x:
    print(i)

"""
Output:

(4, 'Holmes', 'CE', 'UK', None)

"""
#%%
cursor.execute('SELECT * FROM StudentDetails WHERE department LIKE "%p%";')

x = cursor.fetchall()

print(x)

"""
Output:
[(1, 'Uramichi', 'PE', 'Japan', None), (5, 'Kita Shinsuke', 'PE', 'Japan', None)]
"""

#%%


