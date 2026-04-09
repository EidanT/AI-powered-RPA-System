from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def client(gmail_address):
    print("We got a client!")
    print(gmail_address)