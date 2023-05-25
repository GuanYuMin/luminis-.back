from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse
#importaremos la session de la base de datos
from sqlalchemy.orm import Session
#para poder usar el token
from auth.authentication import generate_token ,validate_token
#importando la sessionde base de datos
from utils.Session_bd import get_db
#importando las funciones de auser  
from  functions.user_fumctions import get_user_by_id_function, get_user_by_email_function, get_users_function, create_user_function, update_user_function, delete_user_function , recover_password_function,get_users_function_with_roles_and_photos
#para poder usar el schema de usuario
from schema.authentication_schema import UserBase, UserLogin , UserCreate,UserUpdate
#funciones de utils para hashear la contraseña
from utils.hashed_password import hash_password
#para ingresar a la ruta de user se necesita que el middleware de auth este activo
from middlewares.access_route_for_token import AccessRouteForTokenMiddleware


#router para los usuarios logeados
#user_router = APIRouter(route_class=AccessRouteForTokenMiddleware)
#router para los usuarios no logeados
user_router = APIRouter()

#rruta para obrtener todo el usuariio con los roles y fotos
@user_router.get("/get_users_with_roles_and_photos")
def get_users_with_roles_and_photos(db: Session = Depends(get_db)):
    return get_users_function_with_roles_and_photos(db, skip=0, limit=100)

#ruta para obtener todos los usuarios pero tienen que colocar el token en el header
@user_router.get("/get_users")
def get_users(db: Session = Depends(get_db)):
    return get_users_function(db, skip=0, limit=100)

#obtener usuario por id
@user_router.get("/get_user/{id}")
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return get_user_by_id_function(db, id)

#obtener usuario por email 
@user_router.get("/get_user_by_email/{email}")
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    return get_user_by_email_function(db, email)

#ruta para crear un usuario 
@user_router.post("/create_user")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_function(db, user)

@user_router.put("/update_user/{id}")
def update_user(id: int, user: UserUpdate, db: Session = Depends(get_db), Authorization: str = Header(...)):
    return update_user_function(db, id, user, Authorization)

#ruta para eliminar un usuario
@user_router.delete("/delete_user/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    return delete_user_function(db, id)

# ruta recuperar contraseña
@user_router.post("/recovery_password")
def recovery_password(email: str, db: Session = Depends(get_db)):
    print(email)
    return recover_password_function(db, email)
