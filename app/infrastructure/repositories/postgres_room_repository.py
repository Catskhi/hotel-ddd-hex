from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.room import Room
from infrastructure.database.models import RoomModel


class PostgresRoomRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(self, room: Room) -> None:
        model = RoomModel(
            room_id=room.room_id,
            number=room.room_number,
            capacity=room.capacity,
        )
        self._session.add(model)
        await self._session.commit()

    async def get_by_id(self, room_id: str) -> Room | None:
        result = await self._session.execute(
            select(RoomModel).where(RoomModel.room_id == room_id)
        )
        model = result.scalar_one_or_none()
        if model is None:
            return None
        return Room(room_id=model.room_id, number=model.number, capacity=model.capacity)
