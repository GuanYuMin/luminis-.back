from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse
#importaremos la session de la base de datos
from sqlalchemy.orm import Session
#importando la sessionde base de datos
from utils.Session_bd import get_db
#importando las funciones de auser  
from functions.photo_functions import get_photos_function, get_photo_by_id_function, create_photo_function,delete_photo_function,update_photo_function
#para poder usar el schema de usuario
from schema.photo_schema import  PhotoBase, PhotoCreate, PhotoUpdate,Photo


#router para los photos logeados
#role_router = APIRouter(route_class=AccessRouteForTokenMiddleware)
#router para los photos no logeados
photo_router = APIRouter()

#obtener todos los photos
@photo_router.get("/photos/")
def get_photos(db: Session = Depends(get_db)):
    return get_photos_function(db, skip=0, limit=100)

#obtener un photo por id
@photo_router.get("/photos/{id}")
def get_photo_by_id(id: int, db: Session = Depends(get_db)):
    return get_photo_by_id_function(db, id)

#crear un photo
@photo_router.post("/photos/")
def create_photo(photo: PhotoCreate, db: Session = Depends(get_db)):
    return create_photo_function(db=db, photo=photo)

#actualizar un photo
@photo_router.put("/photos/{id}")
def update_photo(id: int, photo: PhotoUpdate, db: Session = Depends(get_db)):
    return update_photo_function(db=db, id=id, photo=photo)

#eliminar un photo
@photo_router.delete("/photos/{id}")
def delete_photo(id: int, db: Session = Depends(get_db)):
    return delete_photo_function(db=db, id=id)
