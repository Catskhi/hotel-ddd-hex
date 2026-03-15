from typing import Protocol

class GuestRepository(Protocol):
    def save(self, guest) -> None:
        """Saves a guest to the repository."""
        pass

    def get_by_id(self, guest_id: str):
        """Finds a guest by its ID."""
        pass