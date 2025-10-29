import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "lab2-demo-secret-key"
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "flatpages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "firstwebpage.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Per the method: DIRS points to the 'flatpages' folder itself,
        # and templates are referenced as 'templates/index.html'.
        "DIRS": [os.path.join(BASE_DIR, "flatpages")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.static",
            ],
        },
    },
]

WSGI_APPLICATION = "firstwebpage.wsgi.application"

# Per the method (Lab 1): set NAME to os.path.join(BASE_DIR, "db_project_name")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db_firstwebpage"),
    }
}

LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# STATIC settings – keep defaults but define STATIC_URL as usual
# The method links CSS via { STATIC_URL }/static/index.css; to satisfy that, we also include
# a nested file at /static/static/index.css.
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    # allow serving our app's static folder directly in development
    os.path.join(BASE_DIR, "flatpages", "static"),
]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
