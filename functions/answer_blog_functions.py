from sqlalchemy.orm import Session
from sqlalchemy import update
# importando el packete datetime para poder usarlo en el modelo de usuario
from datetime import datetime
# para poder usar el modelo de usuario
from models.blog_model import Question , Answer

from fastapi.responses import JSONResponse

# funcion para obtener todos las respuestas
def get_answers_function(db: Session, skip: int = 0, limit: int = 100):
    if db.query(Answer).count() == 0:
        return JSONResponse(status_code=404, content={"message": "No existen respuestas en la base de datos"})
    else:
        return db.query(Answer).offset(skip).limit(limit).all()

# funcion para crear una respuesta
def create_answer_function(db: Session, answer: Answer):
    # si no existe la respuesta en la base de datos la crea
    if db.query(Answer).filter(Answer.answer == answer.answer).first() == None:
        if db.query(Question).filter(Question.question_id == answer.question_id).first() != None:
            # creando la respuesta
            db_answer = Answer(
                answer=answer.answer,
                active=answer.active,
                answer_timestamp = datetime.now(),
                question_id=answer.question_id
            )
            db.add(db_answer)
            db.commit()
            db.refresh(db_answer)
            return JSONResponse(status_code=200, content={"message": "Respuesta creada exitosamente"})
        else:
            return JSONResponse(status_code=404, content={"message": "La pregunta con el question_id: " + str(answer.question_id) + " no existe en la base de datos por lo tanto no se puede crear la respuesta"})
    # si existe la respuesta en la base de datos retorna un mensaje de error
    else:
        return JSONResponse(status_code=404, content={"message": "La respuesta " + answer.answer + " ya existe en la base de datos"})
    
# funcion para actualizar una respuesta
def update_answer_function(db: Session, answer_id: int, answer: Answer):
    # si existe la respuesta en la base de datos la actualiza
    if db.query(Answer).filter(Answer.answer_id == answer_id).first() != None:
        if db.query(Question).filter(Question.question_id == answer.question_id).first() != None:
            # actualizando la respuesta
            db.query(Answer).filter(Answer.answer_id == answer_id).update({
                Answer.answer: answer.answer,
                Answer.active: answer.active,
                Answer.answer_timestamp: datetime.now(),
                Answer.question_id: answer.question_id
            })
            db.commit()
            return JSONResponse(status_code=200, content={"message": "Respuesta actualizada exitosamente"})
        else:
            return JSONResponse(status_code=404, content={"message": "La pregunta con el question_id: " + str(answer.question_id) + " no existe en la base de datos"})
    # si no existe la respuesta en la base de datos retorna un mensaje de error
    else:
        return JSONResponse(status_code=404, content={"message": "La respuesta con el answer_id: " + str(answer_id) + " no existe en la base de datos"})
    
# funcion para eliminar una respuesta
def delete_answer_function(db: Session, answer_id: int):
    # si existe la respuesta en la base de datos la elimina
    if db.query(Answer).filter(Answer.answer_id == answer_id).first() != None:
        db.query(Answer).filter(Answer.answer_id == answer_id).delete()
        db.commit()
        return JSONResponse(status_code=200, content={"message": "Respuesta eliminada exitosamente"})
    # si no existe la respuesta en la base de datos retorna un mensaje de error
    else:
        return JSONResponse(status_code=404, content={"message": "La respuesta con el answer_id: " + str(answer_id) + " no existe en la base de datos"})