import sqlite3

conn = sqlite3.connect('Assignment_15_2.sqlite')

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')

cur = conn.cursor()
create_query = """
CREATE TABLE Counts (org TEXT, count INTEGER)
"""
cur.execute(create_query)

print('Just press enter')
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'C:\\Users\\fyohn3\\github\\py4e\\Sample_Data\\mbox.txt' #C:\Users\fyohn3\github\py4e\Sample_Data\mbox-short.txt
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    sub_pieces = email.split('@')
    org = sub_pieces[1]
    #print(org)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute("""INSERT INTO Counts (org, count)
                VALUES (?, 1)""", (org,))
    else:
        cur.execute("""UPDATE Counts
        SET count = count + 1 WHERE org = ?""", (org,))
conn.commit()
