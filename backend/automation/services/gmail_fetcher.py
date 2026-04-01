import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .ai_classifier import fetch_gmail_data

tasks = []

@csrf_exempt
def webhook(request):
    if request.method == "POST":
        data = json.loads(request.body)
        fetch_gmail_data(data)
        return JsonResponse({"status": "ok"})