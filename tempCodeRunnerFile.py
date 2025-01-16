import sqlite3

db = sqlite3.connect("data/database.db", check_same_thread=False)
cursor = db.cursor()

#drop tabel finansial data

command = "DROP TABLE IF EXISTS finansial"
cursor.execute(command)
db.commit()
command = "DROP TABLE IF EXISTS hamauliateon"
cursor.execute(command)
db.commit()
command = "DROP TABLE IF EXISTS bulanan"
cursor.execute(command)
db.commit()
command = "DROP TABLE IF EXISTS pemasukan"
cursor.execute(command)
db.commit()
command = "DROP TABLE IF EXISTS pengeluaran"
cursor.execute(command)
db.commit()
# command = "DELETE FROM finansial WHERE id=?"
# param = (3,)
# cursor.execute(command, param)
# db.commit()