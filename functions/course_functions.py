# Python
from sqlalchemy.orm import Session
from datetime import datetime

# FastAPI
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse

from models.course_model import Course
from models.video_model import Video
from models.membership_model import Membership


# FUNCTION TO GET ALL COURSES
def get_courses_function(
    db: Session,
    skip: int=0,
    limit: int=100000
):
    if len(db.query(Course).offset(skip).limit(limit).all())==0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No courses found!"
        )
    return db.query(Course).offset(skip).limit(limit).all()

# FUNCTION TO GET COURSE BY ID
def get_course_by_id_function(
    db: Session,
    course_id: int
):
    if db.query(Course).filter(Course.course_id==course_id).first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No course found with course_id {course_id}."
        )
    return db.query(Course).filter(Course.course_id==course_id).first()

# FUNCTION TO CREATE COURSE
def create_course_function(
    db: Session,
    course: Course
):
    if db.query(Course).filter(Course.name==course.name).first() is not None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f"Course with name {course.name} already exists!"
        )
    if course.membership_id is not None:
        if db.query(Membership).filter(Membership.membership_id==course.membership_id).first() is None:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=f"Membership with membership_id {course.membership_id} doesn't exist!"
            )
    db_course=Course(
        membership_id=course.membership_id,
        video_list=course.video_list,
        name=course.name,
        description=course.description,
        active=course.active,
        content=course.content,
        content_2=course.content_2,
        product=course.product,
        registration_timestamp=datetime.now(),
        update_timestamp=datetime.now()
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return JSONResponse(status_code=200, content={"message": "Course was successfully created."})

# FUNCTION TO UPDATE COURSE
def update_course_function(
    db: Session,
    course_id: int,
    course: Course
):
    if db.query(Course).filter(Course.course_id==course_id).first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with course_id {course_id} doesn't exist!"
        )
    if course.membership_id is not None:
        if db.query(Membership).filter(Membership.membership_id==course.membership_id).first() is None:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=f"Membership with membership_id {course.membership_id} doesn't exist!"
            )
    if db.query(Course).filter(Course.name==course.name).first() is not None:
        if db.query(Course).filter(Course.name==course.name).first().course_id != course_id:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=f"Course with name {course.name} already exists!"
            )
    db_course=db.query(Course).filter(Course.course_id==course_id).first()
    db_course.membership_id=course.membership_id
    db_course.video_list=course.video_list
    db_course.name=course.name
    db_course.description=course.description
    db_course.active=course.active
    db_course.content=course.content
    db_course.content_2=course.content_2
    db_course.product=course.product
    db_course.update_timestamp=datetime.now()
    db.commit()
    db.refresh(db_course)
    return JSONResponse(status_code=200, content={"message": "Course was successfully updated."})

# FUNCTION TO DELETE COURSE
def delete_course_function(
    db: Session,
    course_id: int
):
    if db.query(Course).filter(Course.course_id==course_id).first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with course_id {course_id} doesn't exist!"
        )
    if db.query(Video).filter(Video.course_id==course_id).first() is not None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f"Can't delete course with course_id {course_id}."
        )
    db_course=db.query(Course).filter(Course.course_id==course_id).first()
    db.delete(db_course)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Course was successfully deleted."})