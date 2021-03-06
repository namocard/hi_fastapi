import uuid


def generate_unique_int():
    return uuid.uuid4().int >> 90
