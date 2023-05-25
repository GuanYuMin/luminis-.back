import openpay
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

openpay.api_key =os.getenv('OPEN_PAY_PRIVATE_KEY')
openpay.verify_ssl_certs = False
openpay.merchant_id = os.getenv('OPEN_PAY_ID')
openpay.production = False
openpay.country = os.getenv('OPEN_PAY_COUNTRY')

