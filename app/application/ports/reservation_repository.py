from typing import Protocol

from domain.entities.reservation import Reservation


class ReservationRepository(Protocol):
    async def save(self, reservation: Reservation) -> None: ...

    async def get_by_id(self, reservation_id: str) -> Reservation | None: ...

    async def get_active_by_room(self, room_id: str) -> list[Reservation]: ...
