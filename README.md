# Hotel DDD Project

A hotel reservation system built with Domain-Driven Design (DDD) and Hexagonal Architecture.

## Architecture

```
app/
├── domain/                  # Core business logic (no external dependencies)
│   ├── entities/            # Guest, Room, Reservation
│   ├── value_objects/       # DateRange
│   └── enums/               # ReservationStatus
├── application/             # Use cases and port definitions
│   ├── use_cases/           # CreateReservation
│   └── ports/               # Repository interfaces (Protocols)
└── infrastructure/          # External concerns
    ├── api/                 # FastAPI routers
    ├── database/            # SQLAlchemy models and connection
    └── repositories/        # Postgres implementations of ports
```

### Application Flow

```
HTTP Request
  → FastAPI Router (infrastructure/api)
    → Use Case (application/use_cases)
      → Domain Entity (domain/entities)
    → Repository Port (application/ports) ← Protocol interface
      → Postgres Repository (infrastructure/repositories) ← Implementation
        → SQLAlchemy Model (infrastructure/database/models)
          → PostgreSQL
```

1. A request hits a **FastAPI router** in the infrastructure layer
2. The router injects an `AsyncSession` and builds the **repository** (adapter)
3. The repository is passed to a **use case**, which orchestrates the business logic
4. The use case calls **domain entities** for validation and state transitions
5. The use case persists changes through the **repository port** (Protocol)
6. The Postgres repository maps domain entities to/from **SQLAlchemy models**

The domain and application layers have zero knowledge of FastAPI, SQLAlchemy, or PostgreSQL.

## Tech Stack

- Python 3.14
- FastAPI
- SQLAlchemy (async)
- PostgreSQL
- Docker
- uv (package manager)

## Running the Project

### Prerequisites

- Docker and Docker Compose
- uv (optional, for local development)

### With Docker

```bash
cp .env.example .env
docker compose up --build
```

The API will be available at `http://localhost:8000`.

### Local Development

```bash
# Start only the database
docker compose up db -d

# Install dependencies
uv sync

# Update .env to point to localhost
# DATABASE_URL=postgresql+asyncpg://hotel:hotel@localhost:5432/hotel_db

# Run the app
uvicorn app.main:app --app-dir app --reload
```

## API Endpoints

| Method | Path              | Description            |
|--------|-------------------|------------------------|
| GET    | `/health`         | Health check           |
| POST   | `/reservations/`  | Create a reservation   |

### Example: Create a Reservation

```bash
curl -X POST http://localhost:8000/reservations/ \
  -H "Content-Type: application/json" \
  -d '{
    "reservation_id": "res-001",
    "guest_id": "1",
    "room_id": "room-101",
    "check_in": "2026-04-01",
    "check_out": "2026-04-05"
  }'
```
