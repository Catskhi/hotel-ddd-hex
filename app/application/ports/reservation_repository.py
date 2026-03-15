from typing import Protocol

from domain.entities.reservation import Reservation

class ReservationRepository(Protocol):
    def save(self, reservation: Reservation) -> None:
        """Saves a reservation to the repository."""
        pass

    def get_by_id(self, reservation_id: str) -> Reservation | None:
        """Finds a reservation by its ID."""
        pass

    def get_active_by_room(self, room_id: str) -> list[Reservation]:
        """Gets all active reservations for a given room."""
        pass