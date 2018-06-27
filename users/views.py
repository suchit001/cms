from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
from .models import CustomUser

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def disp(request):
    return render(request, 'about.html')

def list(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'contact.html', context=context)