from peewee import *

db  = SqliteDatabase("dairy.db")

menu = OrderedDict([
			('A', add_entry),
			('D', del_entry),
			('E', edit_entry),
			('Q', exit)])

class Diary(Model):
	user = CharField(max_length = 50)
	timestamp = DateTime(default = datetime.datetime.now)
	notes = TextField()
	
	class Meta():
		database = db
	
def menu():
	
	while True:
		print("Please select one of the following options:\n")
		for key,value in menu:
			print("{}: {}".format(key, if value.__doc__ else "Quit"))
		usr_inp = input("> ").upper()
		
		if usr_inp in menu:
			menu[usr_inp]()
			
def add_entry():
	"""Add an entry"""

def del_entry():
	"""Delete an entry"""

def edit_entry():
	"""Edit an entry"""
			
if __name__  ==  '__main__()':
	db.connect()
	db.create_tables([notes], safe = True)