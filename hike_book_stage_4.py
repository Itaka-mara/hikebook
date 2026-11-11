# === Stage 4: Редактирование записей ===
# Project: HikeBook
from collections import OrderedDict


class HikeEditError(Exception):
    """Ошибка при редактировании похода: неизвестное поле или недопустимое значение."""


class Hike:
    """Поход: название, регион, дистанция, сложность."""

    _ALLOWED_FIELDS = ("name", "region", "distance", "difficulty")

    def __init__(self, name, region, distance, difficulty):
        self.name = name
        self.region = region
        self.distance = distance
        self.difficulty = difficulty

    def apply_edit(self, changes):
        """Применить изменения к сущности по списку допустимых полей.

        changes - dict вида {field: new_value}.
        Неизвестные поля отбрасываются с предупреждением.
        Значения, не являющиеся строкой или числом, отбрасываются.
        Возвращает список применённых изменений.
        """
        applied = OrderedDict()
        for field, new_value in changes.items():
            if field not in self._ALLOWED_FIELDS:
                print(f"Предупреждение: игнорирую неизвестное поле {field!r}.")
                continue
            if not isinstance(new_value, (str, int, float)):
                print(f"Предупреждение: игнорирую недопустимое значение для {field!r}.")
                continue
            old_value = getattr(self, field)
            setattr(self, field, new_value)
            applied[field] = (old_value, new_value)
        return applied

    def to_dict(self):
        return {
            "name": self.name,
            "region": self.region,
            "distance": self.distance,
            "difficulty": self.difficulty,
        }


def edit_hike_by_id(hikes, hike_id, changes):
    """Редактировать поход по идентификатору.

    hikes - dict {id: Hike}. Возвращает обновлённую сущность или None.
    """
    if hike_id not in hikes:
        print(f"Поход с id={hike_id!r} не найден.")
        return None
    hikes[hike_id].apply_edit(changes)
    return hikes[hike_id]


if __name__ == "__main__":
    demo = {
        1: Hike("Горная тропа", "Кавказ", 15.0, 3),
        2: Hike("Речной берег", "Полесье", 5.0, 1),
    }
    edit_hike_by_id(demo, 1, {"name": "Горная тропа 2", "color": "red"})
    edit_hike_by_id(demo, 99, {"name": "X"})
    print(demo[1].to_dict())
