from typing import Protocol

from domain.entities.guest import Guest


class GuestRepository(Protocol):
    async def save(self, guest: Guest) -> None: ...

    async def get_by_id(self, guest_id: int) -> Guest | None: ...
