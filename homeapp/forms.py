from django import forms
from django.contrib.auth.forms import UserCreationForm

from homeapp.models import Login, userpage, workerpage,workershedule,admin_addwork,user_appoinment,feedback,payment,admin_payment

class DateInput(forms.DateInput):
    input_type='date'

class TimeInput(forms.TimeInput):
    input_type='time'


class LoginRegister(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2')

class userform(forms.ModelForm):
    class Meta:
        model=userpage
        exclude=('user',)

class workerform(forms.ModelForm):
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







