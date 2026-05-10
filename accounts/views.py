from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.http import HttpResponse


def home_view(request):

    return render(
        request,
        'home.html'
    )
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request,'accounts/signup.html',{'form': form})


def test_csrf(request):

    if request.method == "POST":

        return HttpResponse("POST SUCCESS")

    return render(
        request,
        "accounts/test.html"
    )
def home_view(request):

    return HttpResponse(
        "AI Job Tracker Home Page"
    )