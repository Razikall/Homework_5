import random
import string


def random_string(lenght=5):
    return "".join([random.choice(string.ascii_letters) for _ in range(lenght)])


def random_email():
    return random_string() + "@" + random_string(5) + "." + random.choice(["com", "org", "ru"])
