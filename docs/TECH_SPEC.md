# TECH_SPEC.md – File Share Guard

---

## 1. Overview

**File Share Guard** is a lightweight, self‑contained service that allows users to create time‑limited, optionally password‑protected file shares. The service exposes a minimal API for:

1. **Creating a share** – generates a unique `share_id` and stores the mapping to the original file.
2. **Authenticating** – verifies a password (if set) and issues a short‑lived JWT token that authorises subsequent file‑access calls.
3. **Retrieving the file name** – returns the original file name for a valid share and token.

The implementation is intentionally simple to keep the codebase maintainable while still covering the core use‑case of secure file sharing.

---

## 2. Architecture

```
┌───────────────────────┐
│  Client (CLI / API)   │
└─────────────┬─────────┘
              │ HTTP
              ▼
┌───────────────────────┐
│  FastAPI Application  │
│  (file_share_guard)    │
└───────┬───────┬───────┘
        │       │
        │  REST │
        ▼       ▼
┌───────────────────────┐   ┌───────────────────────┐
│  Share Service Layer  │   │  Auth Service Layer   │
│  (business logic)     │   │  (JWT handling)       │
└───────┬───────┬───────┘   └───────┬───────┬───────┘
        │       │                 │       │
        ▼       ▼                 ▼       ▼
┌───────────────────────┐   ┌───────────────────────┐
│  SQLite DB (file_shares)│   │  Redis (cache)         │
│  (share_id, file_name,  │   │  (token revocation)   │
│   password_hash, ttl)   │   └───────────────────────┘
└───────────────────────┘
```

* **FastAPI** – Provides the HTTP interface and automatic OpenAPI docs.
* **SQLite** – Persistent store for share metadata; lightweight and file‑based.
* **Redis** – Optional in‑memory cache for token revocation lists (TTL‑based).
* **JWT** – Stateless authentication tokens issued after successful password verification.

---

## 3. Components

| Layer | Responsibility | Key Files |
|-------|----------------|-----------|
| **API Layer** | Exposes endpoints (`/shares`, `/auth`, `/file`) | `app/main.py`, `app/routers/*.py` |
| **Service Layer** | Business logic, validation, hashing, TTL handling | `app/services/share_service.py`, `app/services/auth_service.py` |
| **Persistence Layer** | ORM / DB access | `app/models/*.py`, `app/database.py` |
| **Auth Layer** | JWT creation/verification, password hashing | `app/auth/*.py` |
| **Utilities** | Config, logging, error handling | `app/utils/*.py` |
| **Tests** | Unit & integration tests | `tests/*.py` |

---

## 4. Data Model

```sql
CREATE TABLE file_shares (
    id          TEXT PRIMARY KEY,          -- UUID4 string
    file_name   TEXT NOT NULL,
    password_hash TEXT,                    -- NULL if no password
    expires_at  DATETIME NOT NULL,          -- UTC timestamp
    created_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

* `id` – Unique share identifier returned to the client.
* `password_hash` – Stored using `argon2` (via `argon2-cffi`).
* `expires_at` – Share validity window (default 24 h, configurable).
* `created_at` – Creation timestamp for audit purposes.

---

## 5. Key APIs / Interfaces

| HTTP Method | Path | Description | Request Body | Response |
|-------------|------|-------------|--------------|----------|
| `POST` | `/shares` | Create a new share | `{"file_name": "report.pdf", "password": "secret", "ttl_seconds": 86400}` | `{"share_id": "uuid", "expires_at": "2026-07-01T12:00:00Z"}` |
| `POST` | `/auth` | Authenticate a share | `{"share_id": "uuid", "password": "secret"}` | `{"token": "<jwt>"}` |
| `GET` | `/file/{share_id}` | Retrieve original file name | Header: `Authorization: Bearer <jwt>` | `{"file_name": "report.pdf"}` |

*All responses are JSON. Errors return standard HTTP status codes with a `detail` field.*

### JWT Payload

```json
{
  "sub": "share_id",
  "exp": 1690000000,
  "iat": 1690000000
}
```

* `sub` – Share ID.
* `exp` – Expiration timestamp (same as `expires_at`).

---

## 6. Tech Stack

| Category | Library / Tool | Version |
|----------|----------------|---------|
| **Framework** | FastAPI | 0.112.0 |
| **Server** | Uvicorn | 0.30.1 |
| **Database** | SQLite (via SQLAlchemy) | 2.0.32 |
| **Auth** | PyJWT | 2.8.0 |
| **Password Hashing** | argon2-cffi | 23.1.0 |
| **Caching** | Redis | 5.0.14 |
| **Testing** | pytest, httpx | 3.2.0 |
| **Linting** | ruff | 0.5.5 |
| **CI** | GitHub Actions | N/A |
| **Container** | Docker | 27.0.3 |

---

## 7. Dependencies

```toml
[tool.poetry]
name = "file-share-guard"
version = "0.1.0"
description = "Secure file share guard"
authors = ["Axentx <contact@axentx.com>"]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.12"
fastapi = "^0.112.0"
uvicorn = "^0.30.1"
sqlalchemy = "^2.0.32"
pydantic = "^2.9.2"
pyjwt = "^2.8.0"
argon2-cffi = "^23.1.0"
redis = "^5.0.14"

[tool.poetry.group.dev.dependencies]
pytest = "^8.
