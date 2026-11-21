# === Stage 8: Фильтрация записей ===
# Project: HikeBook
from datetime import date


def filter_hikes_by_region(hikes, region):
    return [hike for hike in hikes if hike.get("region") == region]


def filter_hikes_by_date_range(hikes, start_date, end_date):
    return [
        hike
        for hike in hikes
        if start_date <= hike.get("date") <= end_date
    ]


def filter_hikes(hikes, region=None, start_date=None, end_date=None):
    result = hikes
    if region is not None:
        result = filter_hikes_by_region(result, region)
    if start_date is not None:
        result = filter_hikes_by_date_range(result, start_date, end_date)
    return result


def parse_date(date_str):
    return date.fromisoformat(date_str.strip())


def filter_hikes_cli(hikes, args):
    filters = {}
    for arg in args:
        if arg.startswith("--region="):
            filters["region"] = arg.split("=", 1)[1]
        elif arg.startswith("--from="):
            filters["start_date"] = parse_date(arg.split("=", 1)[1])
        elif arg.startswith("--to="):
            filters["end_date"] = parse_date(arg.split("=", 1)[1])
    return filter_hikes(hikes, **filters)


if __name__ == "__main__":
    sample_hikes = [
        {
            "name": "Горы Шантарала",
            "region": "Арктика",
            "distance": 45.0,
            "difficulty": "высокая",
            "date": "2023-06-15",
        },
        {
            "name": "Волжские пески",
            "region": "Поволжье",
            "distance": 12.0,
            "difficulty": "средняя",
            "date": "2023-07-20",
        },
        {
            "name": "Камчатские вулканы",
            "region": "Дальний Восток",
            "distance": 80.0,
            "difficulty": "экстремальная",
            "date": "2023-08-05",
        },
    ]

    filtered = filter_hikes_cli(sample_hikes, ["--region=Поволжье", "--from=2023-07-01", "--to=2023-08-31"])
    for hike in filtered:
        print(f"{hike['name']} | {hike['region']} | {hike['date']}")
