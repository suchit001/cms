from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView, CreateView, DetailView, ListView

from .forms import CustomUserCreationForm,PersonalDetailForm,DocumentListForm
from .models import CustomUser, Documents

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

class DetailUpdateForm(UpdateView):
    model = CustomUser
    template_name = 'users/custumuser_form.html'
    fields = ('username', 'email', 'gender', 'bd', 'fname', 'lname', 'phoneno','profpic','address')
    success_url = reverse_lazy('home')

class DetailViewForm(UpdateView):
    model = CustomUser
    #form_class = PersonalDetailForm
    template_name = 'users/detailview.html'
    fields = ('username', 'email', 'gender','bd', 'fname', 'lname', 'phoneno','profpic','address')

class DocumentView(UpdateView):
    model = Documents
    template_name = 'users/documents.html'
    #form_class = DocumentListForm
    fields = ('resume','birth_certificate', 'marksheet')




class DocumentUpload(UpdateView):
    model = Documents
    template_name = 'users/documentsupload.html'
    form_class = DocumentListForm
    success_url = reverse_lazy('home')


