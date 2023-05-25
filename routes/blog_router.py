from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse
#importaremos la session de la base de datos
from sqlalchemy.orm import Session
#importando la sessionde base de datos
from utils.Session_bd import get_db
#importando las funciones de auser  
from  functions.blog_functions import get_blogs_function, create_blog_function,update_blog_function , delete_blog_function , get_blogs_by_id_function, get_blogs_function_with_answers
#para poder usar el schema de usuario
from schema.blog_schema import BlogBase , BlogCreate , Blog
#para ingresar a la ruta de user se necesita que el middleware de auth este activo
from middlewares.access_route_for_token import AccessRouteForTokenMiddleware


#router para los usuarios logeados
#user_router = APIRouter(route_class=AccessRouteForTokenMiddleware)
#router para los usuarios no logeados
blog_router = APIRouter()

#ruta para obtener todos los blogs de un usuario con sus preguntas y respuestas
@blog_router.get("/get_blogs_with_answers")
def get_blogs_with_answers(db: Session = Depends(get_db)):
    return get_blogs_function_with_answers(db, skip=0, limit=100)

#ruta para obtener todos los blogs
@blog_router.get("/get_blogs")
def get_blogs(db: Session = Depends(get_db)):
    return get_blogs_function(db, skip=0, limit=100)

#ruta para obtener un usuario por su id
@blog_router.get("/get_blog/{blog_id}")
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    return get_blogs_by_id_function(db, blog_id)

#ruta para crear un blog
@blog_router.post("/create_blog")
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    return create_blog_function(db, blog)

#ruta para actualizar un blog
@blog_router.put("/update_blog/{blog_id}")
def update_blog(blog_id: int, blog: BlogCreate, db: Session = Depends(get_db)):
    return update_blog_function(db, blog_id, blog)

#ruta para eliminar un blog
@blog_router.delete("/delete_blog/{blog_id}")
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    return delete_blog_function(db, blog_id)