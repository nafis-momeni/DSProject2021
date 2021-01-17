from models import Deed, Relationship, User, Transaction, BankAccount

from datetime import timedelta, datetime


def is_user_has_any_deed(user: User) -> bool:
    return (
        Deed.select()
        .where((Deed.user == user) & (Deed.date_created >= datetime.now() - timedelta(days=2 * 365)))
        .exists()
    )


def find_users_who_took_bribes():
    users_who_took_bribes = set()

    for user in User.select():
        if user.job in ["سازمان بنادر", "گمرک"]:

            if is_user_has_any_deed(user):
                users_who_took_bribes.add(user)

            else:
                for relation in Relationship.select().where(
                    (Relationship.person_1 == user) or (Relationship.person_2 == user)
                ):
                    is_person_1_has_any_deed = is_user_has_any_deed(relation.person_1)
                    is_person_2_has_any_deed = is_user_has_any_deed(relation.person_2)

                    if is_person_1_has_any_deed or is_person_2_has_any_deed:
                        users_who_took_bribes.add(user)
                        break

    for user in users_who_took_bribes:
        print(
            user.first_name,
            user.last_name,
            "with national_id",
            user.national_id,
            "working in",
            user.job,
            "has been took some bribes.",
        )
    print(f"⭕️ Totally {len(users_who_took_bribes)} users has been took bribes.\n")

