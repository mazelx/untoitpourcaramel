from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase('annonces.db')


class Annonce(Model):
    # id = "pap-123456789"
    id = CharField(unique=True, primary_key=True)
    # site = [pap, lbc, logic-immo, seloger]
    site = CharField()
    created = DateTimeField()
    title = CharField()
    description = TextField(null=True)
    price = FloatField()
    charges = FloatField(null=True)
    surface = FloatField()
    rooms = IntegerField()
    bedrooms = IntegerField()
    city = CharField()
    link = CharField()
    picture = CharField(null=True)
    published = BooleanField(default=False)

    class Meta:
        database = db
        order_by = ('-created',)


def create_tables():
    db.connect()
    db.create_table(Annonce, safe=True)
