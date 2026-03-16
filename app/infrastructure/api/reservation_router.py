from datetime import date

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from application.use_cases.create_reservation import CreateReservation
from infrastructure.database.connection import get_session
from infrastructure.repositories.postgres_reservation_repository import PostgresReservationRepository

router = APIRouter(prefix="/reservations", tags=["reservations"])


class CreateReservationRequest(BaseModel):
    reservation_id: str
    guest_id: str
    room_id: str
    check_in: date
    check_out: date


class ReservationResponse(BaseModel):
    reservation_id: str
    guest_id: str
    room_id: str
    check_in: date
    check_out: date
    status: str


@router.post("/", response_model=ReservationResponse, status_code=201)
async def create_reservation(
    request: CreateReservationRequest,
    session: AsyncSession = Depends(get_session),
) -> ReservationResponse:
    repository = PostgresReservationRepository(session)
    use_case = CreateReservation(repository)
    reservation = await use_case.execute(
        reservation_id=request.reservation_id,
        guest_id=request.guest_id,
        room_id=request.room_id,
        check_in=request.check_in,
        check_out=request.check_out,
    )
    return ReservationResponse(
        reservation_id=reservation.reservation_id,
        guest_id=reservation.guest_id,
        room_id=reservation.room_id,
        check_in=reservation.stay_period.check_in,
        check_out=reservation.stay_period.check_out,
        status=reservation.status.value,
    )
