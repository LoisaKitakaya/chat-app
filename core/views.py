from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

# Create your views here.
def home(request):

    return render(request, 'core/index.html')

def signup(request):

    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home')

    else:

        form = SignUpForm()

    context = {
        'form': form
    }

    return render(request, 'core/signup.html', context)

def about(request):

    return render(request, 'core/about.html')