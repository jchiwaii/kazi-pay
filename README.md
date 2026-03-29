# KaziPay – Secure Escrow for Kenya’s Gig Economy

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Built with Django](https://img.shields.io/badge/Built%20with-Django-092E20?logo=django)](https://www.djangoproject.com/)
[![React](https://img.shields.io/badge/Frontend-React-61DAFB?logo=react)](https://reactjs.org/)
[![M‑Pesa](https://img.shields.io/badge/Powered%20by-M‑Pesa-00A859?logo=safaricom)](https://developer.safaricom.co.ke/)


KaziPay is an escrow platform for Kenya's gig economy – built for the M‑Pesa Africa x GOMYCODE Hackathon 2026.

**Live Demo:** [https://kazi-pay-five.vercel.app/](https://kazi-pay-five.vercel.app/)

## Test Accounts

| Username | Phone Number | Password | Role |
|----------|--------------|----------|------|
| amina_client | 254711000001 | SecureK@zi99! | Client |
| brian_plumber | 254711000002 | SecureK@zi99! | Worker |

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
8. **Withdraw to M‑Pesa** – Worker can cash out anytime

---

## Problem

Kenya's informal workers (5M+) face a two‑sided trust gap: workers fear non‑payment; clients fear paying upfront for poor work.

## Solution

We're building a web‑based escrow system using M‑Pesa STK Push and B2C. Clients deposit funds, workers accept jobs, and payment is released only after client confirmation.

---

## Core Features

- **Secure Authentication** – Register/login with phone number or email/password. JWT tokens secure all API requests. Roles: Client, Worker, or Both.

- **M‑Pesa Escrow Payments** – Clients pay via STK Push; funds are held until the job is completed. Workers receive payment instantly via B2C after client confirmation.

![alt text](https://raw.githubusercontent.com/susan-awori/kazi-pay/refs/heads/main/screenshots/mpesa%20prompt/WhatsApp%20Image%202026-03-29%20at%208.18.58%20PM.jpeg "Pay via STK push")

- **Job Management** – Clients post jobs with description, amount, and target worker. Workers view and accept available jobs. Clients confirm completion to release payment.

![alt text](https://raw.githubusercontent.com/susan-awori/kazi-pay/refs/heads/main/screenshots/worker%20invoice%20sent/WhatsApp%20Image%202026-03-29%20at%208.18.56%20PM.jpeg "Invoice Sent")

- **Bidding System** – Workers submit competitive bids with proposals. Clients review and select the best fit for their job.

- **Digital Wallet** – Every user has a wallet to track balance, view transaction history, and withdraw funds to M‑Pesa.

![alt text](https://raw.githubusercontent.com/susan-awori/kazi-pay/refs/heads/main/screenshots/kazipay%20client/WhatsApp%20Image%202026-03-29%20at%208.18.57%20PM.jpeg)

![alt text](https://raw.githubusercontent.com/susan-awori/kazi-pay/refs/heads/main/screenshots/kazipay%20worker%20profile/WhatsApp%20Image%202026-03-29%20at%2010.54.03%20AM.jpeg)

- **Real‑time Notifications** – In-app notifications keep both parties informed at every step: bid accepted, payment received, job completed, funds released.

- **Dispute Resolution** – Either party can raise disputes with detailed reasons. Admin reviews and mediates to ensure fair outcomes.

- **Auto‑Release Mechanism** – If the client does not confirm within 48 hours of worker completion, the system automatically pays the worker (protects workers from unresponsive clients).

- **Transaction History** – Every deposit and payout is logged in a transaction model for full transparency.

- **Dual‑Role Dashboards** – Separate interfaces for clients (post jobs, track active jobs, confirm completion) and workers (browse available jobs, see accepted jobs, track earnings).

![alt text](https://raw.githubusercontent.com/susan-awori/kazi-pay/refs/heads/main/screenshots/kazipay%20client/WhatsApp%20Image%202026-03-29%20at%208.18.57%20PM.jpeg "KaziPay Client")

![alt text](https://raw.githubusercontent.com/susan-awori/kazi-pay/refs/heads/main/screenshots/kazi%20pay%20worker/WhatsApp%20Image%202026-03-29%20at%2010.54.03%20AM.jpeg "KaziPay Worker")

- **Responsive Web Interface** – Built with React and Tailwind CSS, works seamlessly on desktop and mobile.

---

## Tech Stack

| Category | Technology |
|----------|------------|
| **Backend** | Django 6.0.3, Django REST Framework |
| **Database** | PostgreSQL (Production), SQLite (Development) |
| **Frontend** | React 18, Vite, Tailwind CSS |
| **Authentication** | JWT (Simple JWT), dj-rest-auth |
| **M‑Pesa Integration** | Safaricom Daraja API (STK Push, B2C) |
| **SMS** | Africa's Talking API |
| **Deployment** | Render (Backend), Vercel (Frontend) |
| **API Documentation** | drf-yasg (Swagger/ReDoc) |
| **Environment Management** | python-decouple |
| **Static Files** | WhiteNoise |

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
│   │   ├── models.py              # CustomUser model
│   │   ├── serializers.py         # Auth serializers
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
│   │   ├── views.py               # Submit bid, view jobs
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
│   │   ├── views.py               # Dispute resolution
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
│   │   ├── api.js                 # API client (axios)
│   │   ├── main.jsx               # React entry point
│   │   └── index.css              # Global styles + Tailwind
│   │
│   ├── index.html                 # HTML template
│   ├── package.json               # NPM dependencies
│   ├── vite.config.js             # Vite configuration
│   ├── tailwind.config.js         # Tailwind CSS config
│   └── vercel.json                # Vercel deployment
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
   
   Create a `.env` file in the `backend-app/` directory (see `.env.example` below):

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser** (optional for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```
   
   Backend will be available at `http://localhost:8000`

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
   
   Create a `.env` file in `frontend-app/` directory:
   ```env
   VITE_API_BASE_URL=http://localhost:8000/api
   ```

4. **Run development server**
   ```bash
   npm run dev
   ```
   
   Frontend will be available at `http://localhost:5173`

5. **Build for production**
   ```bash
   npm run build
   ```

---

## Environment Variables

### Backend (.env.example)

Create a `.env` file in `backend-app/` with the following variables:

```env
# Django Settings
SECRET_KEY=your-super-secret-key-here-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,.ngrok-free.app

# Database (PostgreSQL for production, SQLite for development)
# For PostgreSQL:
DATABASE_URL=postgresql://user:password@localhost:5432/kazipay_db
# For SQLite (default if DATABASE_URL not set):
# Will use db.sqlite3 in backend-app directory

# CORS Settings
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000,https://kazi-pay-five.vercel.app
CORS_ALLOW_ALL_ORIGINS=False

# CSRF Trusted Origins (for production and ngrok testing)
CSRF_TRUSTED_ORIGINS=https://your-production-domain.com,https://your-ngrok-url.ngrok-free.app

# M-Pesa/Daraja API Configuration
MPESA_ENVIRONMENT=sandbox
# Get from https://developer.safaricom.co.ke/
MPESA_CONSUMER_KEY=your_mpesa_consumer_key_here
MPESA_CONSUMER_SECRET=your_mpesa_consumer_secret_here
MPESA_SHORTCODE=174379
MPESA_PASSKEY=your_mpesa_passkey_here
MPESA_INITIATOR_NAME=testapi
MPESA_SECURITY_CREDENTIAL=your_security_credential_here

# M-Pesa Callback URLs (must be publicly accessible HTTPS URLs)
MPESA_C2B_CALLBACK_URL=https://your-domain.com/api/escrow/mpesa-callback
MPESA_B2C_CALLBACK_URL=https://your-domain.com/api/wallet/b2c-callback
MPESA_B2C_TIMEOUT_URL=https://your-domain.com/api/wallet/b2c-callback

# Africa's Talking Configuration
AT_USERNAME=sandbox
# Get from https://africastalking.com/
AT_API_KEY=your_africas_talking_api_key_here
AT_PHONE_NUMBER=your_shortcode_or_sender_id
AT_SHORTCODE=23440
```

### Frontend (.env.example)

Create a `.env` file in `frontend-app/` with:

```env
# API Base URL
VITE_API_BASE_URL=http://localhost:8000/api
# For production:
# VITE_API_BASE_URL=https://your-backend-domain.com/api
```

### Getting API Credentials

1. **M-Pesa Daraja API**
   - Sign up at [https://developer.safaricom.co.ke/](https://developer.safaricom.co.ke/)
   - Create an app to get Consumer Key and Consumer Secret
   - Use sandbox credentials for testing (Shortcode: 174379)

2. **Africa's Talking**
   - Sign up at [https://africastalking.com/](https://africastalking.com/)
   - Get your API Key from the dashboard
   - Use sandbox mode for testing

---

## Testing the Application

### Local Testing

1. Start the backend server on port 8000
2. Start the frontend server on port 5173
3. Use the test accounts provided above to log in
4. Test the complete flow:
   - **As Client (amina_client):**
     - Post a new job
     - Wait for a bid from brian_plumber
     - Accept the bid
     - Confirm STK Push on your phone (in sandbox, use test credentials)
     - After worker marks complete, release the funds
   - **As Worker (brian_plumber):**
     - Browse available jobs
     - Submit a bid on amina_client's job
     - Wait for acceptance
     - Mark the job as complete
     - Check wallet for received payment

### Using Ngrok for M-Pesa Callbacks

M-Pesa requires public HTTPS URLs for callbacks. Use ngrok during development:

```bash
# Install ngrok
npm install -g ngrok

# Expose Django server
ngrok http 8000

# Copy the HTTPS URL and update your .env:
MPESA_C2B_CALLBACK_URL=https://your-ngrok-url.ngrok-free.app/api/escrow/mpesa-callback
CSRF_TRUSTED_ORIGINS=https://your-ngrok-url.ngrok-free.app

# Restart Django server to apply changes
```

---

## Team Lynx

| Name | Role |
|------|------|
| Joseph Omondi | Backend Developer |
| Wendy Okoth | Backend Developer |
| Susan Awori | Frontend Developer |
| John Chiwai | M-Pesa Integration Specialist |
| Gavin Chesebe | Documentation & Presentation |

---

Built for M‑Pesa Africa x GOMYCODE Kenya Hackathon 2026 – *Money in Motion*
