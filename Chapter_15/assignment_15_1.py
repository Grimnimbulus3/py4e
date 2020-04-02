import sqlite3

conn = sqlite3.connect('Assignment1.sqlite')

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('''CREATE TABLE Ages  (
  name VARCHAR(128),
  age INTEGER
)''')

cur.execute('DELETE FROM Ages')

insert_query = """Insert into Ages (name, age) VALUES ('Aamirah', 31);"""
cur.execute(insert_query)
insert_query = """INSERT INTO Ages (name, age) VALUES ('Rahil', 37);"""
cur.execute(insert_query)
insert_query = """INSERT INTO Ages (name, age) VALUES ('Mira', 31);"""
cur.execute(insert_query)
insert_query = """INSERT INTO Ages (name, age) VALUES ('Haley', 29);"""
cur.execute(insert_query)
insert_query = """INSERT INTO Ages (name, age) VALUES ('Evie', 15);"""
cur.execute(insert_query)
insert_query = """INSERT INTO Ages (name, age) VALUES ('Simbiat', 24);"""
cur.execute(insert_query)
#INSERT INTO Ages (name, age) VALUES ('Rahil', 37);
#INSERT INTO Ages (name, age) VALUES ('Mira', 31);
#INSERT INTO Ages (name, age) VALUES ('Haley', 29);
#INSERT INTO Ages (name, age) VALUES ('Evie', 15);
#INSERT INTO Ages (name, age) VALUES ('Simbiat', 24);


cur.execute(insert_query)

hex_command = """
SELECT hex(name || age) AS X
FROM Ages
ORDER BY X
"""

results = cur.execute(hex_command)
print(results)



#cur.execute("""INSERT INTO Ages (name, age) VALUES ('Aamirah', 31)')
#cur.execute('INSERT INTO Ages (name, age) VALUES ('Rahil', 37)')
#cur.execute('INSERT INTO Ages (name, age) VALUES ('Mira', 31)')
#cur.execute('INSERT INTO Ages (name, age) VALUES ('Haley', 29)')
#cur.execute('INSERT INTO Ages (name, age) VALUES ('Evie', 15)')
#cur.execute('INSERT INTO Ages (name, age) VALUES ('Simbiat', 24)')
#cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')


conn.commit()

conn.close()
