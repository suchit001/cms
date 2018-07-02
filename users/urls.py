from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from . import views
app_name = 'users'

urlpatterns = [
    url('signup/', views.SignUp.as_view(), name='signup'),
    url('details/', views.list, name='info'),
    path('detailupdate/<int:pk>/', views.DetailUpdateForm.as_view(), name='update'),
    path('detailsview/<int:pk>/', views.DetailViewForm.as_view(), name='detailview'),
    path('documents/<int:pk>/', views.DocumentView.as_view(), name='documents'),
    path('documentsupload/<int:pk>/', views.DocumentUpload.as_view(), name='documentsupload'),

]