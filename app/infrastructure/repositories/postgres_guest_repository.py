from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.guest import Guest
from infrastructure.database.models import GuestModel


class PostgresGuestRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(self, guest: Guest) -> None:
        model = GuestModel(
            id=guest.id,
            name=guest.name,
            email=guest.email,
            phone=guest.phone,
        )
        self._session.add(model)
        await self._session.commit()

    async def get_by_id(self, guest_id: int) -> Guest | None:
        result = await self._session.execute(
            select(GuestModel).where(GuestModel.id == guest_id)
        )
        model = result.scalar_one_or_none()
        if model is None:
            return None
        return Guest(id=model.id, name=model.name, email=model.email, phone=model.phone)
