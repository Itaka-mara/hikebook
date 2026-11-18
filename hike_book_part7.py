# === Stage 7: Генерация идентификаторов ===
# Project: HikeBook
import uuid
import re


PROJECT_PREFIX = "HKB"


def _is_valid_uuid(value):
    if not isinstance(value, str):
        return False
    try:
        uuid.UUID(value, version=4)
    except (ValueError, AttributeError):
        return False
    return True


def generate_unique_id(length=8):
    if length <= 0:
        raise ValueError("length must be a positive integer")
    base = "0123456789abcdefghijklmnopqrstuvwxyz"
    while True:
        value = "".join(
            base[(uuid.uuid4().int >> (3 * (length - i))) % len(base)]
            for i in range(length)
        )
        if _is_valid_uuid(value):
            return PROJECT_PREFIX + value


def check_collision(existing_ids, new_id):
    return new_id in existing_ids


def make_unique_id(existing_ids, length=8):
    new_id = generate_unique_id(length)
    while check_collision(existing_ids, new_id):
        new_id = generate_unique_id(length)
    return new_id


def get_unused_id(existing_ids, length=8):
    new_id = make_unique_id(existing_ids, length)
    return new_id
