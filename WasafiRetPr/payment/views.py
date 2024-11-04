# views.py
from django.shortcuts import render
from .mpesa_utils import send_stk_push
from django.http import JsonResponse

def initiate_stk_push(request):
    # Call the function to send STK Push
    response = send_stk_push()
    
    # Handle response
    if response:
        return JsonResponse(response)
    else:
        return JsonResponse({"error": "Failed to initiate STK Push"})
