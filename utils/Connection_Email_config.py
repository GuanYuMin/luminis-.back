from fastapi_mail import ConnectionConfig

conf = ConnectionConfig(
            MAIL_USERNAME = "correogmail",
            MAIL_PASSWORD = "correogmail",
            MAIL_FROM = "correogmail@gmail.com",
            MAIL_PORT = 587,
            MAIL_SERVER = "smtp.gmail.com",
            MAIL_STARTTLS = False,
            MAIL_SSL_TLS = True,
            USE_CREDENTIALS = True,
            VALIDATE_CERTS = True,
            )
