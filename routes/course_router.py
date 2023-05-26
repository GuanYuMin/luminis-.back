# Python
from sqlalchemy.orm import Session

# FastAPI
from fastapi import APIRouter, Depends
from fastapi import status
from fastapi import Path, Body

from utils.Session_bd import get_db
from schema.course_schema import Course
from functions.course_functions import get_courses_function
from functions.course_functions import get_course_by_id_function
from functions.course_functions import create_course_function
from functions.course_functions import update_course_function
from functions.course_functions import delete_course_function


# course_router = APIRouter(route_class=AccessRouteForTokenMiddleware)
course_router = APIRouter()

# PATH OPERATION TO GET ALL COURSES
# Path Operation Decorator
@course_router.get(
    path="/detail",
    status_code=status.HTTP_200_OK,
    summary="Show courses in the app"
)
# Path Operation Function
def show_courses(
    db: Session = Depends(get_db)
):
    """
    **Show courses**
    
    This path operation shows all courses in the app.
    
    No parameters.
    
    Returns all courses with course_id, membership_id, video_list, name, description, active, content, content_2, index, learning, interactive, product, registration_timestamp and update_timestamp.
    """
    db_course = get_courses_function(db, skip=0, limit=100000)
    return db_course

# PATH OPERATION TO GET COURSE BY ID
# Path Operation Decorator
@course_router.get(
    path="/detail/{course_id}",
    status_code=status.HTTP_200_OK,
    summary="Show course by id in the app"
)
# Path Operation Function
def show_course_by_id(
    db: Session = Depends(get_db),
    course_id: int = Path(
        ...,
        gt=0,
        title="Course Id",
        description="This is the course id.",
        example=2
    )
):
    """
    **Show course by id**
    
    This path operation shows a course by id in the app.
    
    Parameters:
    - Path:
        - **course_id: int** => This is the identifier of the course and is required.
    
    Returns the course with course_id, membership_id, video_list, name, description, active, content, content_2, index, learning, interactive, product, registration_timestamp and update_timestamp.
    """
    db_course = get_course_by_id_function(db, course_id)
    return db_course

# PATH OPERATION TO CREATE COURSE
# Path Operation Decorator
@course_router.post(
    path="/new",
    status_code=status.HTTP_201_CREATED,
    summary="Create course in the app"
)
# Path Operation Function
def create_course(
    db: Session = Depends(get_db),
    course: Course = Body(...)
):
    """
    **Create course**
    
    This path operation creates a course in the app and save the information in the database.
    
    Parameters:
    - Request body parameter:
        - **course: Course** => A course model with membership_id, video_list, name, description, active, content, content_2, index, learning, interactive and product.
    
    Returns a message with confirmation of the change or the detail by which the change was not made.
    """
    db_course = create_course_function(db, course)
    return db_course

# PATH OPERATION TO UPDATE COURSE
# Path Operation Decorator
@course_router.put(
    path="/update/{course_id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update course in the app"
)
# Path Operation Function
def update_course(
    db: Session = Depends(get_db),
    course_id: int = Path(
        ...,
        gt=0,
        title="Course Id",
        description="This is the course id.",
        example=4
    ),
    course: Course = Body(...)
):
    """
    **Update course**
    
    This path operation updates a course by id in the app and save the information in the database.
    
    Parameters:
    - Path:
        - **course_id: int** => This is the identifier of the course and is required.
    - Request body parameter:
        - **course: Course** => A course model with membership_id, video_list, name, description, active, content, content_2, index, learning, interactive and product.
    
    Returns a message with confirmation of the change or the detail by which the change was not made.
    """
    db_course = update_course_function(db, course_id, course)
    return db_course

# PATH OPERATION TO DELETE COURSE
# Path Operation Decorator
@course_router.delete(
    path="/delete/{course_id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Delete course in the app"
)
# Path Operation Function
def delete_course(
    db: Session = Depends(get_db),
    course_id: int = Path(
        ...,
        gt=0,
        title="Course Id",
        description="This is the course id.",
        example=4
    )
):
    """
    **Delete course**
    
    This path operation deletes a course by id in the app.
    
    Parameters:
    - Path:
        - **course_id: int** => This is the identifier of the course and is required.
    
    Returns a message with confirmation of the change or the detail by which the change was not made.
    """
    db_course = delete_course_function(db, course_id)
    return db_course