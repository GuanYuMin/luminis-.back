from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse
#importaremos la session de la base de datos
from sqlalchemy.orm import Session
#importando la sessionde base de datos
from utils.Session_bd import get_db
#importando las funciones de auser  
from  functions.question_blog_functions import get_questions_function , create_question_function , update_question_function , delete_question_function
#para poder usar el schema de usuario
from schema.blog_schema import QuestionBase , Question , QuestionCreate, QuestionUpdate , QuestionDelete
#para ingresar a la ruta de user se necesita que el middleware de auth este activo
from middlewares.access_route_for_token import AccessRouteForTokenMiddleware


#router para los usuarios logeados
#user_router = APIRouter(route_class=AccessRouteForTokenMiddleware)
#router para los usuarios no logeados
question_blog_router = APIRouter()


#ruta para obtener todos los usuarios pero tienen que colocar el token en el header
@question_blog_router.get("/get_questions")
def get_questions(db: Session = Depends(get_db)):
    return get_questions_function(db, skip=0, limit=100)

#ruta para crear una pregunta de blog
@question_blog_router.post("/create_question")
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    return create_question_function(db, question)

#ruta para actualizar una pregunta de blog
@question_blog_router.put("/update_question/{question_id}")
def update_question(question_id: int, question: QuestionUpdate, db: Session = Depends(get_db)):
    return update_question_function(db, question_id, question)

#ruta para eliminar una pregunta de blog
@question_blog_router.delete("/delete_question/{question_id}")
def delete_question(question_id: int, db: Session = Depends(get_db)):
    return delete_question_function(db, question_id)