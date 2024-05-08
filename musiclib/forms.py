from django import forms
from django.contrib.auth.forms import AuthenticationForm
from pip._internal.utils._jaraco_text import _

from musiclib.models import CustomUser, MusicFiles
from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm

class MyAuthForm(AuthenticationForm):
    # Сейчас из темплейта сообщения
    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = CustomUser
        fields = ( 'email', 'password1', 'password2',)
                  
class MusicFilesForm(forms.ModelForm):
    class Meta:
        model = MusicFiles
        fields = ['title', 'file', 'customuser']

class MusicFilesFilterForm(forms.Form):
    min_id = forms.IntegerField(label='От', required=False)
    max_id = forms.IntegerField(label='До', required=False)
    title_for_search = forms.CharField(label='Название трека', required=False)
  