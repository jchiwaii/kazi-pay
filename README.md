# KaziPay (In Progress)– Secure Escrow for Kenya’s Gig Economy

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Built with Django](https://img.shields.io/badge/Built%20with-Django-092E20?logo=django)](https://www.djangoproject.com/)
[![React](https://img.shields.io/badge/Frontend-React-61DAFB?logo=react)](https://reactjs.org/)
[![M‑Pesa](https://img.shields.io/badge/Powered%20by-M‑Pesa-00A859?logo=safaricom)](https://developer.safaricom.co.ke/)

KaziPay is an escrow platform for Kenya’s gig economy – currently under development for the M‑Pesa Africa x GOMYCODE Hackathon 2026.



## 📌 Problem

Kenya’s informal workers (5M+) face a two‑sided trust gap: workers fear non‑payment; clients fear paying upfront for poor work.

## 💡 Solution

We’re building a web‑based escrow system using M‑Pesa STK Push and B2C. Clients deposit funds, workers accept jobs, and payment is released only after client confirmation.



## 🛠️ Tech Stack (Planned)

| Category | Technology |
|----------|------------|
| Backend  | Django, Python |
| Database | PostgreSQL |
| Frontend | React, Vite |
| M‑Pesa   | Daraja API (STK Push, B2C) |
| SMS      | Africa’s Talking |


## 🌟 Core Features

- 🔐 **Secure Authentication** – Register/login with phone number (OTP) or email/password. JWT tokens secure all API requests. Roles: Client, Worker, or Both.

- 💰 **M‑Pesa Escrow Payments** – Clients pay via STK Push; funds are held until the job is completed. Workers receive payment instantly via B2C after client confirmation.

- 📋 **Job Management** – Clients post jobs with description, amount, and target worker. Workers view and accept available jobs. Clients confirm completion to release payment.

- 📨 **Real‑time SMS Notifications** – Africa’s Talking sends SMS updates at every key step: payment received, job accepted, payment released.

- ⏱️ **Auto‑Release Mechanism** – If the client does not confirm within 48 hours of worker acceptance, the system automatically pays the worker (protects workers from unresponsive clients).

- 🧾 **Transaction History** – Every deposit and payout is logged in a transaction model for full transparency.

- 👥 **Dual‑Role Dashboards** – Separate interfaces for clients (post jobs, track active jobs, confirm completion) and workers (browse available jobs, see accepted jobs, track earnings).

- 📱 **Responsive Web Interface** – Built with React and Tailwind CSS, works seamlessly on desktop and mobile.

  
---

## 👥 Team

| Name | Role |
|------|------|
| Joseph Omondi | Backend |
| Wendy Okoth | Backend |
| Susan Awori | Frontend |
| John Chiwai | M‑Pesa Integration |
| Gavin Chesebe | Documentation & Presentation |

## 🏗️ **Project Structure**
```text
kazipay/
├── backend/                 # Django project
│   ├── Kazi_Pay/            # Project settings
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── kazipay_app/         # Main app
│   │   ├── migrations/
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── auto_release.py   # Auto‑release cron
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── utils/
│   │       ├── mpesa.py
│   │       └── sms.py
│   ├── requirements.txt
│   ├── .env.example
│   └── manage.py
├── frontend/                # React + Vite
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   │   ├── PostJob.jsx
│   │   │   ├── FindWork.jsx
│   │   │   ├── ClientDashboard.jsx
│   │   │   └── WorkerDashboard.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.js
│   └── .env
├── screenshots/             # (optional) for README
├── .gitignore
├── LICENSE
└── README.md
```
## 🚧 Status

The project is being actively developed. This README will be updated with:

- Screenshots of key features
- Live demo link
- Setup instructions
- Full documentation

Stay tuned!



Built for M‑Pesa Africa x GOMYCODE Kenya Hackathon 2026 – *Money in Motion*
