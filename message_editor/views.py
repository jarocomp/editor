from django.shortcuts import render
import requests

def index(request):
    return render(request, "message_editor/message_list.html",{})

def download_data(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    user_data = response.json()



    return render(request, 'message_editor/message_list.html', {

    })
