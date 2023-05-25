from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse
#importaremos la session de la base de datos
from sqlalchemy.orm import Session
#para poder usar el schema de usuario
from schema.authentication_schema import UserLogin
#para poder usar el token
from auth.authentication import generate_token ,validate_token
#importando la sessionde base de datos
from utils.Session_bd import get_db
#importando utils para verificar la contraseña
from utils.hashed_password import verify_password
#importando las funciones de user 
from functions.user_fumctions import get_user_by_email_function



#router para la autenticacion
authentication_router = APIRouter()

#ruta para el login
@authentication_router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email_function(db, user.email)
    if not db_user:
        return JSONResponse(status_code=404, content={"message": "User not found"})
    if not verify_password(user.password, db_user.password):
        return JSONResponse(status_code=401, content={"message": "Incorrect password"})
    token = generate_token({"id": db_user.id, "email": db_user.email})
    return JSONResponse(status_code=200, content={"token": 'Bearer ' + token, "user_id": db_user.id, "email": db_user.email})


#ruta para verificar el token y que en el docs se pueda probar
@authentication_router.post("/verify_token")
def verify_token(Authorization: str = Header(...)):
    token = Authorization.split(" ")[1]
    validate = validate_token(token, output=True)
    return validate

#ruta para logout
@authentication_router.post("/logout")
def logout():
    return JSONResponse(status_code=200, content={"message": "logout successfully"})