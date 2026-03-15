from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.reservation import Reservation
from domain.enums.reservation_status import ReservationStatus
from domain.value_objects.date_range import DateRange
from infrastructure.database.models import ReservationModel


class PostgresReservationRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(self, reservation: Reservation) -> None:
        model = ReservationModel(
            reservation_id=reservation.reservation_id,
            guest_id=reservation.guest_id,
            room_id=reservation.room_id,
            check_in=reservation.stay_period.check_in,
            check_out=reservation.stay_period.check_out,
            status=reservation.status.value,
        )
        self._session.add(model)
        await self._session.commit()

    async def get_by_id(self, reservation_id: str) -> Reservation | None:
        result = await self._session.execute(
            select(ReservationModel).where(ReservationModel.reservation_id == reservation_id)
        )
        model = result.scalar_one_or_none()
        if model is None:
            return None
        return self._to_entity(model)

    async def get_active_by_room(self, room_id: str) -> list[Reservation]:
        active_statuses = [ReservationStatus.PENDING.value, ReservationStatus.CONFIRMED.value]
        result = await self._session.execute(
            select(ReservationModel).where(
                ReservationModel.room_id == room_id,
                ReservationModel.status.in_(active_statuses),
            )
        )
        return [self._to_entity(model) for model in result.scalars().all()]

    def _to_entity(self, model: ReservationModel) -> Reservation:
        stay_period = DateRange(check_in=model.check_in, check_out=model.check_out)
        return Reservation(
            reservation_id=model.reservation_id,
            guest_id=model.guest_id,
            room_id=model.room_id,
            stay_period=stay_period,
        )
