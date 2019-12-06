from peewee import *

db = SqliteDatabase('notofocations.db')

class TextNotification(Model):
    payload = CharField()
    time = DateField()

    class Meta:
        database = db  # модель будет использовать базу данных 'people.db'