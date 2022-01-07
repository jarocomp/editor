from django.shortcuts import render
import requests
from .models import Message

def index(request):
    return render(request, "message_editor/message_list.html",{})


def show_data(request):
    data = Message.objects.all()
    return render(request,'message_editor/message_list.html', {'data': data} )
