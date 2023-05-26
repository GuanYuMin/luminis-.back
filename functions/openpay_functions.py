# importando el packete datetime para poder usarlo en el modelo de usuario
from datetime import datetime

from fastapi.responses import JSONResponse
from sqlalchemy import update
from sqlalchemy.orm import Session

#importano el cliente de openpay
from utils.openpay_config import openpay


# funcion para crear un cliente de openpay
def create_customer_openpay(name, last_name, email, phone_number):
    try:
        customer = openpay.Customer.create(
            name=name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            requires_account=False
        )
        return customer
    except Exception as e:
        print(e)
        return False


# funcion para crear un token de openpay
def create_token_openpay(customer_id, card_number, holder_name, expiration_year, expiration_month, cvv2):
    try:
        token = openpay.Token.create(
            card_number=card_number,
            holder_name=holder_name,
            expiration_year=expiration_year,
            expiration_month=expiration_month,
            cvv2=cvv2,
            customer_id=customer_id
        )
        return token
    except Exception as e:
        print(e)
        return False

##Customer de prueba id = adygku9kfq74nq8ojqyg
##token de prueba id = khu4bq5brpyere1jq1cv
##id de tarjeta de prueba = khu4bq5brpyere1jq1cv
##Plan ID =p5iyxa5rfbh9mqrhm4a3

# funcion para crear una tarjeta de openpay
def create_card_openpay(customer_id, token_id, device_session_id):
    try:
        card = openpay.Card.create(
            token_id=token_id,
            customer_id=customer_id,
            device_session_id=device_session_id
        )
        return card
    except Exception as e:
        print(e)
        return False
    

# obtener el cliente de openpay
def get_customer_openpay(customer_id):
    try:
        customer = openpay.Customer.retrieve(customer_id)
        return customer
    except Exception as e:
        print(e)
        return False
    
# funcion para actualizar el cliente de openpay
def update_customer_openpay(customer_id, name, last_name, email, phone_number):
    try:
        customer = openpay.Customer.retrieve(customer_id)
        customer.name = name
        customer.last_name = last_name
        customer.email = email
        customer.phone_number = phone_number
        customer.save()
        return customer
    except Exception as e:
        print(e)
        return False

# funcion para obtener todos los clientes de openpay
def get_all_customers_openpay():
    try:
        customers = openpay.Customer.all()
        return customers
    except Exception as e:
        print(e)
        return False
    
# funcion para obtener todas las tarjetas 
def get_all_cards_openpay():
    try:
        cards = openpay.Card.all()
        return cards
    except Exception as e:
        print(e)
        return False
    
# funcion para obtener una tarjeta de openpay
def get_card_openpay(card_id):
    try:
        card = openpay.Card.retrieve(card_id)
        return card
    except Exception as e:
        print(e)
        return False
    
# funcion para eliminar una tarjeta de openpay
def delete_card_openpay(card_id):
    try:
        card = openpay.Card.retrieve(card_id)
        card.delete()
        return True
    except Exception as e:
        print(e)
        return False
    
# Get all customer transfers (inbound and outbound)
def get_all_transfers_openpay(customer_id):
    try:
        transfers = openpay.Transfer.all(customer_id)
        return transfers
    except Exception as e:
        print(e)
        return False

#Create a customer transfer
def create_transfer_openpay(customer_id, amount, description, order_id):
    try:
        transfer = openpay.Transfer.create(
            customer_id=customer_id,
            amount=amount,
            description=description,
            order_id=order_id
        )
        return transfer
    except Exception as e:
        print(e)
        return False

#Get specific transfer
def get_transfer_openpay(customer_id, transfer_id):
    try:
        transfer = openpay.Transfer.retrieve(customer_id, transfer_id)
        return transfer
    except Exception as e:
        print(e)
        return False
    
#Add bank account to customer
def add_bank_account_openpay(customer_id, holder_name, alias, clabe):
    try:
        bank_account = openpay.BankAccount.create(
            customer_id=customer_id,
            holder_name=holder_name,
            alias=alias,
            clabe=clabe
        )
        return bank_account
    except Exception as e:
        print(e)
        return False
    
#Get all customer bank accounts
def get_all_bank_accounts_openpay(customer_id):
    try:
        bank_accounts = openpay.BankAccount.all(customer_id)
        return bank_accounts
    except Exception as e:
        print(e)
        return False

#Get specific bank account
def get_bank_account_openpay(customer_id, bank_account_id):
    try:
        bank_account = openpay.BankAccount.retrieve(customer_id, bank_account_id)
        return bank_account
    except Exception as e:
        print(e)
        return False
    
##SUSCRIPCIONES

#Add subscription to customer
##error que me sale type object 'Subscription' has no attribute 'create'
##Customer de prueba id = adygku9kfq74nq8ojqyg
##token de prueba id = kmenrzks2hu6gtykvqg4
##id de tarjeta de prueba = kmenrzks2hu6gtykvqg4
##Plan ID =p5iyxa5rfbh9mqrhm4a3

def add_subscription_openpay(customer_id, plan_id, card_id, trial_days):
    try:
        customer = openpay.Customer.retrieve(customer_id)
        subscription = customer.subscriptions.create(
            plan_id=plan_id,
            trial_days=trial_days,
            card_id=card_id
        )
        return subscription
    except Exception as e:
        print(e)
        return False
    
#Cancel subscription
def cancel_subscription_openpay(customer_id, subscription_id):
    try:
        subscription = openpay.Subscription.retrieve(customer_id, subscription_id)
        subscription.cancel()
        return True
    except Exception as e:
        print(e)
        return False

#List all customers subscriptions
def get_all_subscriptions_openpay(customer_id):
    try:
        subscriptions = openpay.Subscription.all(customer_id)
        return subscriptions
    except Exception as e:
        print(e)
        return False

#Update subscription
def update_subscription_openpay(customer_id, subscription_id, card_id):
    try:
        subscription = openpay.Subscription.retrieve(customer_id, subscription_id)
        subscription.card_id = card_id
        subscription.save()
        return subscription
    except Exception as e:
        print(e)
        return False

#Add payout for customer
def add_payout_openpay(customer_id, method, amount, description, order_id):
    try:
        payout = openpay.Payout.create(
            customer_id=customer_id,
            method=method,
            amount=amount,
            description=description,
            order_id=order_id
        )
        return payout
    except Exception as e:
        print(e)
        return False
    
#Get all payouts for customer
def get_all_payouts_openpay(customer_id):
    try:
        payouts = openpay.Payout.all(customer_id)
        return payouts
    except Exception as e:
        print(e)
        return False

##CREACION DE PLANES

#Create new plan
def create_plan_openpay(amount,status_after_retry, retry_times, name, repeat_unit,trial_days, repeat_every):
    try:
        plan = openpay.Plan.create(
            amount=amount,
            status_after_retry=status_after_retry,
            retry_times=retry_times,
            name=name,
            repeat_unit=repeat_unit,
            trial_days=trial_days,
            repeat_every=repeat_every
        )
        return plan
    except Exception as e:
        print(e)
        return False
#List all plans
def get_all_plans_openpay():
    try:
        plans = openpay.Plan.all()
        return plans
    except Exception as e:
        print(e)
        return False
    
#Get specific plan
def get_plan_openpay(plan_id):
    try:
        plan = openpay.Plan.retrieve(plan_id)
        return plan
    except Exception as e:
        print(e)
        return False

#Update a plan
def update_plan_openpay(plan_id, name, status_after_retry, retry_times, repeat_unit, trial_days, repeat_every, amount):
    try:
        plan = openpay.Plan.retrieve(plan_id)
        plan.name = name
        plan.status_after_retry = status_after_retry
        plan.retry_times = retry_times
        plan.repeat_unit = repeat_unit
        plan.trial_days = trial_days
        plan.repeat_every = repeat_every
        plan.amount = amount
        plan.save()
        return plan
    except Exception as e:
        print(e)
        return False

#Delete a plan
def delete_plan_openpay(plan_id):
    try:
        plan = openpay.Plan.retrieve(plan_id)
        plan.delete()
        return True
    except Exception as e:
        print(e)
        return False