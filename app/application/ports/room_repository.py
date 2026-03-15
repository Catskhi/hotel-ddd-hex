from typing import Protocol

from domain.entities.room import Room


class RoomRepository(Protocol):
    async def save(self, room: Room) -> None: ...

    async def get_by_id(self, room_id: str) -> Room | None: ...
