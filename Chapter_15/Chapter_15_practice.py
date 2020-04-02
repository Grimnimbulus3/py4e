import sqlite3

conn = sqlite3.connect('Assignment1.sqlite')

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('''CREATE TABLE Ages  (
  name VARCHAR(128),
  age INTEGER
)''')

cur.execute('DELETE FROM Ages';
cur.execute('INSERT INTO Ages (name, age) VALUES (''Aamirah'', 31)')
cur.execute('INSERT INTO Ages (name, age) VALUES (''Rahil'', 37)')
cur.execute('INSERT INTO Ages (name, age) VALUES (''Mira'', 31)')
cur.execute('INSERT INTO Ages (name, age) VALUES (''Haley'', 29)')
cur.execute('INSERT INTO Ages (name, age) VALUES (''Evie'', 15)')
cur.execute('INSERT INTO Ages (name, age) VALUES (''Simbiat'', 24)')
cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
conn.commit()

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)
    cur.execute('DELETE FROM Tracks WHERE plays < 100')

conn.close()
