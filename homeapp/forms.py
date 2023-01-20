from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re
from django.core.validators import RegexValidator


from homeapp.models import Login, userpage, workerpage,workershedule,admin_addwork,user_appoinment,feedback,payment,admin_payment

class DateInput(forms.DateInput):
    input_type='date'

def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a valid phone number')


class TimeInput(forms.TimeInput):
    input_type='time'


class LoginRegister(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2')

class userform(forms.ModelForm):
    phonenumber=forms.CharField(validators=[phone_number_validator])
    email=forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='please enter valid Email')])

    class Meta:
        model=userpage
        exclude=('user',)

    def clean_email(self):
        mail=self.cleaned_data["email"]
        email_qs_t=userpage.objects.filter(email=mail)
        email_qs_t=workerpage.objects.filter(email=mail)
        if email_qs_t.exists():
            raise forms.ValidationError('This email already registered')
        if email_qs_t.exists():
            raise forms.ValidationError('This email already registered')
        return mail


    def clean_phonenumber(self):
        phnnumber=self.cleaned_data["phonenumber"]
        phnnumber_qs_t=userpage.objects.filter(phonenumber=phnnumber)
        phnnumber_qs_t=workerpage.objects.filter(phonenumber=phnnumber)
        if phnnumber_qs_t.exists():
            raise forms.ValidationError('This phonenumber already registered')
        if phnnumber_qs_t.exists():
            raise forms.ValidationError('This phonenumber already registered')
        return phnnumber


class workerform(forms.ModelForm):
    phonenumber = forms.CharField(validators=[phone_number_validator])
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='please enter valid Email')])
    class Meta:
        model=workerpage
        exclude=('user',)


class workerscheduleform(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    start_time=forms.TimeField(widget=TimeInput,)
    end_time = forms.TimeField(widget=TimeInput,   )
    class Meta:
        model=workershedule
        exclude = ('employee',)


class admin_addworkeform(forms.ModelForm):
    class Meta:
        model=admin_addwork
        fields= ('__all__')

class user_appoinmentform(forms.ModelForm):
    class Meta:
        model=user_appoinment
        fields=('__all__')

class feedbackform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    time = forms.TimeField(widget=TimeInput)
    class Meta:
        model=feedback
        exclude = ('replay','user',)


class paymentform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    time = forms.TimeField(widget=TimeInput)
    class Meta:
        model=payment
        fields = ('__all__')


class admin_paymentform(forms.ModelForm):
    class Meta:
        model = admin_payment
        exclude = ('paid_date','status',)







