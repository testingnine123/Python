#import the module for sqlite
import sqlite3

#create a connection object that would talk to a sqlite file
#in this case, a file named "emaildb.sqlite" is created
conn = sqlite3.connect('emaildb.sqlite')

#like a socket that can send commands
cur = conn.cursor()

#reomve or delete the "Counts" table if it already exists
cur.execute('''
DROP TABLE IF EXISTS Counts''')

#create a table "Counts"
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

#take file name from user
fname = raw_input('Enter file name: ')
if (len(fname) < 1) : fname = 'mbox-short.txt'

fh = open(fname)

for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    #print email

    #check in the DB for the email found in the file...
    #...entered by the user. "?" acts like a placeholder.
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email, ))
    
    try:
        #if email found in the table, just add the count by 1
        #fetchone takes one row from the memory as a list. "[0]" is because...
        #...we selected only the counts from "cur.execute('SELECT count...."
        count = cur.fetchone()[0]
        #print count
        
        #update the count value by one if email already exists in the table
        cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?', (email, ))

    except:
        #if email doesn't exit in table, insert the email, and the count starts from 1
        cur.execute('''INSERT INTO Counts (email, count) VALUES (?, 1 )''', (email, ) )
        
    #commit data in the drive, and not in memory.
    conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

#just to check and print on the terminal
for row in cur.execute(sqlstr) :
    #row[0] is email, and row[1] is count. Convert into string...
    #...in case it has any unicode in it.
    print str(row[0]), row[1]

#close the cursor
cur.close()