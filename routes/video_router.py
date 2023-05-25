# Python
from sqlalchemy.orm import Session

# FastAPI
from fastapi import APIRouter, Depends
from fastapi import status
from fastapi import Path, Body

from utils.Session_bd import get_db
from schema.video_schema import Video
from functions.video_functions import get_videos_function
from functions.video_functions import get_video_by_id_function
from functions.video_functions import create_video_function
from functions.video_functions import update_video_function
from functions.video_functions import delete_video_function


# video_router = APIRouter(route_class=AccessRouteForTokenMiddleware)
video_router = APIRouter()

# PATH OPERATION TO GET ALL VIDEOS
# Path Operation Decorator
@video_router.get(
    path="/detail",
    status_code=status.HTTP_200_OK,
    summary="Show videos in the app"
)
# Path Operation Function
def show_videos(
    db: Session = Depends(get_db)
):
    """
    **Show videos**
    
    This path operation shows all videos in the app.
    
    No parameters.
    
    Returns all videos with video_id, course_id, name, description, type, cost, video_url, registration_timestamp and update_timestamp.
    """
    db_video = get_videos_function(db, skip=0, limit=100000)
    return db_video

# PATH OPERATION TO GET VIDEO BY ID
# Path Operation Decorator
@video_router.get(
    path="/detail/{video_id}",
    status_code=status.HTTP_200_OK,
    summary="Show video by id in the app"
)
# Path Operation Function
def show_video_by_id(
    db: Session = Depends(get_db),
    video_id: int = Path(
        ...,
        gt=0,
        title="Video Id",
        description="This is the video id.",
        example=2
    )
):
    """
    **Show video by id**
    
    This path operation shows a video by id in the app.
    
    Parameters:
    - Path:
        - **video_id: int** => This is the identifier of the video and is required.
    
    Returns the video with video_id, course_id, name, description, type, cost, video_url, registration_timestamp and update_timestamp.
    """
    db_video = get_video_by_id_function(db, video_id)
    return db_video

# PATH OPERATION TO CREATE VIDEO
# Path Operation Decorator
@video_router.post(
    path="/new",
    status_code=status.HTTP_201_CREATED,
    summary="Create video in the app"
)
# Path Operation Function
def create_video(
    db: Session = Depends(get_db),
    video: Video = Body(...)
):
    """
    **Create video**
    
    This path operation creates a video in the app and save the information in the database.
    
    Parameters:
    - Request body parameter:
        - **video: Video** => A video model with course_id, name, description, type, cost and video_url.
    
    Returns a message with confirmation of the change or the detail by which the change was not made.
    """
    db_video = create_video_function(db, video)
    return db_video

# PATH OPERATION TO UPDATE VIDEO
# Path Operation Decorator
@video_router.put(
    path="/update/{video_id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update video in the app"
)
# Path Operation Function
def update_video(
    db: Session = Depends(get_db),
    video_id: int = Path(
        ...,
        gt=0,
        title="Video Id",
        description="This is the video id.",
        example=4
    ),
    video: Video = Body(...)
):
    """
    **Update video**
    
    This path operation updates a video by id in the app and save the information in the database.
    
    Parameters:
    - Path:
        - **video_id: int** => This is the identifier of the video and is required.
    - Request body parameter:
        - **video: Video** => A video model with course_id, name, description, type, cost and video_url.
    
    Returns a message with confirmation of the change or the detail by which the change was not made.
    """
    db_video = update_video_function(db, video_id, video)
    return db_video

# PATH OPERATION TO DELETE VIDEO
# Path Operation Decorator
@video_router.delete(
    path="/delete/{video_id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Delete video in the app"
)
# Path Operation Function
def delete_video(
    db: Session = Depends(get_db),
    video_id: int = Path(
        ...,
        gt=0,
        title="Video Id",
        description="This is the video id.",
        example=4
    )
):
    """
    **Delete video**
    
    This path operation deletes a video by id in the app.
    
    Parameters:
    - Path:
        - **video_id: int** => This is the identifier of the video and is required.
    
    Returns a message with confirmation of the change or the detail by which the change was not made.
    """
    db_video = delete_video_function(db, video_id)
    return db_video