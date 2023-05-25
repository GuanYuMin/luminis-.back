# Python
from sqlalchemy.orm import Session
from datetime import datetime

# FastAPI
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse

from models.video_model import Video
from models.course_model import Course


# FUNCTION TO GET ALL VIDEOS
def get_videos_function(
    db: Session,
    skip: int=0,
    limit: int=100000
):
    if len(db.query(Video).offset(skip).limit(limit).all())==0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No videos found!"
        )
    return db.query(Video).offset(skip).limit(limit).all()

# FUNCTION TO GET VIDEO BY ID
def get_video_by_id_function(
    db: Session,
    video_id: int
):
    if db.query(Video).filter(Video.video_id==video_id).first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No video found with video_id {video_id}."
        )
    return db.query(Video).filter(Video.video_id==video_id).first()

# FUNCTION TO CREATE VIDEO
def create_video_function(
    db: Session,
    video: Video
):
    if db.query(Video).filter(Video.name==video.name).first() is not None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f"Video with name {video.name} already exists!"
        )
    if video.course_id is not None:
        if db.query(Course).filter(Course.course_id==video.course_id).first() is None:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=f"Course with course_id {video.course_id} doesn't exist!"
            )
    db_video=Video(
        course_id=video.course_id,
        name=video.name,
        description=video.description,
        type=video.type,
        cost=video.cost,
        video_url=video.video_url,
        registration_timestamp=datetime.now(),
        update_timestamp=datetime.now()
    )
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return JSONResponse(status_code=200, content={"message": "Video was successfully created."})

# FUNCTION TO UPDATE VIDEO
def update_video_function(
    db: Session,
    video_id: int,
    video: Video
):
    if db.query(Video).filter(Video.video_id==video_id).first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Video with video_id {video_id} doesn't exist!"
        )
    if video.course_id is not None:
        if db.query(Course).filter(Course.course_id==video.course_id).first() is None:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=f"Course with course_id {video.course_id} doesn't exist!"
            )
    if db.query(Video).filter(Video.name==video.name).first() is not None:
        if db.query(Video).filter(Video.name==video.name).first().video_id != video_id:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=f"Video with name {video.name} already exists!"
            )
    db_video=db.query(Video).filter(Video.video_id==video_id).first()
    db_video.course_id=video.course_id
    db_video.name=video.name
    db_video.description=video.description
    db_video.type=video.type
    db_video.cost=video.cost
    db_video.video_url=video.video_url
    db_video.update_timestamp=datetime.now()
    db.commit()
    db.refresh(db_video)
    return JSONResponse(status_code=200, content={"message": "Video was successfully updated."})

# FUNCTION TO DELETE VIDEO
def delete_video_function(
    db: Session,
    video_id: int
):
    if db.query(Video).filter(Video.video_id==video_id).first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Video with video_id {video_id} doesn't exist!"
        )
    db_video=db.query(Video).filter(Video.video_id==video_id).first()
    db.delete(db_video)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Video was successfully deleted."})