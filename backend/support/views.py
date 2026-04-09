from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def support(gmail_address):
    print("Created a ticket!")
    print(gmail_address)