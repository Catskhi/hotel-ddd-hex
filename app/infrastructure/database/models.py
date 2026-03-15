from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class GuestModel(Base):
    __tablename__ = "guests"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    phone: Mapped[str] = mapped_column(String, nullable=False)

    reservations: Mapped[list["ReservationModel"]] = relationship(back_populates="guest")


class RoomModel(Base):
    __tablename__ = "rooms"

    room_id: Mapped[str] = mapped_column(String, primary_key=True)
    number: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    capacity: Mapped[int] = mapped_column(Integer, nullable=False)

    reservations: Mapped[list["ReservationModel"]] = relationship(back_populates="room")


class ReservationModel(Base):
    __tablename__ = "reservations"

    reservation_id: Mapped[str] = mapped_column(String, primary_key=True)
    guest_id: Mapped[int] = mapped_column(Integer, ForeignKey("guests.id"), nullable=False)
    room_id: Mapped[str] = mapped_column(String, ForeignKey("rooms.room_id"), nullable=False)
    check_in: Mapped[str] = mapped_column(Date, nullable=False)
    check_out: Mapped[str] = mapped_column(Date, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False, default="pending")

    guest: Mapped["GuestModel"] = relationship(back_populates="reservations")
    room: Mapped["RoomModel"] = relationship(back_populates="reservations")
