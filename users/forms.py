from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms, SelectDateWidget

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'sq', 'sa','bd')
        widgets = {
            'bd': DatePickerInput(),  # default date-format %m/%d/%Y will be used
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields