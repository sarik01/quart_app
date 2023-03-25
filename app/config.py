import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
THREADS_PER_PAGE = 2
CSRF_ENABLED = True
CSRF_SESSION_KEY = "secret"

# SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost:5432/new_agro'

SECRET_KEY = "secret"
FLASK_ADMIN_SWATCH = "yeti"
FLASK_ADMIN_FLUID_LAYOUT = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
MAX_LOGIN_ATTEMPTS = 5
CRONTAB_EXECUTABLE = ''
CRONTAB_LOCK_JOBS = False
REDIS_URL = "redis://:123456@localhost:6379"