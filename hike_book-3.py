# === Stage 3: Хранилище в памяти ===
# Project: HikeBook
memory_hike.py

from typing import Dict, List, Optional


class Hike:
    def __init__(self, name: str, region: str, distance: float, difficulty: str):
        self.id = None
        self.name = name
        self.region = region
        self.distance = distance
        self.difficulty = difficulty


class HikeMemoryStore:
    def __init__(self):
        self._hikes: Dict[str, Hike] = {}
        self._counter = 0

    def add(self, hike: Hike) -> Hike:
        self._counter += 1
        hike.id = str(self._counter)
        self._hikes[hike.id] = hike
        return hike

    def get(self, hike_id: str) -> Optional[Hike]:
        return self._hikes.get(hike_id)

    def list_all(self) -> List[Hike]:
        return list(self._hikes.values())
