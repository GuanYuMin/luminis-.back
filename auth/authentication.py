from fastapi.responses import JSONResponse
from jwt import encode,decode
from jwt import exceptions
from datetime import datetime, timedelta
from dotenv import load_dotenv

# cargar las variables de entorno
load_dotenv()

from os import getenv

def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date

def generate_token(data : dict):
    token = encode(payload={**data,"exp": expire_date(1) }, key=getenv("SECRET_TOKEN"), algorithm="HS256")
    return token

def validate_token(token, output = False):
    try:
        decoded_token = decode(token, key=getenv("SECRET_TOKEN"), algorithms=["HS256"])

        if output:
            return {
                "status": 200,
                "data": decoded_token
            }

        return {"status": 200}
    except exceptions.DecodeError:
        return {
            "status": 401,
            "message": "Invalid token"
        }
    except exceptions.ExpiredSignatureError:
        return {
            "status": 401,
            "message": "Token expired"
        }