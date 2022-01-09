from django.shortcuts import render, redirect, render_to_response
from django.views import generic
from .models import Message
from .forms import MessageForm


def index(request):
    return render(request, "message_editor/message_list.html",{})


def show_data(request):
    data = Message.objects.all()
    return render(request,'message_editor/message_list.html', {'data': data} )


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
