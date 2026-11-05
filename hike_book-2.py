# === Stage 2: Проверка полей ===
# Project: HikeBook
import re


HARDNESS_LEVELS = {1, 2, 3, 4}


def normalize_text(value):
    text = str(value).strip()
    text = re.sub(r"[^\w\s.,]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_distance(value):
    text = str(value).strip()
    match = re.search(r"([0-9]*\.?[0-9]+)", text)
    if match is None:
        raise ValueError("Дистанция должна содержать число")
    number = float(match.group())
    if number <= 0:
        raise ValueError("Дистанция должна быть положительной")
    return number


def normalize_hardness(value):
    text = str(value).strip().lower()
    replacements = {
        "легко": 1,
        "средне": 2,
        "сложно": 3,
        "экстрим": 4,
        "очень сложно": 4,
        "очень трудно": 4,
    }
    if text in replacements:
        return replacements[text]
    if text.isdigit():
        level = int(text)
        if level in HARDNESS_LEVELS:
            return level
    raise ValueError("Сложность должна быть от 1 до 4")


def validate_hike(name, region, distance, hardness):
    name = normalize_text(name)
    if not name:
        raise ValueError("Название похода не может быть пустым")

    region = normalize_text(region)
    if not region:
        raise ValueError("Регион не может быть пустым")

    distance = normalize_distance(distance)
    if distance > 1000:
        raise ValueError("Дистанция превышает разумный максимум")

    hardness = normalize_hardness(hardness)

    return name, region, distance, hardness
