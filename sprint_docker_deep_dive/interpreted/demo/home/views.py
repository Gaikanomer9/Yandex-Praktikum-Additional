from django.http import HttpResponse
import os


def index(request):
    return HttpResponse(f'You are in {os.environ.get("ENV")} environment')
