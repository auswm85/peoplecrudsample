from peewee import *
import os
db = SqliteDatabase(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'people.db'))


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
