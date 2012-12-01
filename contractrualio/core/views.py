from core.utils import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def home(request, template='home.html'):
    context = {
        'login_form': AuthenticationForm(), 
        'register_form': UserCreationForm(), 
    }
    return render(request, template, context)

def contact(request, template='contact.html'):
    context = {}
    return render(request, template, context)
