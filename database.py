import sqlite3
con = sqlite3.connect('database.db')
cur = con.cursor()


def createConnection():
    global con
    global cur
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    
    
def closeConnection():
    con.close()
    
    
def logRetrive():
    createConnection()
    with con:
        cur.execute('SELECT * FROM logs WHERE name=:name ', {"name": 'Tree'})
    return cur.fetchall()


def logAdd(date, hours, total_hours):
    createConnection()
    with con:
        cur.execute('INSERT INTO logs VALUES (:date, :hours, :name, :totalHours)', {"date": date, "hours": hours, "name": 'Tree', "totalHours": total_hours})




# cur.execute('''CREATE TABLE logs
#                (date text, hours text, name text, totalHours text)''')
# logAdd('test1', 'test2', '90')
# print(logRetrive())

# print(divmod(300, 300))

con.commit()
closeConnection()
