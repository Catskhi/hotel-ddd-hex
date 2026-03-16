from domain.entities.reservation import Reservation
from domain.value_objects.date_range import DateRange
from application.ports.reservation_repository import ReservationRepository

class CreateReservation():
    def __init__(self, reservation_repository: ReservationRepository) -> None:
        self._reservation_repository = reservation_repository  

    async def execute(
            self,
            reservation_id: str,
            guest_id: str,
            room_id: str,
            check_in: DateRange,
            check_out: DateRange
    ) -> Reservation:
        stay_period = DateRange(check_in, check_out)
        for existing in await self._reservation_repository.get_active_by_room(room_id):
            if existing.stay_period.overlaps(stay_period):
                raise ValueError("The room is already booked for the selected dates")
        reservation = Reservation.create(reservation_id, guest_id, room_id, stay_period)
        await self._reservation_repository.save(reservation)
        return reservation