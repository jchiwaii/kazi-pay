# KaziPay – Secure Escrow for Kenya's Gig Economy

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Built with Django](https://img.shields.io/badge/Built%20with-Django-092E20?logo=django)](https://www.djangoproject.com/)
[![React](https://img.shields.io/badge/Frontend-React-61DAFB?logo=react)](https://reactjs.org/)
[![M‑Pesa](https://img.shields.io/badge/Powered%20by-M‑Pesa-00A859?logo=safaricom)](https://developer.safaricom.co.ke/)

KaziPay is an escrow platform for Kenya's gig economy – built for the M‑Pesa Africa x GOMYCODE Hackathon 2026.

**Live Demo:** [https://kazi-pay-five.vercel.app/](https://kazi-pay-five.vercel.app/)

**API Docs:** [https://kazi-pay.onrender.com/swagger/](https://kazi-pay.onrender.com/swagger/) · [ReDoc](https://kazi-pay.onrender.com/redoc/)

## Test Accounts

The live database is fresh on each deploy. Register new accounts at [https://kazi-pay-five.vercel.app/](https://kazi-pay-five.vercel.app/) using the samples below, or use these on your local setup after running migrations.

| Username       | Phone Number   | Password                     | Role   |
| -------------- | -------------- | ---------------------------- | ------ |
| `amina_client` | `254712000001` | `KaziPay@2026!KaziPay@2026!` | Client |
| `brian_worker` | `254712000002` | `KaziPay@2026!KaziPay@2026!` | Worker |

> **Login uses phone number**.

---

## About

KaziPay solves the trust gap in Kenya's informal economy by providing a secure escrow system for gig workers and clients. The platform ensures workers get paid for completed work while protecting clients from paying for undelivered services.

### How It Works

1. **Client posts a job** – Describes the work needed and sets a budget
2. **Workers submit bids** – Interested workers propose their rates and qualifications
3. **Client accepts a bid** – Triggers M‑Pesa STK Push for payment
4. **Funds locked in escrow** – Payment is secured but not yet released
5. **Worker completes job** – Marks the job as complete when done
6. **Client confirms completion** – Reviews work and releases payment
7. **Worker receives funds** – Money lands in their KaziPay wallet
8. **Withdraw to M‑Pesa** – Worker can cash out anytime via B2C

---

## Problem

Kenya's informal workers (5M+) face a two‑sided trust gap: workers fear non‑payment; clients fear paying upfront for poor work.

## Solution

A web‑based escrow system using M‑Pesa STK Push and B2C. Clients deposit funds, workers accept jobs, and payment is released only after client confirmation.

---

## Core Features

- **Secure Authentication** – Register and login with phone number and password. JWT tokens secure all API requests. Roles: Client or Worker.

- **M‑Pesa Escrow Payments** – Clients pay via STK Push; funds are held until the job is completed. Workers receive payment instantly via B2C after client confirmation.

![Pay via STK push](https://raw.githubusercontent.com/susan-awori/kazi-pay/refs/heads/main/screenshots/mpesa%20prompt/WhatsApp%20Image%202026-03-29%20at%208.18.58%20PM.jpeg)

- **Job Management** – Clients post jobs with description and budget. Workers view and bid on available jobs. Clients confirm completion to release payment.

![Invoice Sent](https://raw.githubusercontent.com/susan-awori/kazi-pay/refs/heads/main/screenshots/worker%20invoice%20sent/WhatsApp%20Image%202026-03-29%20at%208.18.56%20PM.jpeg)

- **Bidding System** – Workers submit competitive bids with proposals and amounts. Clients review and select the best fit for their job.

- **Digital Wallet** – Every user has a wallet to track balance, view transaction history, and withdraw funds to M‑Pesa.

![KaziPay Client](https://raw.githubusercontent.com/susan-awori/kazi-pay/refs/heads/main/screenshots/kazipay%20client/WhatsApp%20Image%202026-03-29%20at%208.18.57%20PM.jpeg)

![KaziPay Worker Profile](https://raw.githubusercontent.com/susan-awori/kazi-pay/refs/heads/main/screenshots/kazipay%20worker%20profile/WhatsApp%20Image%202026-03-29%20at%2010.54.03%20AM.jpeg)

- **Real‑time Notifications** – In-app notifications keep both parties informed at every step: bid accepted, job completed, funds released, dispute raised.

- **Dispute Resolution** – Either party can raise a dispute with a detailed reason. Admin reviews and resolves via the platform admin panel.

- **Transaction History** – Every deposit and payout is logged in the wallet transaction model for full transparency.

- **Dual‑Role Dashboards** – Separate interfaces for clients (post jobs, review bids, confirm completion, manage escrow) and workers (browse jobs, place bids, mark complete, track earnings and withdraw).

![KaziPay Worker](https://raw.githubusercontent.com/susan-awori/kazi-pay/refs/heads/main/screenshots/kazi%20pay%20worker/WhatsApp%20Image%202026-03-29%20at%2010.54.03%20AM.jpeg)

- **Responsive Web Interface** – Built with React 18 and Tailwind CSS, works on desktop and mobile.

---

## Tech Stack

| Category                   | Technology                                    |
| -------------------------- | --------------------------------------------- |
| **Backend**                | Django 6.0.3, Django REST Framework           |
| **Database**               | PostgreSQL (Production), SQLite (Development) |
| **Frontend**               | React 18, Vite, Tailwind CSS                  |
| **Authentication**         | JWT (Simple JWT), dj-rest-auth                |
| **M‑Pesa Integration**     | Safaricom Daraja API (STK Push, B2C)          |
| **SMS**                    | Africa's Talking API                          |
| **Deployment**             | Render (Backend), Vercel (Frontend)           |
| **API Documentation**      | drf-yasg (Swagger/ReDoc)                      |
| **Environment Management** | python-decouple                               |
| **Static Files**           | WhiteNoise                                    |

### APIs & Integrations

- **Safaricom Daraja API** – M-Pesa STK Push for client deposits and B2C for worker payouts
- **Africa's Talking** – SMS notifications for payment confirmations and job updates
- **JWT Authentication** – Secure token-based authentication for all API endpoints

---

## Project Structure

```text
kazi-pay/
├── backend-app/                    # Django backend
│   ├── backend/                    # Project settings
│   │   ├── settings.py            # Django configuration
│   │   ├── urls.py                # Main URL routing
│   │   └── wsgi.py                # WSGI application
│   │
│   ├── authApp/                   # Authentication module
│   │   ├── models.py              # CustomUser model (phone_number as USERNAME_FIELD)
│   │   ├── serializers.py         # Auth serializers (login by phone number)
│   │   ├── views.py               # Register/Login/Logout
│   │   └── adapters.py            # Custom account adapter
│   │
│   ├── clients/                   # Client module
│   │   ├── models.py              # Job, ClientProfile, ClientRating
│   │   ├── views.py               # Job CRUD, accept bid
│   │   ├── services.py            # Business logic
│   │   └── urls.py                # Client API routes
│   │
│   ├── workers/                   # Worker module
│   │   ├── models.py              # WorkerProfile, Bid, WorkerRating
│   │   ├── views.py               # Submit bid, browse jobs, mark complete
│   │   └── urls.py                # Worker API routes
│   │
│   ├── escrow/                    # Escrow module
│   │   ├── models.py              # Escrow model
│   │   ├── views.py               # Release funds, dispute, M-Pesa callback
│   │   └── urls.py                # Escrow API routes
│   │
│   ├── wallet/                    # Wallet module
│   │   ├── models.py              # Wallet, WalletTransaction
│   │   ├── views.py               # Balance, transactions, withdraw
│   │   ├── services.py            # Wallet operations
│   │   └── urls.py                # Wallet API routes
│   │
│   ├── notification/              # Notification module
│   │   ├── models.py              # Notification model
│   │   ├── services.py            # Send notification
│   │   ├── utils.py               # SMS integration
│   │   └── urls.py                # Notification API routes
│   │
│   ├── adminApp/                  # Admin module
│   │   ├── views.py               # Dispute resolution, revenue summary
│   │   └── urls.py                # Admin API routes
│   │
│   ├── manage.py                  # Django management
│   ├── requirements.txt           # Python dependencies
│   ├── Procfile                   # Render deployment
│   └── render.yaml                # Render configuration
│
├── frontend-app/                  # React frontend
│   ├── src/
│   │   ├── App.jsx                # Main app (Landing, Client/Worker dashboards)
│   │   ├── api.js                 # API client (native fetch + JWT)
│   │   ├── main.jsx               # React entry point
│   │   └── index.css              # Global styles + Tailwind
│   │
│   ├── index.html                 # HTML template
│   ├── package.json               # NPM dependencies
│   ├── vite.config.js             # Vite configuration + dev proxy
│   ├── tailwind.config.js         # Tailwind CSS config
│   └── vercel.json                # Vercel deployment (SPA rewrite)
│
├── screenshots/                   # App screenshots
├── .gitignore                     # Git ignore patterns
├── LICENSE                        # MIT License
└── README.md                      # This file
```

---

## Setup Instructions

### Prerequisites

- Python 3.10+
- Node.js 18+ and npm
- PostgreSQL (for production) or SQLite (for development)
- M-Pesa Developer Account (Safaricom Daraja)
- Africa's Talking Account

### Backend Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/susan-awori/kazi-pay.git
   cd kazi-pay/backend-app
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment configuration**

   Create a `.env` file in the `backend-app/` directory (see Environment Variables section below).

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create superuser** (optional, for admin panel access)

   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**

   ```bash
   python manage.py runserver
   ```

   Backend available at `http://localhost:8000`

8. **Access API documentation**
   - Swagger UI: `http://localhost:8000/swagger/`
   - ReDoc: `http://localhost:8000/redoc/`
   - Admin Panel: `http://localhost:8000/admin/`

### Frontend Setup

1. **Navigate to frontend directory**

   ```bash
   cd ../frontend-app
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Environment configuration**

   Create a `.env` file in `frontend-app/`:

   ```env
   VITE_API_URL=http://localhost:8000
   ```

   > In development the Vite proxy forwards `/api` requests to `localhost:8000` automatically. The `VITE_API_URL` variable is only needed when pointing at a remote backend.

4. **Run development server**

   ```bash
   npm run dev
   ```

   Frontend available at `http://localhost:5173`

5. **Build for production**
   ```bash
   npm run build
   ```

---

## Environment Variables

### Backend (`backend-app/.env`)

```env
# Django Settings
SECRET_KEY=your-super-secret-key-here-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,.ngrok-free.app

# Database (SQLite used by default; set DATABASE_URL for PostgreSQL)
DATABASE_URL=postgresql://user:password@localhost:5432/kazipay_db

# CORS — add any additional origins beyond the hardcoded defaults
EXTRA_CORS_ORIGINS=https://your-custom-frontend.vercel.app

# M-Pesa / Daraja API
MPESA_ENVIRONMENT=sandbox
MPESA_CONSUMER_KEY=your_consumer_key
MPESA_CONSUMER_SECRET=your_consumer_secret
MPESA_SHORTCODE=174379
MPESA_PASSKEY=your_mpesa_passkey
MPESA_INITIATOR_NAME=testapi
MPESA_SECURITY_CREDENTIAL=your_security_credential
MPESA_B2C_SHORTCODE=600981

# M-Pesa Callback URLs (must be publicly accessible HTTPS URLs)
MPESA_C2B_CALLBACK_URL=https://your-domain.com/api/escrow/mpesa-callback/
MPESA_B2C_CALLBACK_URL=https://your-domain.com/wallet/b2c-callback/
MPESA_B2C_TIMEOUT_URL=https://your-domain.com/wallet/b2c-callback/

# Africa's Talking
AT_USERNAME=sandbox
AT_API_KEY=your_africas_talking_api_key
AT_PHONE_NUMBER=your_shortcode_or_sender_id
AT_SHORTCODE=23440
```

### Frontend (`frontend-app/.env`)

```env
# Point to your backend — leave empty to use Vite proxy in development
VITE_API_URL=https://kazi-pay.onrender.com
```

### Getting API Credentials

1. **M-Pesa Daraja API**
   - Sign up at [https://developer.safaricom.co.ke/](https://developer.safaricom.co.ke/)
   - Create an app to get Consumer Key and Consumer Secret
   - Sandbox shortcode: `174379`

2. **Africa's Talking**
   - Sign up at [https://africastalking.com/](https://africastalking.com/)
   - Get your API Key from the dashboard
   - Use sandbox mode for testing

---

## Testing the Application

### Local Testing

1. Start the backend: `python manage.py runserver`
2. Start the frontend: `npm run dev`
3. Open `http://localhost:5173`
4. Register two accounts — one as **Client**, one as **Worker**

**As Client:**

- Post a new job (title, description, budget)
- Wait for a bid from the worker
- Accept the bid → escrow created
- After worker marks complete, release the funds

**As Worker:**

- Browse available jobs
- Submit a bid with a proposal and amount
- Wait for acceptance
- Mark the job as complete
- Check wallet for received payment → withdraw to M-Pesa

### Using Ngrok for M-Pesa Callbacks

M-Pesa requires public HTTPS URLs for callbacks. Use ngrok during local development:

```bash
# Expose Django server
ngrok http 8000

# Copy the HTTPS URL and update your .env:
MPESA_C2B_CALLBACK_URL=https://your-ngrok-url.ngrok-free.app/api/escrow/mpesa-callback/
MPESA_B2C_CALLBACK_URL=https://your-ngrok-url.ngrok-free.app/wallet/b2c-callback/
```

---

## API Reference

All endpoints require `Authorization: Bearer <access_token>` except registration, login, and M-Pesa callbacks.

| Method | Endpoint                                       | Description                      |
| ------ | ---------------------------------------------- | -------------------------------- |
| POST   | `/api/auth/register/`                          | Register (phone, password, role) |
| POST   | `/api/auth/login/`                             | Login with phone number          |
| GET    | `/api/client/jobs/`                            | List client's jobs               |
| POST   | `/api/client/jobs/`                            | Post a new job                   |
| POST   | `/api/client/jobs/{id}/accept-bid/`            | Accept a worker's bid            |
| GET    | `/api/worker/browse-jobs/`                     | Browse open jobs                 |
| POST   | `/api/worker/my-bids/`                         | Place a bid                      |
| POST   | `/api/worker/my-bids/{id}/mark-complete/`      | Mark job as complete             |
| GET    | `/api/escrow/transactions/`                    | List escrow transactions         |
| POST   | `/api/escrow/transactions/{id}/release-funds/` | Release funds to worker          |
| POST   | `/api/escrow/transactions/{id}/raise-dispute/` | Raise a dispute                  |
| GET    | `/api/wallet/wallet/`                          | Get wallet balance + history     |
| POST   | `/api/wallet/wallet/withdraw/`                 | Withdraw to M-Pesa               |
| GET    | `/api/notifications/`                          | List notifications               |
| POST   | `/api/notifications/{id}/mark_as_read/`        | Mark notification as read        |

Full interactive documentation: [swagger](https://kazi-pay.onrender.com/swagger/) · [redoc](https://kazi-pay.onrender.com/redoc/)

---

## Team Lynx

| Name          | Role                          |
| ------------- | ----------------------------- |
| Joseph Omondi | Backend Developer             |
| Wendy Okoth   | Backend Developer             |
| Susan Awori   | Frontend Developer            |
| John Chiwai   | M-Pesa Integration Specialist |
| Gavin Chesebe | Documentation & Presentation  |

---

Built for M‑Pesa Africa x GOMYCODE Kenya Hackathon 2026 – _Money in Motion_
