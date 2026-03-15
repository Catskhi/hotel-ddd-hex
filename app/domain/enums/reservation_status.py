from enum import Enum

class ReservationStatus(str, Enum):
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    CANCELED = 'canceled'
    CHECKED_IN = 'checked_in'
    CHECKED_OUT = 'checked_out'
