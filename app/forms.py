from django import forms
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "select"

class SignUpForm(UserCreationForm):
    username: forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

        def __init__(self, *args, **kwargs):
            super(SignUpForm,self).__init__(*args, **kwargs)

            

    