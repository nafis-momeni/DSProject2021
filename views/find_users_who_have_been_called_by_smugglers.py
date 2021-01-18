from models import User, CallLog


def is_user_has_any_call_from_smugglers(user: User) -> bool:
    for call in CallLog.select():
        if call.to_number.user == user:
            if call.from_number.user.job == "قاچاقچی" :
                return True
    return False


def find_users_who_have_been_called_by_smugglers(users_who_took_money: set):
    users_who_have_been_called_by_smugglers = set()
    for user in users_who_took_money:
        if is_user_has_any_call_from_smugglers(user):
            users_who_have_been_called_by_smugglers.add(user)

    for user in users_who_have_been_called_by_smugglers:
        print(
            user.first_name,
            user.last_name,
            "with national_id",
            user.national_id,
            "working in",
            user.job,
            "has been took some money from smugglers.",
        )
    print(f"⭕️ Totally {len(users_who_have_been_called_by_smugglers)} users have been called by smugglers.\n")
    return users_who_have_been_called_by_smugglers
