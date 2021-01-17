import os


def destroy_database():
    os.remove(os.getenv("DATABASE"))
