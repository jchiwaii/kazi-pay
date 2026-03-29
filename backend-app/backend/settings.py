import os
from pathlib import Path
from datetime import timedelta
import dj_database_url
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECURITY ---
SECRET_KEY = config("SECRET_KEY", default="your_secret_key_here")
DEBUG = config("DEBUG", default=True, cast=bool)

# FIX: Added .ngrok-free.app so Africa's Talking can connect to your local server
ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="localhost,127.0.0.1,.ngrok-free.app"
).split(",")

# --- APPLICATION DEFINITION ---
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "drf_yasg",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "allauth",
    "allauth.socialaccount",
    "allauth.account",
]

LOCAL_APPS = [
    "authApp.apps.AuthappConfig",
    "clients.apps.ClientsConfig",
    "workers.apps.WorkersConfig",
    "escrow.apps.EscrowConfig",
    "wallet.apps.WalletConfig",
    "notification.apps.NotificationConfig",
    "adminApp.apps.AdminappConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # Must be at the top
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

SITE_ID = 1
ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

# --- DATABASE ---
DATABASES = {
    "default": dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# --- AUTHENTICATION & REST FRAMEWORK ---
AUTH_USER_MODEL = "authApp.CustomUser"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "authApp.serializers.CustomRegisterSerializer",
}

ACCOUNT_ADAPTER = "authApp.adapters.CustomAccountAdapter"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
}

REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_COOKIE": "access-token",
    "JWT_AUTH_REFRESH_COOKIE": "refresh-token",
    "JWT_AUTH_HTTPONLY": True,
    "JWT_AUTH_SECURE": False,  # Changed to False for local development/Testing
    "JWT_AUTH_SAMESITE": "Lax",
    "LOGIN_SERIALIZER": "authApp.serializers.CustomLoginSerializer",
    "USER_DETAILS_SERIALIZER": "authApp.serializers.UserDetailSerializer",
    'REGISTER_SERIALIZER': 'authApp.serializers.CustomRegisterSerializer',
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:3000",
    "https://kazi-pay-five.vercel.app",
] + [o for o in config("EXTRA_CORS_ORIGINS", default="").split(",") if o]
CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

# --- PASSWORD VALIDATION ---
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- INTERNATIONALIZATION ---
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Nairobi" 
USE_I18N = True
USE_TZ = True

# --- STATIC FILES ---
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# --- DEFAULT AUTO FIELD ---
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- AFRICA'S TALKING CONFIG ---
AT_USERNAME = config("AT_USERNAME", default="sandbox")
AT_API_KEY = config("AT_API_KEY", default="")
AT_PHONE_NUMBER = config("AT_PHONE_NUMBER", default="")
AT_SHORTCODE = config("AT_SHORTCODE", default="23440")

# --- MPESA INTEGRATION ---
MPESA_ENVIRONMENT = config("MPESA_ENVIRONMENT", default="sandbox")
MPESA_CONSUMER_KEY = config("MPESA_CONSUMER_KEY", default="")
MPESA_CONSUMER_SECRET = config("MPESA_CONSUMER_SECRET", default="")
MPESA_SHORTCODE = config("MPESA_SHORTCODE", default="")
MPESA_PASSKEY = config("MPESA_PASSKEY", default="")
MPESA_INITIATOR_NAME = config("MPESA_INITIATOR_NAME", default="")
MPESA_SECURITY_CREDENTIAL = config("MPESA_SECURITY_CREDENTIAL", default="")
MPESA_C2B_CALLBACK_URL = config("MPESA_C2B_CALLBACK_URL", default="")
MPESA_B2C_CALLBACK_URL = config("MPESA_B2C_CALLBACK_URL", default="")
MPESA_B2C_TIMEOUT_URL = config("MPESA_B2C_TIMEOUT_URL", default=MPESA_B2C_CALLBACK_URL)

# --- ALLAUTH ADDITIONAL CONFIG ---
ACCOUNT_LOGIN_METHODS = ["username"]
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# --- CSRF CONFIGURATION ---
# This allows Africa's Talking to send POST requests to your Ngrok URL
CSRF_TRUSTED_ORIGINS = [
    "https://cordie-unladen-lena.ngrok-free.dev",
    "http://cordie-unladen-lena.ngrok-free.dev",
]

APPEND_SLASH = False
