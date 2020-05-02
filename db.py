import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Email_Counts')
cur.execute('''CREATE TABLE Email_Counts(email TEXT, Mailcount INTEGER)''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'

fh = open(fname)

for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    mail = pieces[1]

    cur.execute('SELECT Mailcount FROM Email_Counts WHERE email = ? ', (mail,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Email_Counts(email, Mailcount) VALUES(?, 1)''', (mail,))
    else:
        cur.execute('UPDATE Email_Counts SET Mailcount = Mailcount + 1 WHERE email = ?', (mail,))

    conn.commit()

sqlstr = 'SELECT email, Mailcount FROM Email_Counts ORDER BY Mailcount DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
