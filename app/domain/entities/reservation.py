from domain.enums.reservation_status import ReservationStatus
from domain.value_objects.date_range import DateRange

class Reservation():
    def __init__(self, reservation_id: str, guest_id: str, room_id: str, stay_period: DateRange):
        self._reservation_id = reservation_id
        self._guest_id = guest_id
        self._room_id = room_id
        self._stay_period = stay_period
        self._status = ReservationStatus.PENDING

    @classmethod
    def create(cls, reservation_id: str, guest_id: str, room_id: str, stay_period: DateRange):
        if not reservation_id:
            raise ValueError("Reservation ID cannot be empty")
        if not guest_id:
            raise ValueError("Guest ID cannot be empty")
        if not room_id:
            raise ValueError("Room ID cannot be empty")
        if stay_period is None:
            raise ValueError("Stay period cannot be empty")
        return cls(reservation_id, guest_id, room_id, stay_period)

    @property
    def reservation_id(self) -> str:
        return self._reservation_id

    @property
    def guest_id(self) -> str:
        return self._guest_id

    @property
    def room_id(self) -> str:
        return self._room_id

    @property
    def stay_period(self) -> DateRange:
        return self._stay_period

    @property
    def status(self) -> ReservationStatus:
        return self._status

    def confirm(self):
        if self._status not in (
            ReservationStatus.PENDING,
        ):
            raise ValueError("Only pending reservations can be confirmed")
        self._status = ReservationStatus.CONFIRMED

    def cancel(self):
        if self._status not in (
            ReservationStatus.PENDING,
            ReservationStatus.CONFIRMED
        ):
            raise ValueError("Only pending or confirmed reservations can be canceled")
        self._status = ReservationStatus.CANCELED

    def check_in(self):
        if self._status != ReservationStatus.CONFIRMED:
            raise ValueError("Only confirmed reservations can be checked in")
        self._status = ReservationStatus.CHECKED_IN

    def check_out(self):
        if self._status != ReservationStatus.CHECKED_IN:
            raise ValueError("Only checked-in reservations can be checked out")
        self._status = ReservationStatus.CHECKED_OUT