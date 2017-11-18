import MySQLdb, datetime, time

db = MySQLdb.connect("localhost","discordbot","M54@5ghbX%97*","discord")
c = db.cursor()

def dbconcheck():
	c.execute("SELECT VERSION()")
	result = c.fetchone()
	return result

def dbdiscon():
	db.close()
