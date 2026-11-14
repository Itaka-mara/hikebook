# === Stage 5: Удаление и восстановление ===
# Project: HikeBook
import copy


class Hike:
    def __init__(self, name, region, distance, difficulty):
        self.id = self._generate_id()
        self.name = name
        self.region = region
        self.distance = distance
        self.difficulty = difficulty
        self.soft_deleted = False

    def _generate_id(self):
        return len(Hike._id_counter) + 1

    Hike._id_counter = 0

    def delete(self):
        self.soft_deleted = True

    def restore(self):
        self.soft_deleted = False

    def is_deleted(self):
        return self.soft_deleted

    def get_active(self):
        return [h for h in Hike.list if not h.soft_deleted]

    def get_deleted(self):
        return [h for h in Hike.list if h.soft_deleted]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "region": self.region,
            "distance": self.distance,
            "difficulty": self.difficulty,
            "soft_deleted": self.soft_deleted,
        }

    @classmethod
    def from_dict(cls, data):
        hike = cls(data["name"], data["region"], data["distance"], data["difficulty"])
        hike.id = data.get("id", hike.id)
        hike.soft_deleted = data.get("soft_deleted", False)
        return hike


Hike.list = []


def add_hike(name, region, distance, difficulty):
    hike = Hike(name, region, distance, difficulty)
    Hike.list.append(hike)
    return hike


def get_hike(hike_id):
    for hike in Hike.list:
        if hike.id == hike_id and not hike.soft_deleted:
            return hike
    return None


def delete_hike(hike_id):
    hike = get_hike(hike_id)
    if hike:
        hike.delete()
        return True
    return False


def restore_hike(hike_id):
    hike = get_hike(hike_id)
    if hike:
        hike.restore()
        return True
    return False


def list_hikes(active_only=True):
    hikes = Hike.list
    if active_only:
        hikes = [h for h in hikes if not h.soft_deleted]
    return hikes


def delete_hike_permanent(hike_id):
    hike = get_hike(hike_id)
    if hike:
        Hike.list.remove(hike)
        return True
    return False


def snapshot():
    return copy.deepcopy(Hike.list)


def restore_snapshot(snapshot_data):
    Hike.list.clear()
    for data in snapshot_data:
        Hike.list.append(Hike.from_dict(data))
