import os
from dotenv import load_dotenv
from datetime import datetime
import base64
import requests

# Load environment variables from .env file
load_dotenv()

def generate_access_token():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")

    # Sandbox environment URL
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    try:
        # Encode credentials
        encoded_credentials = base64.b64encode(f"{consumer_key}:{consumer_secret}".encode()).decode()

        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/json"
        }

        # Send the request and parse the response
        response = requests.get(url, headers=headers).json()
        print("Response:", response)  # Log the entire response

        # Check for access token in the response
        if "access_token" in response:
            return response["access_token"]
        else:
            raise Exception("Failed to get access token: " + response.get("error_description", "No description"))
    except Exception as e:
        raise Exception("Failed to get access token: " + str(e))




def send_stk_push():
    token = generate_access_token()
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    short_code = os.getenv("SHORT_CODE")  
    passkey = os.getenv("PASSKEY")

    # Encode the password
    stk_password = base64.b64encode((short_code + passkey + timestamp).encode('utf-8')).decode('utf-8')
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    request_body = {
        "BusinessShortCode": short_code,
        "Password": stk_password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": "254114511133", 
        "PartyB": short_code,
        "PhoneNumber": "254114511133",  
        "CallBackURL": "https://yourwebsite.co.ke/callbackurl",
        "AccountReference": "account",
        "TransactionDesc": "test"
    }

    try:
        response = requests.post(url, json=request_body, headers=headers)
        print(response.json())
        return response.json()
    except Exception as e:
        print('Error:', str(e))

