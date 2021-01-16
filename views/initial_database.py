from models import *


def initial_database():
    from os import getenv

    database.init(getenv("DATABASE"))
    database.connect()
    database.create_tables(
        [
            User,
            BankAccount,
            House,
            Car,
            PhoneNumber,
            Deed,
            Transaction,
            CallLog,
            Relationship,
        ]
    )
