import base64
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
"""
@csrf_exempt
def webhook(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        return JsonResponse({"status": "ok"})"""