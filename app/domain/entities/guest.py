class Guest():

    def __init__(self, id: int, name: str, email: str, phone: str):
        self._id = id
        self._name = name
        self._email = email
        self._phone = phone

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def phone(self) -> str:
        return self._phone

    def change_name(self, new_name: str) -> None:
        if not new_name:
            raise ValueError("Name cannot be empty")
        self._name = new_name

    def change_email(self, new_email: str) -> None:
        if not new_email or '@' not in new_email:
            raise ValueError("Invalid email address")
        self._email = new_email

    def change_phone(self, new_phone: str) -> None:
        if not new_phone:
            raise ValueError("Phone number cannot be empty")
        self._phone = new_phone

    def __str__(self):
        return f"Guest(id={self._id}, name='{self._name}', email='{self._email}', phone='{self._phone}')"