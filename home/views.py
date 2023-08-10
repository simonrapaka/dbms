from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def loginp(request):
    return render(request, 'home/loginp.html')

def logind(request):
    return render(request,  'home/logind.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('ghms-home')
    else:
        form = UserCreationForm()
    return render(request, 'home/reg.html', {'form' : form})