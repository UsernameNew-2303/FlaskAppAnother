import os

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join('agency.db')
SQLALCHEMY_DATABASE_MODIFICATIONS = False

