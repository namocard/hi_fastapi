import uuid


def generate_unique_int():
    return uuid.uuid1().int >> 90
