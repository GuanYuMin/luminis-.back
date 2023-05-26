# Python
import os
from mangum import Mangum
from dotenv import load_dotenv
from utils.cors_utils import origins

# FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.authentication_router import authentication_router
from routes.user_router import user_router
from routes.role_router import role_router
from routes.video_router import video_router
from routes.membership_router import membership_router
from routes.course_router import course_router
from routes.blog_router import blog_router
from routes.question_blog_router import question_blog_router
from routes.answer_blog_router import answer_blog_router
from routes.photo_router import photo_router
from routes.openpay_router import openpay_router

# Load environment variables
load_dotenv()

stage=os.environ.get('STAGE', None)
openapi_prefix=f"/{stage}" if stage else "/"

# Create an instance of the FastAPI class
app=FastAPI(
    title="project-server-lumnis-backend",
    description="This documentation contains the APIs and details of the same of the Luminis project.",
    version="1.0.0",
    root_path=openapi_prefix
)
# Include cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"]
)

# Include routes and tags
app.include_router(authentication_router, prefix="/auth", tags=["authentication"])
app.include_router(role_router, prefix="/role", tags=["role"])
app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(video_router, prefix="/video", tags=["Video"])
app.include_router(membership_router, prefix="/membership", tags=["Membership"])
app.include_router(course_router, prefix="/course", tags=["Course"])
app.include_router(blog_router, prefix="/blog", tags=["Blog"])
app.include_router(question_blog_router, prefix="/question_blog", tags=["QuestionBlog"])
app.include_router(answer_blog_router, prefix="/answer_blog", tags=["AnswerBlog"])
app.include_router(photo_router, prefix="/photo", tags=["Photo"])
app.include_router(openpay_router, prefix="/openpay", tags=["Openpay"])

@app.get("/")
async def root():
    project="project-server-lumnis-backend"
    description="""Este es un proyecto para la administración de un centro estudiante en el cual se puede realizar las siguientes acciones:
    - Suscribirse a un tipo de suscripción.
    - Agregar cursos a su suscripción.
    - Agregar adicionales a sus suscripciones.
    - Tener perfiles controlados por roles.
    - Tener un historial de transacciones.
    - Tener un historial de pagos.
    - Tener un historial de cursos.
    - etc."""
    authors=["Marco Antonio", "Frank Bill"]
    docs='/docs'
    redoc="/redoc"
    return {
        "project": project,
        "description": description,
        "authors": authors,
        "docs": docs,
        "redoc": redoc
    }

# Create the handler for AWS Lambda
handler=Mangum(app)