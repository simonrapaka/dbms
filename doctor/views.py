from django.shortcuts import render, redirect

# Create your views here.
def doc(request):
    return render(request, 'doctor/land.html')

def pat(request):
    return render(request, 'doctor/pt.html')