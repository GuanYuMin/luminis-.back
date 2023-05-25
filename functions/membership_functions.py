# Python
from sqlalchemy.orm import Session
from datetime import datetime

# FastAPI
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse

from models.membership_model import Membership
from models.course_model import Course


# FUNCTION TO GET ALL MEMBERSHIP
def get_memberships_function(
    db: Session,
    skip: int=0,
    limit: int=100000
):
    if len(db.query(Membership).offset(skip).limit(limit).all())==0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No memberships found!"
        )
    return db.query(Membership).offset(skip).limit(limit).all()

# FUNCTION TO GET MEMBERSHIP BY ID
def get_membership_by_id_function(
    db: Session,
    membership_id: int
):
    if db.query(Membership).filter(Membership.membership_id==membership_id).first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No membership found with membership_id {membership_id}."
        )
    return db.query(Membership).filter(Membership.membership_id==membership_id).first()

# FUNCTION TO CREATE MEMBERSHIP
def create_membership_function(
    db: Session,
    membership: Membership
):
    if db.query(Membership).filter(Membership.name==membership.name).first() is not None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f"Membership with name {membership.name} already exists!"
        )
    db_membership=Membership(
        course_list=membership.course_list,
        name=membership.name,
        description=membership.description,
        active=membership.active,
        cost=membership.cost,
        duration=membership.duration,
        to=membership.to,
        membership_url=membership.membership_url,
        registration_timestamp=datetime.now(),
        update_timestamp=datetime.now()
    )
    db.add(db_membership)
    db.commit()
    db.refresh(db_membership)
    return JSONResponse(status_code=200, content={"message": "Membership was successfully created."})

# FUNCTION TO UPDATE MEMBERSHIP
def update_membership_function(
    db: Session,
    membership_id: int,
    membership: Membership
):
    if db.query(Membership).filter(Membership.membership_id==membership_id).first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Membership with membership_id {membership_id} doesn't exist!"
        )
    if db.query(Membership).filter(Membership.name==membership.name).first() is not None:
        if db.query(Membership).filter(Membership.name==membership.name).first().membership_id != membership_id:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=f"Membership with name {membership.name} already exists!"
            )
    db_membership=db.query(Membership).filter(Membership.membership_id==membership_id).first()
    db_membership.course_list=membership.course_list
    db_membership.name=membership.name
    db_membership.description=membership.description
    db_membership.active=membership.active
    db_membership.cost=membership.cost
    db_membership.duration=membership.duration
    db_membership.to=membership.to
    db_membership.membership_url=membership.membership_url
    db_membership.update_timestamp=datetime.now()
    db.commit()
    db.refresh(db_membership)
    return JSONResponse(status_code=200, content={"message": "Membership was successfully updated."})

# FUNCTION TO DELETE MEMBERSHIP
def delete_membership_function(
    db: Session,
    membership_id: int
):
    if db.query(Membership).filter(Membership.membership_id==membership_id).first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Membership with membership_id {membership_id} doesn't exist!"
        )
    if db.query(Course).filter(Course.membership_id==membership_id).first() is not None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f"Can't delete membership with membership_id {membership_id}."
        )
    db_membership=db.query(Membership).filter(Membership.membership_id==membership_id).first()
    db.delete(db_membership)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Membership was successfully deleted."})