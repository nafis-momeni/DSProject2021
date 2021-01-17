import functools

from models import User, BankAccount, Transaction, Relationship

users_who_took_money = set()
visited_users = set()


@functools.lru_cache(maxsize=None)
def get_smugglers_bank_accounts() -> set:
    accounts_for_smuggler = set()
    for account in BankAccount.select():
        if account.user.job == "قاچاقچی":
            accounts_for_smuggler.add(account)
    return accounts_for_smuggler


def is_user_took_money_from_smugglers(user: User) -> bool:
    smugglers_accounts = get_smugglers_bank_accounts()
    # TODO: اینجا باگ داریم چرا شو هم نمیدونمیم
    return Transaction.select().where(
        (Transaction.to_account.user in user.bank_accounts.select()) and (Transaction.from_account in smugglers_accounts)
    ).exists()


def dfs(user: User, depth: int):
    visited_users.add(user)
    if is_user_took_money_from_smugglers(user):
        print("   🎈🎈🎈🎈🎈🎈🎈🎈   ")
        users_who_took_money.add(user)

    # Check for ending the bfs
    if depth == 5:
        return

    for relation in Relationship.select().where(Relationship.person_1 == user):
        if relation.person_2 not in visited_users:
            dfs(relation.person_2, depth+1)

    for relation in Relationship.select().where(Relationship.person_2 == user):
        if relation.person_1 not in visited_users:
            dfs(relation.person_1, depth+1)


def find_users_who_took_money(users_who_took_bribes: set):
    # Make sure `users_who_took_money` and `visited_users` are empty at first!
    users_who_took_money.clear()
    visited_users.clear()

    # Start DFS
    for user in users_who_took_bribes:
        dfs(user, depth=0)

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
