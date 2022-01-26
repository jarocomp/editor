from django.shortcuts import render, redirect
from django.views import generic
from .models import Message
from .forms import MessageForm
import requests

#pagination
from django.core.paginator import Paginator

def index(request):
    return render(request, "message_editor/message_list.html",{})

def home(request):
    return render(request, "message_editor/home.html",{})

def show_all_messages(request):
    data = Message.objects.all()
    p = Paginator(Message.objects.all(),10)
    page = request.GET.get('page')
    message = p.get_page(page)
    nums = "a" * message.paginator.num_pages
    return render(request,'message_editor/message_list.html', {'data': data,'message':message, 'nums':nums})

def search_message(request):
    if request.method== "POST":
        searched = request.POST['searched']
        messages = Message.objects.filter(title__contains=searched)
        return render(request,'message_editor/search_message.html', {'searched':searched, 'messages': messages})
    else:
        return render(request, 'message_editor/search_message.html', {})

def show_message(request, id):
    message = Message.objects.get(pk = id)
    return render(request, 'message_editor/show_message.html', {'message': message})

def update_message(request, id):
    message = Message.objects.get(pk = id)
    form = MessageForm(request.POST or None, instance = message)
    if form.is_valid():
        form.save()
        return redirect('messages')

    return render(request, 'message_editor/update_message.html', {'message': message, 'form':form})

def delete_message(request,id):
    message = Message.objects.get(pk=id)
    message.delete()
    return  redirect('messages')

def test_data(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    user_data = response.json()

    data = Message(
        id = user_data['id'],
        userId = user_data['userId'],
        title = user_data['title'],
        body = user_data['body']
    )
    data.save()
    return redirect('messages')

def test_users(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    user_data = response.json()
    for i in user_data:
        data = Message(
            id=i['id'],
            userId=i['userId'],
            title=i['title'],
            body=i['body']

    )
        data.save()
    return redirect('messages')


class CreateMessage(generic.edit.CreateView):

    form_class = MessageForm
    template_name = "message_editor/create_message.html"


    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form":form})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return render(request, self.template_name, {"form":form})
