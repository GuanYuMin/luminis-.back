from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse
#importaremos la session de la base de datos
from sqlalchemy.orm import Session
#importando la sessionde base de datos
from utils.Session_bd import get_db
#importando las funciones de auser  
from  functions.roles_functions import get_role_by_id_function, get_roles_function, create_role_function, update_role_function, delete_role_function
#para poder usar el schema de usuario
from schema.role_schema import  RoleBase, RoleCreate, RoleUpdate,Role


#router para los roles logeados
#role_router = APIRouter(route_class=AccessRouteForTokenMiddleware)
#router para los roles no logeados
role_router = APIRouter()

#ruta para obtener todos los roles
@role_router.get("/get_roles")
def get_roles(db: Session = Depends(get_db)):
    return get_roles_function(db, skip=0, limit=100)

#obtener rol por id
@role_router.get("/get_role/{id}")
def get_role_by_id(id: int, db: Session = Depends(get_db)):
    return get_role_by_id_function(db, id)

#ruta para crear un rol
@role_router.post("/create_role")
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    return create_role_function(db, role)

#ruta para actualizar un rol solo con algunos campos
@role_router.put("/update_role/{id}")
def update_role(id: int, role: RoleUpdate, db: Session = Depends(get_db)):
    return update_role_function(db, id, role)

#ruta para eliminar un rol
@role_router.delete("/delete_role/{id}")
def delete_role(id: int, db: Session = Depends(get_db)):
    return delete_role_function(db, id)
