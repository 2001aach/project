from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_user=models.BooleanField(default=False)
    is_worker=models.BooleanField(default=False)

class userpage(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='user')
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    housenumber=models.IntegerField()
    phonenumber=models.IntegerField()
    email=models.EmailField()
    photo=models.ImageField(upload_to='photo')

    def __str__(self):
        return self.name

class admin_addwork(models.Model):
    workname=models.CharField(max_length=30)
    discription=models.CharField(max_length=300)
    charge=models.IntegerField()

    def __str__(self):
       return self.workname


class workerpage(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='worker')
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    phonenumber = models.IntegerField()
    email = models.EmailField()
    photo = models.ImageField(upload_to='photo')
    worktype=models.ForeignKey(admin_addwork,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class workershedule(models.Model):
   employee=models.ForeignKey(workerpage,on_delete=models.CASCADE)
   date=models.DateField()
   start_time=models.TimeField()
   end_time=models.TimeField()

   def __str__(self):
       return self.name




class user_appoinment(models.Model):
   user=models.ForeignKey(userpage,on_delete=models.CASCADE,related_name='appoinment')
   schedule=models.ForeignKey(workershedule,on_delete=models.CASCADE)
   status=models.IntegerField(default=0)

   def __str__(self):
       return self.name

class feedback(models.Model):
    user=models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    date=models.DateField()
    time=models.TimeField()
    feedback=models.CharField(max_length=800)
    replay=models.TextField(null=True, blank=True)


class payment(models.Model):
    user=models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    date = models.DateField()
    time = models.TimeField()
    cash=models.ForeignKey(admin_addwork,on_delete=models.CASCADE)

class admin_payment(models.Model):
    name = models.ForeignKey(userpage, on_delete=models.DO_NOTHING)
    amount=models.IntegerField()
    paid_date=models.DateField(auto_now=True)
    bill_date=models.DateField(auto_now=True)
    status=models.IntegerField(default=0)
























