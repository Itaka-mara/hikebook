# === Stage 6: Связанная сущность ===
# Project: HikeBook
from dataclasses import dataclass, field
from typing import List, Optional

from hikebook_core.entities.hike import Hike
from hikebook_core.repository.base import BaseRepository


class StopRepository(BaseRepository):
    def __init__(self, storage: dict):
        self._storage = storage
        self._index = {}

    def add(self, hike: Hike, name: str, description: str = "") -> int:
        hike_id = hike.id
        if hike_id not in self._index:
            self._index[hike_id] = []
        stop = Stop(hike_id=hike_id, name=name, description=description)
        self._storage[f"stop_{stop.id}"] = stop
        self._index[hike_id].append(stop)
        return stop.id

    def get_by_hike(self, hike_id: int) -> List["Stop"]:
        return list(self._index.get(hike_id, []))


@dataclass
class Stop:
    id: int
    hike_id: int
    name: str
    description: str = ""
