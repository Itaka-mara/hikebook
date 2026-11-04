# === Stage 1: Каркас модуля ===
# Project: HikeBook
from dataclasses import dataclass, field
from typing import List


@dataclass
class Hike:
    name: str
    region: str
    distance: float
    difficulty: str


def create_sample_hikes() -> List[Hike]:
    return [
        Hike(name="Хребет Тавр", region="Крым", distance=12.5, difficulty="средняя"),
        Hike(name="Водлодzersk", region="Карелия", distance=18.0, difficulty="высокая"),
        Hike(name="Холмы Подмосковья", region="МО", distance=7.2, difficulty="низкая"),
    ]


def main() -> None:
    hikes = create_sample_hikes()
    print("HikeBook: дневник походов")
    print(f"Демо-записей: {len(hikes)}")
    for hike in hikes:
        print(f"  {hike.name} | {hike.region} | {hike.distance} км | {hike.difficulty}")


if __name__ == "__main__":
    main()
