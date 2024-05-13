from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm , UserRegisterForm
from django.contrib import messages

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
    return render(request , "app/client_chat.html")

# Error 404
def error_404(request, exception):
    return render(request,'error/404.html')

# Error 500
def error_500(request):
    return render(request,'error/500.html')