from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .forms import  UserRegisterForm
from django.contrib import messages
from .models import Conversation, Message
from .serene import Serene
from django.http import JsonResponse
from django.core import serializers

# instantiate the chatbot
chatbot = Serene()

# Create your views here.
def client_index(request):
    return render(request, "index.html")

# Create your views here.
def client_signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} successfully!')
            return redirect('client-login')
        else :
            print(form.errors)
            messages.error(request, f'Account not created! Please try again.')
            return redirect('client-signup')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/client_signup.html', {'form': form})

@login_required
def client_chat(request):
    if request.method == 'POST':
        Conversation.objects.create(
            user=request.user ,
            name = request.POST.get('name')
            )
        return redirect('client-chat')
    conversations = Conversation.objects.filter(user=request.user)
    return render(request , "app/client_chat.html", {'conversations': conversations})

# Chat view
def client_send_message(request):
    conversation = Conversation.objects.get(id=request.POST.get('conversation_id'))
    Message.objects.create(
        content = request.POST.get('content'),
        conversation = conversation
    )
    predict = chatbot.make_prediction(request.POST.get('content'))
    message = Message.objects.create(
        content = predict,
        conversation = conversation
    )
    data = serializers.serialize('json', [message,])
    return JsonResponse(data, safe=False)

def client_get_message(request):
    conversation_id = request.GET.get('conversation_id')
    conversation = Conversation.objects.get(id=conversation_id)
    messages = Message.objects.filter(conversation=conversation)
    data = serializers.serialize('json', messages)
    return JsonResponse(data, safe=False)

def client_delete_conversation(request ,pk):
    conversation = Conversation.objects.get(id=pk)
    conversation.delete()
    return redirect('client-chat')

# Error 404
def error_404(request, exception):
    return render(request,'error/404.html')

# Error 500
def error_500(request):
    return render(request,'error/500.html')