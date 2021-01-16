from datetime import datetime

from peewee import *


database = SqliteDatabase(None)


class User(Model):
    first_name = CharField(max_length=128, null=True)
    last_name = CharField(max_length=128, null=True)
    national_id = CharField(max_length=32, unique=True, primary_key=True)
    birth_date = DateField(null=True)
    birth_place = CharField(max_length=128, null=True)
    job = CharField(max_length=128, null=True)

    class Meta:
        database = database


class BankAccount(Model):
    user = ForeignKeyField(User, backref="bank_accounts")
    bank_name = CharField(max_length=128, null=True)
    sheba_id = CharField(max_length=128, null=True)
    account_id = CharField(primary_key=True, unique=True, max_length=128, null=True)

    class Meta:
        database = database


class House(Model):
    user = ForeignKeyField(User, backref="houses")
    price = IntegerField(null=True)
    postal_code = CharField(primary_key=True, unique=True, max_length=128)
    area = IntegerField(null=True)
    address = CharField(max_length=128, null=True)

    class Meta:
        database = database


class Car(Model):
    user = ForeignKeyField(User, backref="cars")
    Plaquecar = CharField(primary_key=True, unique=True, max_length=128)
    model = CharField(max_length=128, null=True)
    color = CharField(max_length=128, null=True)

    class Meta:
        database = database


class PhoneNumber(Model):
    user = ForeignKeyField(User, backref="phone_numbers")
    phone_number = CharField(primary_key=True, unique=True, max_length=128)
    operator = CharField(max_length=128, null=True)

    class Meta:
        database = database


class Deed(Model):
    id = CharField(primary_key=True, unique=True, max_length=128)

    user = ForeignKeyField(User, backref="deeds")
    car = ForeignKeyField(Car, backref="deeds", null=True)
    house = ForeignKeyField(House, backref="deeds", null=True)
    amount = IntegerField(null=True)

    date_created = DateTimeField(default=datetime.now())

    class Meta:
        database = database


class Transaction(Model):
    id = CharField(primary_key=True, unique=True, max_length=128)

    from_account = ForeignKeyField(BankAccount, backref="from_accounts")
    to_account = ForeignKeyField(BankAccount, backref="to_accounts")
    amount = IntegerField(null=True)

    date_created = DateTimeField(default=datetime.now())

    class Meta:
        database = database


class CallLog(Model):
    id = PrimaryKeyField()

    from_number = ForeignKeyField(PhoneNumber, backref="outgoing_calls")
    to_number = ForeignKeyField(PhoneNumber, backref="incoming_calls")

    duration = TimeField()  # should be a `DurationField` in other databases but peewee does not support that
    date_created = DateTimeField(default=datetime.now())

    class Meta:
        database = database


class Relationship(Model):
    id = CharField(primary_key=True, unique=True, max_length=128)  # Combination of the related people's national_id

    person_1 = ForeignKeyField(User, backref="person_1s")
    person_2 = ForeignKeyField(User, backref="person_2s")

    relation = CharField(max_length=128, null=True)

    date_created = DateTimeField(default=datetime.now())

    class Meta:
        database = database
