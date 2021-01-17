import csv

from models import *


def fill_data_from_csv():

    with open("data/people.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                User.create(
                    first_name=row[0],
                    last_name=row[1],
                    national_id=row[2],
                    birth_date=row[3],
                    birth_place=row[4],
                    job=row[5],
                )
            line_count += 1
        print(f"✅ {line_count} people are added to database.")

    with open("data/accounts.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                BankAccount.create(
                    user=User.get(User.national_id == row[0]),
                    bank_name=row[1],
                    sheba_id=row[2],
                    account_id=row[3],
                )
            line_count += 1
        print(f"✅ {line_count} bank accounts are added to database.")

    with open("data/homes.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                House.create(
                    user=User.get(User.national_id == row[0]),
                    price=row[1],
                    postal_code=row[2],
                    area=row[3],
                    address=row[4],
                )
            line_count += 1
        print(f"✅ {line_count} houses are added to database.")

    with open("data/cars.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                Car.create(
                    user=User.get(User.national_id == row[1]),
                    plaque=row[0],
                    model=row[2],
                    color=row[3],
                )
            line_count += 1
        print(f"✅ {line_count} cars are added to database.")

    with open("data/phones.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                PhoneNumber.create(
                    user=User.get(User.national_id == row[0]),
                    phone_number=row[1],
                    operator=row[2],
                )
            line_count += 1
        print(f"✅ {line_count} phone numbers are added to database.")

    with open("data/ownerships.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                if row[1].replace("-", "").isnumeric():
                    Deed.create(
                        user=User.get(User.national_id == row[0]),
                        house=House.get(House.postal_code == row[1]),
                        id=row[2],
                        amount=row[4],
                        date_created=row[3],
                    )
                else:
                    Deed.create(
                        user=User.get(User.national_id == row[0]),
                        car=Car.get(Car.plaque == row[1]),
                        id=row[2],
                        amount=row[4],
                        date_created=row[3],
                    )
            line_count += 1
        print(f"✅ {line_count} Deeds are added to database.")

    with open("data/transactions.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                from_account: BankAccount = BankAccount.get(BankAccount.account_id == row[0])
                to_account: BankAccount = BankAccount.get(BankAccount.account_id == row[1])
                Transaction.create(
                    id=row[2],
                    from_account=from_account,
                    to_account=to_account,
                    relation=row[2],
                    date_created=row[3],
                    amount=row[4],
                )
            line_count += 1
        print(f"✅ {line_count} transaction are added to database.")

    with open("data/calls.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                from_number: PhoneNumber = PhoneNumber.get(PhoneNumber.phone_number == row[0])
                to_number: PhoneNumber = PhoneNumber.get(PhoneNumber.phone_number == row[1])
                CallLog.create(
                    from_number=from_number,
                    to_number=to_number,
                    id=row[2],
                    date_created=row[3],
                    duration=row[4],
                )
            line_count += 1
        print(f"✅ {line_count} calls are added to database.")

    with open("data/relationships.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                person_1: User = User.get(User.national_id == row[0])
                person_2: User = User.get(User.national_id == row[1])
                Relationship.create(
                    id="-".join([person_1.national_id, person_2.national_id, str(line_count)]),
                    person_1=person_1,
                    person_2=person_2,
                    relation=row[2],
                    date=row[3],
                )
            line_count += 1
        print(f"✅ {line_count} relationships are added to database.")

    print("⭕️ Database Successfully Updated.\n")
