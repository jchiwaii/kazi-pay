# KaziPay (In Progress)– Secure Escrow for Kenya’s Gig Economy

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Built with Django](https://img.shields.io/badge/Built%20with-Django-092E20?logo=django)](https://www.djangoproject.com/)
[![React](https://img.shields.io/badge/Frontend-React-61DAFB?logo=react)](https://reactjs.org/)
[![M‑Pesa](https://img.shields.io/badge/Powered%20by-M‑Pesa-00A859?logo=safaricom)](https://developer.safaricom.co.ke/)

KaziPay is an escrow platform for Kenya’s gig economy – currently under development for the M‑Pesa Africa x GOMYCODE Hackathon 2026.



##  Problem

Kenya’s informal workers (5M+) face a two‑sided trust gap: workers fear non‑payment; clients fear paying upfront for poor work.

##  Solution

We’re building a web‑based escrow system using M‑Pesa STK Push and B2C. Clients deposit funds, workers accept jobs, and payment is released only after client confirmation.

Authentication & Roles

- Users register/login with **phone number (OTP)** or **email/password**.
- JWT tokens secure all API requests.
- Roles: `client`, `worker`, or `both`.

**Test accounts** (use in the live demo):
- Client: `254711000001` (phone) / `SecureK@zi99!` / `client`
- Worker: `254711000002` (phone) / `SecureK@zi99!` / `worker`



##  Tech Stack (Planned)

| Category | Technology |
|----------|------------|
| Backend  | Django, Python |
| Database | PostgreSQL |
| Frontend | React, Vite |
| M‑Pesa   | Daraja API (STK Push, B2C) |
| SMS      | Africa’s Talking |


##  Core Features

-  **Secure Authentication** – Register/login with phone number (OTP) or email/password. JWT tokens secure all API requests. Roles: Client, Worker, or Both.

-  **M‑Pesa Escrow Payments** – Clients pay via STK Push; funds are held until the job is completed. Workers receive payment instantly via B2C after client confirmation.

-  **Job Management** – Clients post jobs with description, amount, and target worker. Workers view and accept available jobs. Clients confirm completion to release payment.

-  **Real‑time SMS Notifications** – Africa’s Talking sends SMS updates at every key step: payment received, job accepted, payment released.

-  **Auto‑Release Mechanism** – If the client does not confirm within 48 hours of worker acceptance, the system automatically pays the worker (protects workers from unresponsive clients).

-  **Transaction History** – Every deposit and payout is logged in a transaction model for full transparency.

-  **Dual‑Role Dashboards** – Separate interfaces for clients (post jobs, track active jobs, confirm completion) and workers (browse available jobs, see accepted jobs, track earnings).

-  **Responsive Web Interface** – Built with React and Tailwind CSS, works seamlessly on desktop and mobile.

  
---

##  Team Lynx

| Name | Role |
|------|------|
| Joseph Omondi | Backend |
| Wendy Okoth | Backend |
| Susan Awori | Frontend |
| John Chiwai | M‑Pesa Integration |
| Gavin Chesebe | Documentation & Presentation |

##  **Project Structure**
```text
kazipay/
├── backend-app/             # Django Modular Backend
│
│   ├── adminApp/            # Platform Oversight & Disputes
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── base_tests.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── services.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── __init__.py
│
│   ├── authApp/             # User Auth, Profiles & Signals
│   │   ├── adapters.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── signals.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   ├── views.py
│   │   └── __init__.py
│
│   ├── backend/             # Core Project Settings
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── __init__.py
│
│   ├── clients/             # Client-side Job Management
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── services.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── __init__.py
│
│   ├── escrow/              # M-Pesa C2B & Transaction Logic
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── mpesa.py
│   │   ├── serializers.py
│   │   ├── services.py
│   │   ├── signals.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── __init__.py
│
│   ├── notification/        # USSD & SMS - Africa's Talking
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── services.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   ├── views.py
│   │   └── __init__.py
│
│   ├── wallet/              # Financial Records & M-Pesa B2C
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── mpesa.py
│   │   ├── serializers.py
│   │   ├── services.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── __init__.py
│
│   ├── workers/             # Worker Profiles & Bidding
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── services.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── __init__.py
│
│   ├── templates/           # Server-rendered HTML (Tailwind UI)
│   │   ├── base.html
│   │   ├── login.html
│   │   └── dashboard.html
│
│   ├── manage.py            # Django CLI tool
│   ├── requirements.txt     # Python package list
│   └── .env                 # Environment variables (Safaricom & AT Keys)
│
├── frontend-app/            # React + Vite landing app
│   ├── src/
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   └── vite.config.js
│
├── frontend/                # Static HTML/CSS/JS dashboard
│   ├── dashboard.css
│   ├── dashboard.html
│   ├── index.html
│   ├── job-details.html
│   ├── market.html
│   ├── payment.html
│   ├── postjob.html
│   ├── script.js
│   ├── service.html
│   └── style.css
│
├── assets/                  # Shared images & media
│   ├── istockphoto-2198966728-612x612.jpg
│   ├── istockphoto-2249457023-612x612.webp
│   ├── photo-1502920917128-1aa500764cbd.avif
│   ├── photo-1609250291996-fdebe6020a8f.avif
│   ├── photo-1627405016867-4d59bd6b4747.avif
│   ├── photo-1631464572173-597f6db2f18a.avif
│   ├── photo-1656944227421-416b1d2186c9.avif
│   ├── premium_photo-1667251760504-096946b820af.avif
│   └── premium_photo-1679513691474-73102089c117.avif
│
├── screenshots/             # (optional) for README
├── .gitignore
├── LICENSE
└── README.md

```
 Setup & Installation

### Prerequisites
- Python 3.10+, Node.js 16+
- PostgreSQL (local or cloud)
- Safaricom Daraja sandbox credentials
- Africa’s Talking sandbox credentials

### Backend (Django)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
cp .env.example .env

