# coding: utf-8

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..commons.django_views_utils import ajax_login_required
from .service import email_svc
from time import sleep
from adapters import aiassistant




@csrf_exempt
@ajax_login_required
def add_emai(request):
    body = json.loads(request.body)
    new_emai = email_svc.add_emai(body.get("description"))

    return JsonResponse(new_emai)

@ajax_login_required
def list_email(request):
    email = email_svc.list_email()
    return JsonResponse({"email": email})

@ajax_login_required
def chat(request):
    body = json.loads(request.body)
    print(body)
    jsonresponse = aiassistant.sendMessage(body["message"])
    return JsonResponse(jsonresponse)
