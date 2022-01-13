from django.shortcuts import render, redirect
from django.views import generic
from .models import Message
from .forms import MessageForm


def index(request):
    return render(request, "message_editor/message_list.html",{})


def show_all_messages(request):
    data = Message.objects.all()
    return render(request,'message_editor/message_list.html', {'data': data} )


def search_message(request):
    if request.method== "POST":
        searched = request.POST['searched']
        messages = Message.objects.filter(title__contains=searched)
        return render(request,'message_editor/search_message.html', {'searched':searched, 'messages': messages} )
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

def delete_message(requet, id):
    message = Message.objects.get(pk=id)
    message.delete()
    return  redirect('messages')



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
