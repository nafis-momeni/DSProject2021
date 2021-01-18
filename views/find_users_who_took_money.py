from models import User


# DFS
def is_user_took_money_from_smugglers(user: User, depth) -> bool:
    if depth == 5:
        return False
    for account in user.bank_accounts:
        for transaction in account.to_accounts:
            if transaction.from_account.user.job == "قاچاقچی":
                return True
            if is_user_took_money_from_smugglers(transaction.from_account.user, depth + 1):
                return True
    return False


def find_users_who_took_money(users_who_took_bribes: set):
    # Set a new empty set for users who took money to
    users_who_took_money = set()

    # Start DFS
    for user in users_who_took_bribes:
        if is_user_took_money_from_smugglers(user, depth=1):
            users_who_took_money.add(user)

    for user in users_who_took_money:
        print(
            user.first_name,
            user.last_name,
            "with national_id",
            user.national_id,
            "working in",
            user.job,
            "has been took some money from smugglers.",
        )
    print(f"⭕️ Totally {len(users_who_took_money)} users has been took money from smugglers.\n")

    return users_who_took_money
