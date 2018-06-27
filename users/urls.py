from django.conf.urls import url
from django.views.generic import TemplateView

from . import views
app_name = 'users'

urlpatterns = [
    url('signup/', views.SignUp.as_view(), name='signup'),
    url('details/', views.list, name='detail'),

]