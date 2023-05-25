from sqlalchemy.orm import Session
#para poder usar el modelo de role
from models.authentication_model import Role
# para poder usar el schema de role
from schema.role_schema import RoleBase, RoleCreate, RoleUpdate 
from fastapi.responses import JSONResponse

#funcion para obtener todos los roles
def get_roles_function(db: Session, skip: int = 0, limit: int = 100):
    #si no hay roles entonces no se puede obtener nada
    if not db.query(Role).offset(skip).limit(limit).all():
        return JSONResponse(status_code=404, content={"message": "No roles found"})
    return db.query(Role).offset(skip).limit(limit).all()

#funcion para obtener el rol por el id
def get_role_by_id_function(db: Session, id: int):
    #si el id del rol no existe entonces no se puede obtener
    if not db.query(Role).filter(Role.id == id).first():
        return JSONResponse(status_code=404, content={"message": "Role id does not exist"})
    return db.query(Role).filter(Role.id == id).first()

#funcion para crear un rol
def create_role_function(db: Session , role: RoleCreate):
    #si el nombre del rol ya existe entonces no se puede crear
    if db.query(Role).filter(Role.name == role.name).first():
        return JSONResponse(status_code=404, content={"message": "Role name already exists"})
    db_role = Role(name=role.name, description=role.description)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

#funcion para actualizar un rol
def update_role_function(db: Session, id: int, role: RoleUpdate):
    #si el id del rol no existe entonces no se puede actualizar
    if not db.query(Role).filter(Role.id == id).first():
        return JSONResponse(status_code=404, content={"message": "Role id does not exist"})
    db_role = db.query(Role).filter(Role.id == id).first()
    db_role.name = role.name
    db_role.description = role.description
    db.commit()
    db.refresh(db_role)
    return db_role

#funcion para eliminar un rol
def delete_role_function(db: Session, id: int):
    #si el id del rol no existe entonces no se puede eliminar
    if not db.query(Role).filter(Role.id == id).first():
        return JSONResponse(status_code=404, content={"message": "Role id does not exist"})
    db_role = db.query(Role).filter(Role.id == id).first()
    db.delete(db_role)
    db.commit()
    return db_role
