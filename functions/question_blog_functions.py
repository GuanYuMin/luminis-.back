from sqlalchemy.orm import Session
from sqlalchemy import update
# importando el packete datetime para poder usarlo en el modelo de usuario
from datetime import datetime
# para poder usar el modelo de usuario
from models.blog_model import Question , Blog

from fastapi.responses import JSONResponse

# funcion para obtener todos las preguntas
def get_questions_function(db: Session, skip: int = 0, limit: int = 100):
    # si no existen preguntas en la base de datos retorna un arreglo vacio
    if db.query(Question).count() == 0:
        return JSONResponse(status_code=404, content={"message": "No existen preguntas en la base de datos"})
    # si existen preguntas en la base de datos retorna un arreglo con las preguntas
    else:
        return db.query(Question).offset(skip).limit(limit).all()

# funcion para crear una pregunta
def create_question_function(db: Session, question: Question):
    # si no existe la pregunta en la base de datos la crea
    if db.query(Question).filter(Question.question == question.question).first() == None:
        if db.query(Blog).filter(Blog.blog_id == question.blog_id).first() != None:
            # creando la pregunta
            db_question = Question(
                question=question.question,
                active=question.active,
                question_timestamp = datetime.now(),
                blog_id=question.blog_id
            )
            db.add(db_question)
            db.commit()
            db.refresh(db_question)
            return JSONResponse(status_code=200, content={"message": "Pregunta creada exitosamente"})
        else:
            return JSONResponse(status_code=404, content={"message": "El blog con el id: " + str(question.blog_id) + " no existe en la base de datos"})
    # si existe la pregunta en la base de datos retorna un mensaje de error
    else:
        return JSONResponse(status_code=404, content={"message": "La pregunta " + question.question + " ya existe en la base de datos"})

# funcion para actualizar una pregunta
def update_question_function(db: Session, question_id: int, question: Question):
    # si existe la pregunta en la base de datos la actualiza
    if db.query(Question).filter(Question.question_id == question_id).first() != None:
        if db.query(Blog).filter(Blog.blog_id == question.blog_id).first() != None:
            # actualizando la pregunta
            db.query(Question).filter(Question.question_id == question_id).update({
                Question.question: question.question,
                Question.active: question.active,
                Question.question_timestamp: datetime.now(),
                Question.blog_id: question.blog_id
            })
            db.commit()
            return JSONResponse(status_code=200, content={"message": "Pregunta actualizada exitosamente"})
        else:
            return JSONResponse(status_code=404, content={"message": "El blog con el blod_id: " + str(question.blog_id) + " no existe en la base de datos"})
    # si no existe la pregunta en la base de datos retorna un mensaje de error
    else:
        return JSONResponse(status_code=404, content={"message": "La pregunta con el question_id: " + str(question_id) + " no existe en la base de datos"})
    
# funcion para eliminar una pregunta
def delete_question_function(db: Session, question_id: int):
    # si existe la pregunta en la base de datos la elimina
    if db.query(Question).filter(Question.question_id == question_id).first() != None:
        # eliminando la pregunta
        db.query(Question).filter(Question.question_id == question_id).delete()
        db.commit()
        return JSONResponse(status_code=200, content={"message": "Pregunta eliminada exitosamente"})
    # si no existe la pregunta en la base de datos retorna un mensaje de error
    else:
        return JSONResponse(status_code=404, content={"message": "La pregunta con el question_id: " + str(question_id) + " no existe en la base de datos"})