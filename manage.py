import logging
import sys

from views import *
from views.destroy_database import destroy_database
from views.find_users_who_took_money import find_users_who_took_money


def load_environment():
    from dotenv import load_dotenv

    load_dotenv()

    # OR, the same with increased verbosity:
    load_dotenv(verbose=True)

    # OR, explicitly providing path to '.env'
    from pathlib import Path  # python3 only

    env_path = Path(".") / ".env"
    load_dotenv(dotenv_path=env_path)


if __name__ == "__main__":
    load_environment()
    initial_database()

    if "--load-data" in sys.argv:
        fill_data_from_csv()

    users_who_took_bribes = find_users_who_took_bribes()
    users_who_took_money = find_users_who_took_money(users_who_took_bribes)
    find_users_who_have_been_called_by_smugglers(users_who_took_money)

    if "--remove-db" in sys.argv:
        destroy_database()



