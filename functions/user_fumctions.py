from sqlalchemy.orm import Session
from sqlalchemy import update
# importando el packete datetime para poder usarlo en el modelo de usuario
from datetime import datetime
# para poder usar el modelo de usuario
from models.authentication_model import User, Role, Photo
# schema de usuario
from schema.authentication_schema import UserBase, UserLogin, UserUpdate, UserCreate, EmailSchema
# funciones de utils para hashear la contraseña
from utils.hashed_password import hash_password
# para poder usar el token
from auth.authentication import validate_token
# imporatndo fastap_email para poder enviar correos
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
# importando la configuracion desde utils
from utils.Connection_Email_config import send_email
from utils.generate_password import generate_password
from fastapi.responses import JSONResponse


# funcion para obtener todos los usuarios con sus roles y fotos
def get_users_function_with_roles_and_photos(db: Session, skip: int = 0, limit: int = 100):
    # si no existen usuarios en la base de datos retorna un arreglo vacio
    if db.query(User).count() == 0:
        return JSONResponse(status_code=404, content={"message": "No existen usuarios en la base de datos"})
    # si existen photos en la base de datos retorna un arreglo con las photos
    else:
        users = db.query(User).offset(skip).limit(limit).all()
        for user in users:
            user.roles = db.query(Role).filter(Role.id == user.role_id).first()
            user.photos = db.query(Photo).filter(Photo.id == user.id).all()
        return users

# funcion para obtener todos los usuarios


def get_users_function(db: Session, skip: int = 0, limit: int = 100):
    # si no existen usuarios en la base de datos retorna un arreglo vacio
    if db.query(User).count() == 0:
        return JSONResponse(status_code=404, content={"message": "No existen usuarios en la base de datos"})
    # si existen usuarios en la base de datos retorna un arreglo con los usuarios
    else:
        return db.query(User).offset(skip).limit(limit).all()

# funcion para obtener el usuario por el id


def get_user_by_id_function(db: Session, id: int):
    # si no exite el id del usuario en la base de datos retorna un mensaje de error
    if db.query(User).filter(User.id == id).count() == 0:
        return JSONResponse(status_code=404, content={"message": "No existe el usuario en la base de datos"})
    # si existe el id del usuario en la base de datos retorna el usuario
    else:
        return db.query(User).filter(User.id == id).first()

# funcion para obtener el usuario por el email


def get_user_by_email_function(db: Session, email: str):
    # si no exite el email del usuario en la base de datos retorna un mensaje de error
    if db.query(User).filter(User.email == email).count() == 0:
        return JSONResponse(status_code=404, content={"message": "No existe el usuario conn el email ingresado en la base de datos"})
    return db.query(User).filter(User.email == email).first()

# funcion para crear un usuario


def create_user_function(db: Session, user: UserCreate):
    # validar que el rol exista
    if db.query(Role).filter(Role.id == user.role_id).count() == 0:
        return JSONResponse(status_code=404, content={"message": "No existe el rol ingresado en la base de datos"})
    # validar quela photo exista
    if db.query(Photo).filter(Photo.id == user.photo_id).count() == 0:
        return JSONResponse(status_code=404, content={"message": "El id de la foto ingresada no existe en la base de datos"})
    # si el email del usuario ya existe en la base de datos retorna un mensaje de error
    if db.query(User).filter(User.email == user.email).count() != 0:
        return JSONResponse(status_code=404, content={"message": "Ya existe un usuario con el email ingresado en la base de datos"})
    #validar que el formato de fecha sea de la forma correcta 23/12/1998 dia/mes/año
    try:
        datetime.strptime(user.birthdate, '%d/%m/%Y')
    except ValueError:
        return JSONResponse(status_code=404, content={"message": "El formato de fecha ingresado no es correcto, debe ser dia/mes/año"})
    # si el username del usuario ya existe en la base de datos retorna un mensaje de error
    else:
        # se crea el usuario
        db_user = User(
            email=user.email,
            password=hash_password(user.password),
            old_password="",
            username=user.username,
            name=user.name,
            midlename=user.midlename,
            lastname=user.lastname,
            birthdate=user.birthdate,
            phone=user.phone,
            role_id=user.role_id,
            photo_id=user.photo_id,
            is_activate=1,
        )
        # se agrega el usuario a la base de datos
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return JSONResponse(status_code=200, content={"message": "Usuario creado correctamente"})

# funcion para actualizar un usuario siempre y cuando valide el token


def update_user_function(db: Session, id: int, user: UserUpdate, Autorization: str):
    # validar el token
    token = Autorization.split(" ")[1]
    validate = validate_token(token, output=True)
    if validate['status'] == 200:
        id_user = validate['data']['id']
        if id_user != id:
            return JSONResponse(status_code=404, content={"message": "No tienes permisos para actualizar este usuario"})
        # validar el role
        if db.query(Role).filter(Role.id == user.role_id).count() == 0:
            return JSONResponse(status_code=404, content={"message": "No existe el rol del usuario que quieres modificar"})
        # validar la photo
        if db.query(Photo).filter(Photo.id == user.photo_id).count() == 0:
            return JSONResponse(status_code=404, content={"message": "No existe la foto del usuario que quieres modificar"})
        # si el id a actualizar no existe en la base de datos retorna un mensaje de error
        if db.query(User).filter(User.id == id).count() == 0:
            return JSONResponse(status_code=404, content={"message": "No existe el usuario a actualizar en la base de datos"})
        else:
            # se actualiza el usuario
            db_user = db.query(User).filter(User.id == id).first()
            db_user.email = user.email
            db_user.old_password = db_user.password
            db_user.password = hash_password(user.password)
            db_user.username = user.username
            db_user.name = user.name
            db_user.midlename = user.midlename
            db_user.lastname = user.lastname
            db_user.birthdate = user.birthdate
            db_user.phone = user.phone
            db_user.role_id = user.role_id
            db_user.photo_id = user.photo_id
            db_user.is_activate = user.is_activate
            db.commit()
            return JSONResponse(status_code=200, content={"message": "Usuario actualizado correctamente"})
    else:
        return JSONResponse(status_code=validate["status"], content={"message": validate["message"]})

# funcion para eliminar un usuario


def delete_user_function(db: Session, id: int):
    # si el id a eliminar no existe en la base de datos retorna un mensaje de error
    if db.query(User).filter(User.id == id).count() == 0:
        return JSONResponse(status_code=404, content={"message": "No existe el usuario a eliminar en la base de datos"})
    db_user = db.query(User).filter(User.id == id)
    db_user.delete()
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Usuario eliminado correctamente"})

# funcion para Recuperar contraseña


async def recover_password_function(db: Session, email: EmailSchema):

    email = email.dict().get("email")[0]
    print(email)

    if db.query(User).filter(User.email == email).count() == 0:
        return JSONResponse(status_code=404, content={"message": "No existe el usuario con el email ingresado en la base de datos"})
    else:
        # se obtiene el usuario
        db_user = db.query(User).filter(User.email == email).first()
        # se genera una contraseña aleatoria
        password = generate_password()
        print(password)
        # se actualiza la contraseña del usuario
        db_user.old_password = db_user.password
        db_user.password = hash_password(password)
        db.commit()
        # se envia el correo con la nueva contraseña
        send_email(email, 'Recuperar Contraseña', f'Nueva contraseña: {password}')
        return JSONResponse(status_code=200, content={"message": "Se ha enviado un correo con la nueva contraseña"})