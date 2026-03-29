# Employee Management (FastAPI + React)

Full CRUD employee management scaffold using FastAPI + SQLModel backend and React + Vite frontend.

## Project structure

- `backend/` - FastAPI backend
  - `requirements.txt` - dependencies
  - `database.py` - SQLite engine
  - `models.py` - SQLModel Employee model
  - `crud.py` - CRUD operations
  - `main.py` - FastAPI routes

- `frontend/` - React app
  - `package.json`, `vite.config.js`, `index.html`
  - `src/main.jsx`, `src/App.jsx`, `src/App.css`

## Backend setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

- API docs: http://127.0.0.1:8000/docs

## Frontend setup

```bash
cd frontend
npm install
npm run dev
```

- App: http://localhost:5173

## Docker setup

1. Build and run all containers:

```bash
docker compose up --build
```

2. Stop:

```bash
docker compose down
```

3. Access services:
- Backend: http://localhost:8000
- Swagger: http://localhost:8000/docs
- Frontend: http://localhost:5173

## API endpoints

- GET `/employees`
- GET `/employees/{id}`
- POST `/employees`
- PUT `/employees/{id}`
- DELETE `/employees/{id}`

## Notes

- Default DB file: `backend/employee.db`
- Use guarded CORS origins in production (not `*`).
- Add authentication/authorization and production DB for real deployments.
