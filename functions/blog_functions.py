from sqlalchemy.orm import Session
from sqlalchemy import update
# importando el packete datetime para poder usarlo en el modelo de usuario
from datetime import datetime
# para poder usar el modelo de usuario
from models.blog_model import Blog , Question , Answer

from fastapi.responses import JSONResponse

#ruta para obtener todos los blogs de un usuario con sus preguntas y respuestas
def get_blogs_function_with_answers(db: Session, skip: int = 0, limit: int = 100):
    # si no existen blogs en la base de datos retorna un arreglo vacio
    if db.query(Blog).count() == 0:
        return JSONResponse(status_code=404, content={"message": "No existen blogs en la base de datos"})
    # si existen blogs en la base de datos retorna un arreglo con los blogs
    else:
        blogs = db.query(Blog).offset(skip).limit(limit).all()
        for blog in blogs:
            blog.questions = db.query(Question).filter(Question.blog_id == blog.blog_id).all()
            for question in blog.questions:
                question.answers = db.query(Answer).filter(Answer.question_id == question.question_id).all()
        return blogs

# funcion para obtener todos los blogs
def get_blogs_function(db: Session, skip: int = 0, limit: int = 100):
    # si no existen blogs en la base de datos retorna un arreglo vacio
    if db.query(Blog).count() == 0:
        return JSONResponse(status_code=404, content={"message": "No existen blogs en la base de datos"})
    # si existen blogs en la base de datos retorna un arreglo con los blogs
    else:
        return db.query(Blog).offset(skip).limit(limit).all()

# funcion para obtener un blog por su id
def get_blogs_by_id_function(db: Session, blog_id: int):
    # si no existe el blog en la base de datos retorna un mensaje de error
    if db.query(Blog).filter(Blog.blog_id == blog_id).first() == None:
        return JSONResponse(status_code=404, content={"message": "El blog con el id " + str(blog_id) + " no existe"})
    # si existe el blog en la base de datos retorna el blog
    else:
        return db.query(Blog).filter(Blog.blog_id == blog_id).first()

# funcion para crear un blog
def create_blog_function(db: Session, blog: Blog):
    # si no existe el blog en la base de datos lo crea
    if db.query(Blog).filter(Blog.title == blog.title).first() == None:
        # creando el blog
        db_blog = Blog(
            title=blog.title,
            sub_title=blog.sub_title,
            content=blog.content,
            image=blog.image,
            author=blog.author,
            active=blog.active,
            category=blog.category,
            registration_timestamp = datetime.now(),
            update_timestamp = datetime.now()
        )
        db.add(db_blog)
        db.commit()
        db.refresh(db_blog)
        return JSONResponse(status_code=200, content={"message": "Blog creado exitosamente"})
    # si existe el blog en la base de datos retorna un mensaje de error
    else:
        return JSONResponse(status_code=404, content={"message": "El blog ya existe en la base de datos"})

# funcion para actualizar un blog
def update_blog_function(db: Session, blog_id: int, blog: Blog):
    # si existe el blog en la base de datos lo actualiza
    if db.query(Blog).filter(Blog.blog_id == blog_id).first() != None:
        # actualizando el blog
        db.query(Blog).filter(Blog.blog_id == blog_id).update({
            Blog.title: blog.title,
            Blog.sub_title: blog.sub_title,
            Blog.content: blog.content,
            Blog.image: blog.image,
            Blog.author: blog.author,
            Blog.active: blog.active,
            Blog.category: blog.category,
            Blog.update_timestamp: datetime.now()
        })
        db.commit()
        return JSONResponse(status_code=200, content={"message": "Blog actualizado exitosamente"})
    # si no existe el blog en la base de datos retorna un mensaje de error
    else:
        return JSONResponse(status_code=404, content={"message": "El blog no existe en la base de datos"})

# funcion para eliminar un blog
def delete_blog_function(db: Session, blog_id: int):
    # si existe el blog en la base de datos lo elimina
    if db.query(Blog).filter(Blog.blog_id == blog_id).first() != None:
        # eliminando el blog
        db.query(Blog).filter(Blog.blog_id == blog_id).delete()
        db.commit()
        return JSONResponse(status_code=200, content={"message": "Blog eliminado exitosamente"})
    # si no existe el blog en la base de datos retorna un mensaje de error
    else:
        return JSONResponse(status_code=404, content={"message": "El blog no existe en la base de datos"})