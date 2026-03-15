from datetime import date

class DateRange():
    def __init__(self, check_in: date, check_out: date) -> None:
        if check_in is None:
            raise ValueError("Check-in date cannot be empty")
        if check_out is None:
            raise ValueError("Check-out date cannot be empty")
        if check_in >= check_out:
            raise ValueError("Check-in date must be before check-out date")
        self._check_in = check_in
        self._check_out = check_out

    @property
    def check_in(self) -> date:
        return self._check_in

    @property
    def check_out(self) -> date:
        return self._check_out
    
    def nights(self) -> int:
        return (self._check_out - self._check_in).days
    
    def overlaps(self, other: 'DateRange') -> bool:
        return not (
            self._check_out <= other.check_in or
            self._check_in >= other.check_out
        )