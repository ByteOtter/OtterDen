#Copyright ByteOtter (c) 2021-2022

import os

class Config:
    #secret key for tampering protection. 256 Bit python key from secrets module. THIS IS NOT A GOOD ENOUGH OF A SOLUTION.
    SECRET_KEY = os.environ.get('SECRET_KEY')

    #TODO: if database is not present. Have the app create a database file.
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
