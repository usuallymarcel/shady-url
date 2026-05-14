import random
import string

WORDS = [
    "login",
    "verify",
    "secure",
    "auth",
    "session",
    "update",
]

def random_token(length=6):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_url_path():
    return f"{random.choice(WORDS)}-{random_token(random.randint(6, 12))}-{random.choice(WORDS)}"