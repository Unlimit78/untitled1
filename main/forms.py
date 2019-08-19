from django import forms
from .models import  AdvUser,user_registrated,Photos
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

class ChangeUsersInfo(forms.ModelForm):
    email = forms.EmailField(required=True,label='E-mail')
    class Meta:
        model = AdvUser
        fields = ('model_pic','username','email','first_name','last_name','date_of_birth','about','Hobbys','send_messages',)

class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True,label='E-mail')
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput,help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Password again',widget=forms.PasswordInput,help_text='Enter password agein')
    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1!=password2:
            errors = {'password2':ValidationError('Password dont match...',code='password_mismatch')}
            raise ValidationError(errors)

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()
        user_registrated.send(RegisterUserForm,instance=user)
        return user

    class Meta:
        model=AdvUser
        fields = ('username','email','password1','password2','first_name','last_name','send_messages')

class PhotoForm(forms.ModelForm):
    photos = forms.ImageField (label='' ,widget=forms.FileInput(attrs={'multiple': 'multiple'}))
    class Meta:
        model = Photos
        fields=[]