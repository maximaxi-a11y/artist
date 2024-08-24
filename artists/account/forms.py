from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

# class CustomUserCreationForm(UserCreationForm):
    

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', 'group')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         group = self.cleaned_data['group']

#         if commit:
#             user.save()
#             user.groups.add(group)

#         return user

class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'select group'
        }))

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })
    )


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','group')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        group = self.cleaned_data['group']

        if commit:
            user.save()
            user.groups.add(group)

        return user