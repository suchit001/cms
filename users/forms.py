from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms, SelectDateWidget
from django import forms
from .models import CustomUser, Documents


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'sq', 'sa', 'bd','profpic')
        widgets = {
            'bd': DatePickerInput(),  # default date-format %m/%d/%Y will be used
        }





class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class PersonalDetailForm(UserChangeForm):
    class Meta:
         model = CustomUser
         fields = ('username', 'email', 'gender', 'sq', 'sa', 'bd', 'fname', 'lname', 'phoneno','address','profpic')
         widgets = {
                   'bd': DatePickerInput(),  # default date-format %m/%d/%Y will be used
                }
class DocumentListForm(forms.ModelForm):
    class Meta:
         model = Documents
         fields = ('resume', 'birth_certificate', 'marksheet',)
