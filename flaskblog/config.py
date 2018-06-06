import os

class Config:
    SECRET_KEY = 'xxxxx1111'  # os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # os.environ.get('SQLALCHEMY_DATABASE_URI')  # '///' = relative path from current file
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME= os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')