import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='abc123', db='menagerie')
j = conn.cursor()

j.execute("SELECT owner,COUNT(*) FROM pet group by owner")

for thing in j.fetchall():
    print(thing)
