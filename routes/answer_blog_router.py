from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse
#importaremos la session de la base de datos
from sqlalchemy.orm import Session
#importando la sessionde base de datos
from utils.Session_bd import get_db
#importando las funciones de auser  
from  functions.answer_blog_functions import get_answers_function, create_answer_function , update_answer_function , delete_answer_function
#para poder usar el schema de usuario
from schema.blog_schema import AnswerBase , Answer , AnswerCreate , AnswerUpdate
#para ingresar a la ruta de user se necesita que el middleware de auth este activo
from middlewares.access_route_for_token import AccessRouteForTokenMiddleware


#router para los usuarios logeados
#user_router = APIRouter(route_class=AccessRouteForTokenMiddleware)
#router para los usuarios no logeados
answer_blog_router = APIRouter()


#ruta para obtener todos las answers 
@answer_blog_router.get("/get_answers")
def get_answers(db: Session = Depends(get_db)):
    return get_answers_function(db, skip=0, limit=100)

#ruta para crear una answer
@answer_blog_router.post("/create_answer")
def create_answer(answer: AnswerCreate, db: Session = Depends(get_db)):
    return create_answer_function(db, answer)

#ruta para actualizar una answer
@answer_blog_router.put("/update_answer/{answer_id}")
def update_answer(answer_id: int, answer: AnswerUpdate, db: Session = Depends(get_db)):
    return update_answer_function(db, answer_id, answer)

#ruta para eliminar una answer
@answer_blog_router.delete("/delete_answer/{answer_id}")
def delete_answer(answer_id: int, db: Session = Depends(get_db)):
    return delete_answer_function(db, answer_id)