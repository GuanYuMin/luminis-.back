# Python
from sqlalchemy.orm import Session

# FastAPI
from fastapi import APIRouter, Depends
from fastapi import status
from fastapi import Path, Body

from utils.Session_bd import get_db
from schema.membership_schema import Membership
from functions.membership_functions import get_memberships_function
from functions.membership_functions import get_membership_by_id_function
from functions.membership_functions import create_membership_function
from functions.membership_functions import update_membership_function
from functions.membership_functions import delete_membership_function


# video_router = APIRouter(route_class=AccessRouteForTokenMiddleware)
membership_router = APIRouter()

# PATH OPERATION TO GET ALL MEMBERSHIPS
# Path Operation Decorator
@membership_router.get(
    path="/detail",
    status_code=status.HTTP_200_OK,
    summary="Show memberships in the app"
)
# Path Operation Function
def show_memberships(
    db: Session = Depends(get_db)
):
    """
    **Show memberships**
    
    This path operation shows all memberships in the app.
    
    No parameters.
    
    Returns all memberships with membership_id, course_list, name, description, active, cost, duration, to, membership_url, registration_timestamp and update_timestamp.
    """
    db_membership = get_memberships_function(db, skip=0, limit=100000)
    return db_membership

# PATH OPERATION TO GET MEMBERSHIP BY ID
# Path Operation Decorator
@membership_router.get(
    path="/detail/{membership_id}",
    status_code=status.HTTP_200_OK,
    summary="Show membership by id in the app"
)
# Path Operation Function
def show_membership_by_id(
    db: Session = Depends(get_db),
    membership_id: int = Path(
        ...,
        gt=0,
        title="Membership Id",
        description="This is the membership id.",
        example=2
    )
):
    """
    **Show membership by id**
    
    This path operation shows a membership by id in the app.
    
    Parameters:
    - Path:
        - **membership_id: int** => This is the identifier of the membership and is required.
    
    Returns the membership with membership_id, course_list, name, description, active, cost, duration, to, membership_url, registration_timestamp and update_timestamp.
    """
    db_membership = get_membership_by_id_function(db, membership_id)
    return db_membership

# PATH OPERATION TO CREATE MEMBERSHIP
# Path Operation Decorator
@membership_router.post(
    path="/new",
    status_code=status.HTTP_201_CREATED,
    summary="Create membership in the app"
)
# Path Operation Function
def create_membership(
    db: Session = Depends(get_db),
    membership: Membership = Body(...)
):
    """
    **Create membership**
    
    This path operation creates a membership in the app and save the information in the database.
    
    Parameters:
    - Request body parameter:
        - **membership: Membership** => A membership model with course_list, name, description, active, cost, duration, to and membership_url.
    
    Returns a message with confirmation of the change or the detail by which the change was not made.
    """
    db_membership = create_membership_function(db, membership)
    return db_membership

# PATH OPERATION TO UPDATE MEMBERSHIP
# Path Operation Decorator
@membership_router.put(
    path="/update/{membership_id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update membership in the app"
)
# Path Operation Function
def update_membership(
    db: Session = Depends(get_db),
    membership_id: int = Path(
        ...,
        gt=0,
        title="Membership Id",
        description="This is the membership id.",
        example=4
    ),
    membership: Membership = Body(...)
):
    """
    **Update membership**
    
    This path operation updates a membership by id in the app and save the information in the database.
    
    Parameters:
    - Path:
        - **membership_id: int** => This is the identifier of the membership and is required.
    - Request body parameter:
        - **membership: Membership** =>  A membership model with course_list, name, description, active, cost, duration, to and membership_url.
    
    Returns a message with confirmation of the change or the detail by which the change was not made.
    """
    db_membership = update_membership_function(db, membership_id, membership)
    return db_membership

# PATH OPERATION TO DELETE MEMBERSHIP
# Path Operation Decorator
@membership_router.delete(
    path="/delete/{membership_id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Delete membership in the app"
)
# Path Operation Function
def delete_membership(
    db: Session = Depends(get_db),
    membership_id: int = Path(
        ...,
        gt=0,
        title="Membership Id",
        description="This is the membership id.",
        example=4
    )
):
    """
    **Delete membership**
    
    This path operation deletes a membership by id in the app.
    
    Parameters:
    - Path:
        - **membership_id: int** => This is the identifier of the membership and is required.
    
    Returns a message with confirmation of the change or the detail by which the change was not made.
    """
    db_membership = delete_membership_function(db, membership_id)
    return db_membership