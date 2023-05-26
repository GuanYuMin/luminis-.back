from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse
#importaremos la session de la base de datos
from sqlalchemy.orm import Session

#importando las funciones de auser  
from functions.openpay_functions import (create_card_openpay,
                                         create_customer_openpay,
                                         create_token_openpay,
                                         get_all_cards_openpay,
                                         get_all_customers_openpay,
                                         update_customer_openpay,
                                         get_card_openpay,
                                         delete_card_openpay,
                                         create_plan_openpay,
                                         get_plan_openpay,
                                         update_plan_openpay,
                                         delete_plan_openpay,
                                         get_all_plans_openpay,
                                         add_subscription_openpay)
#importando la sessionde base de datos
from utils.Session_bd import get_db

#router para los openpay logeados
#role_router = APIRouter(route_class=AccessRouteForTokenMiddleware)
#router para los openpay no logeados
openpay_router = APIRouter()

##GETS
#obtener todos los clientes de openpay
@openpay_router.get("/openpay/customers/")
def get_all_customers(db: Session = Depends(get_db)):
    customers = get_all_customers_openpay()
    if customers:
        return customers
    else:
        return JSONResponse(status_code=400, content={"message": "Error al obtener los clientes de openpay"})

#obtener todas las tarjetas de openpay
@openpay_router.get("/openpay/cards/")
def get_all_cards(db: Session = Depends(get_db)):
    cards = get_all_cards_openpay()
    if cards:
        return cards
    else:
        return JSONResponse(status_code=400, content={"message": "Error al obtener las tarjetas de openpay"})

#obtener todos los planes de openpay
@openpay_router.get("/openpay/plans/")
def get_all_plans(db: Session = Depends(get_db)):
    plans = get_all_plans_openpay()
    if plans:
        return plans
    else:
        return JSONResponse(status_code=400, content={"message": "Error al obtener los planes de openpay"})

##POSTS
#crear un cliente de openpay
@openpay_router.post("/openpay/customer/")
def create_customer(name: str, last_name: str, email: str, phone_number: str, db: Session = Depends(get_db)):
    customer = create_customer_openpay(name=name, last_name=last_name, email=email, phone_number=phone_number)
    if customer:
        return customer
    else:
        return JSONResponse(status_code=400, content={"message": "Error al crear el cliente de openpay"})


#crear un token de openpay
@openpay_router.post("/openpay/token/")
def create_token(customer_id: str, card_number: str, holder_name: str, expiration_year: str, expiration_month: str, cvv2: str, db: Session = Depends(get_db)):
    token = create_token_openpay(customer_id=customer_id, card_number=card_number, holder_name=holder_name, expiration_year=expiration_year, expiration_month=expiration_month, cvv2=cvv2)
    if token:
        return token
    else:
        return JSONResponse(status_code=400, content={"message": "Error al crear el token de openpay"})

#crear una tarjeta de openpay asociada a un cliente
@openpay_router.post("/openpay/card/")
def create_card(customer_id: str, token_id: str, device_session_id: str, db: Session = Depends(get_db)):
    card = create_card_openpay(customer_id=customer_id, token_id=token_id, device_session_id=device_session_id)
    if card:
        return card
    else:
        return JSONResponse(status_code=400, content={"message": "Error al crear la tarjeta de openpay"})



#crear un plan de openpay
@openpay_router.post("/openpay/plan/")
def create_plan(name: str,status_after_retry: str, retry_times: str,  repeat_unit: str, trial_days:str,repeat_every: str, amount: str,db: Session = Depends(get_db)):
    plan = create_plan_openpay(name=name, status_after_retry=status_after_retry, retry_times=retry_times, repeat_unit=repeat_unit, trial_days=trial_days, repeat_every=repeat_every, amount=amount)
    if plan:
        return plan
    else:
        return JSONResponse(status_code=400, content={"message": "Error al crear el plan de openpay"})
    
# Crear una suscripción de openpay
@openpay_router.post("/openpay/subscription/")
def create_subscription(customer_id: str, plan_id: str, card_id: str, trial_days: str, db: Session = Depends(get_db)):
    subscription = add_subscription_openpay(customer_id=customer_id, plan_id=plan_id, card_id=card_id, trial_days=trial_days)
    if subscription:
        return subscription
    else:
        return JSONResponse(status_code=400, content={"message": "Error al crear la suscripción de openpay"})