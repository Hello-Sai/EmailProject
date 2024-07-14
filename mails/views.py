from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import os
from django.http import HttpResponse
from django.conf import settings
from mails.utils import mail_service
@csrf_exempt
def send_email(request):
    email = 'tech@themedius.ai'
    screenshot = os.path.join(settings.BASE_DIR,'Screenshot.jpeg')
    zipfile = os.path.join(settings.BASE_DIR,'emailproject.zip')
    screenshot = screenshot.replace('\'','/')
    repository_link = "https://github.com/Hello-Sai/EmailProject"
    mail_service(email=email,screenshot=screenshot,repository_link=repository_link,zipfile=zipfile)
    return HttpResponse("<h1> Mail Sent Successfully </h1>")
