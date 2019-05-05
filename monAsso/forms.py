from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#remarques:
#a revoir: changer UserCreation form ambigu

class SignUpAssoForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    nomAsso=forms.CharField(max_length=30)
    typeAsso = forms.CharField(max_length=30)
    description=forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','nomAsso','typeAsso','description', 'password1', 'password2', )

class SignUpBenevoleForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

#formulaire de creation d'un evenement (a finir)
class EventForm(forms.Form):
    nomEvent=forms.CharField(max_length=30)
    lieu=forms.CharField(max_length=30)
    dateDebut=forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))
    dateFin = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))
    description=forms.Textarea()
    nbBenevole=forms.IntegerField()

