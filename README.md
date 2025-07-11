# 🚌 QuickBus Backend

QuickBus is a smart bus ticketing and route management system built with **FastAPI + MongoDB**. It powers a mobile POS app (Flutter, Sunmi V2s) and a web admin panel (React + TypeScript) to handle ticket booking, route and bus management, and real-time reporting.

---

## 🧠 Key Features

- Route and bus management
- Ticket booking and QR printing
- Real-time sales & occupancy summary
- Offline to online sync (for POS)
- Support for cash & digital payments (bKash, Nagad placeholders)
- Admin analytics dashboard and PDF/CSV reports

---

## 🗂️ Recommended Project Structure


🗂️ Recommended Project Structure

```
quickbus_backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py                # FastAPI app instance
│   ├── config.py              # Env vars, DB URI
│   │
│   ├── models/                # MongoDB models (Pydantic)
│   │   ├── bus.py
│   │   ├── route.py
│   │   ├── ticket.py
│   │   ├── user.py
│   │   └── common.py
│   │
│   ├── api/                   # API routers
│   │   ├── auth.py
│   │   ├── bus.py
│   │   ├── route.py
│   │   ├── ticket.py
│   │   ├── sync.py
│   │   └── summary.py
│   │
│   ├── db/                    # MongoDB client
│   │   └── mongo.py
│   │
│   ├── services/              # Business logic
│   │   ├── auth_service.py
│   │   ├── ticket_service.py
│   │   └── sync_service.py
│   │
│   ├── core/                  # Security, JWT
│   │   ├── security.py
│   │   ├── dependencies.py
│   │   └── exceptions.py
│   │
│   └── utils/                 # QR generation, helpers
│       ├── qr_gen.py
│       └── printer_helpers.py
│
├── .env                       # Secrets
├── requirements.txt
└── run.py                     # Entrypoint
```


---

## 🧪 API Modules Overview

| Feature        | Endpoint Prefix | Description                         |
|----------------|------------------|-------------------------------------|
| 🔐 Auth        | `/auth`         | Login, logout, user info            |
| 🚌 Buses       | `/bus`          | Register, edit, list buses          |
| 🚏 Routes      | `/route`        | Manage bus routes                   |
| 🎫 Tickets     | `/ticket`       | Book, view, validate, cancel        |
| 🔄 Sync        | `/sync`         | POS offline/online sync             |
| 📊 Summary     | `/summary`      | Sales stats, bus utilization        |
| 📁 Reports     | `/report`       | Export reports (CSV, PDF)           |

---

## ⚙️ How to Run the Backend

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
