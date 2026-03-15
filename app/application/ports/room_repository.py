from typing import Protocol

class RoomRepository(Protocol):
    def save(self, room) -> None:
        """Saves a room to the repository."""
        pass

    def get_by_id(self, room_id: str):
        """Finds a room by its ID."""
        pass