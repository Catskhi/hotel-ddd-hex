class Room:
    def __int__(self, room_id: str, number: str, capacity: int) -> None:
        if not room_id:
            raise ValueError("Room ID cannot be empty")
        if not number:
            raise ValueError("Room number cannot be empty")
        if capacity is None or capacity <= 0:
            raise ValueError("Capacity cannot be empty or zero")

        self._room_id = room_id
        self._room_number = number
        self._capacity = capacity   

    @property
    def room_id(self) -> str:
        return self._room_id

    @property
    def room_number(self) -> str:
        return self._room_number

    @property
    def capacity(self) -> int:
        return self._capacity