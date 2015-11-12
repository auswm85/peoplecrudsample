from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
	firstname = CharField()
	lastname = CharField()
	birthday = DateField()
	zipcode = CharField()

	class Meta:
		database = db