from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
  firstname = CharField()
  lastname = CharField()
  birthday = DateField()
  zipcode = CharField()

  def serialize(self):
    return {
      'id': self.id,
      'firstname': self.firstname,
      'lastname': self.lastname,
      'birthday': self.birthday.strftime('%m-%d-%Y'),
      'zipcode': self.zipcode
    }

  class Meta:
    database = db