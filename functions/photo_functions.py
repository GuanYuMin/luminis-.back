from sqlalchemy.orm import Session
#para poder usar el modelo de role
from models.authentication_model import Photo , User
# para poder usar el schema de role
from schema.photo_schema import PhotoBase, PhotoCreate, PhotoUpdate
from fastapi.responses import JSONResponse

#funcion para obtener todos las fotos
def get_photos_function(db: Session, skip: int = 0, limit: int = 100):
    #si no hay roles entonces no se puede obtener nada
    if not db.query(Photo).first():
        return JSONResponse(status_code=404, content={"message": "Photos does not exist"})
    return db.query(Photo).offset(skip).limit(limit).all()

#funcion para obtener una foto
def get_photo_by_id_function(db: Session, id: int):
    #si el id de la foto no existe entonces no se puede obtener
    if not db.query(Photo).filter(Photo.id == id).first():
        return JSONResponse(status_code=404, content={"message": "Photo id does not exist"})
    return db.query(Photo).filter(Photo.id == id).first()

#funcion para crear una foto
def create_photo_function(db: Session , photo: PhotoCreate):
    #validar que el nombre de la foto no exista
    if db.query(Photo).filter(Photo.photo_name == photo.photo_name).first():
        return JSONResponse(status_code=404, content={"message": "Photo name already exists"})
    #validar que la url de la foto no exista
    if db.query(Photo).filter(Photo.photo_url == photo.photo_url).first():
        return JSONResponse(status_code=404, content={"message": "Photo url already exists"})
    db_photo = Photo(photo_name=photo.photo_name, photo_url=photo.photo_url, is_activate=photo.is_activate)
    db.add(db_photo)
    db.commit()
    db.refresh(db_photo)
    return db_photo

#funcion para actualizar una foto
def update_photo_function(db: Session, id: int, photo: PhotoUpdate):
    #si el id de la foto no existe entonces no se puede actualizar
    if not db.query(Photo).filter(Photo.id == id).first():
        return JSONResponse(status_code=404, content={"message": "Photo id does not exist"})
    db_photo = db.query(Photo).filter(Photo.id == id).first()
    db_photo.photo_name = photo.photo_name
    db_photo.photo_url = photo.photo_url
    db_photo.is_activate = photo.is_activate
    db.commit()
    db.refresh(db_photo)
    return db_photo

#funcion para eliminar una foto
def delete_photo_function(db: Session, id: int):
    #si el id de la foto no existe entonces no se puede eliminar
    if not db.query(Photo).filter(Photo.id == id).first():
        return JSONResponse(status_code=404, content={"message": "Photo id does not exist"})
    db_photo = db.query(Photo).filter(Photo.id == id).first()
    db.delete(db_photo)
    db.commit()
    return db_photo