from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from homeapp.forms import userform, LoginRegister, workerform,workerscheduleform,admin_addworkeform,user_appoinmentform,feedbackform,paymentform,admin_paymentform
from homeapp.models import userpage,workerpage,workershedule,admin_addwork,user_appoinment,feedback,payment,admin_payment,Login


# Create your views here.
def mainpage(request):
    return render(request,'index1.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminpage')
            elif user.is_user:
                return redirect('user')
            elif user.is_worker:
                return redirect('worker')
        else:
            messages.info(request,'invalid credentials')
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

@login_required(login_url="loginpage")
def adminpage(request):
    return render(request,'inindexadm.html')


@login_required(login_url="loginpage")
def user(request):
    return render(request,'user.html')


@login_required(login_url="loginpage")
def worker(request):
    return render(request,'worker.html')



def userregister(request):
    user_form=LoginRegister()
    userregister_form=userform()
    if request.method=='POST':
        user_form=LoginRegister(request.POST)
        userregister_form=userform(request.POST,request.FILES)
        if user_form.is_valid()and userregister_form.is_valid():
            user=user_form.save(commit=False)
            user.is_user=True
            user.save()
            userregister=userregister_form.save(commit=False)
            userregister.user=user
            userregister.save()
            messages.info(request,'Registration Successfully')
            return redirect('loginpage')
    return render(request,'userregister.html',{'user_form':user_form,'userregister_form':userregister_form})


def workerregister(request):
    user_form = LoginRegister()
    workerregister_form=workerform()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        workerregister_form=workerform(request.POST,request.FILES)
        if user_form.is_valid() and workerregister_form.is_valid():
            user=user_form.save(commit=False)
            user.is_worker = True
            user.save()
            workerregister=workerregister_form.save(commit=False)
            workerregister.user = user
            workerregister.save()
            messages.info(request, 'Registration Successfully')
            return redirect('loginpage')
    return render(request,'workerregister.html',{'worker_form':user_form,'workerregister_form':workerregister_form})



@login_required(login_url="loginpage")
def view_user(request):
    data=userpage.objects.all()
    return render(request,'view_user.html',{'data':data})

@login_required(login_url="loginpage")
def user_view(request):
    return render(request,'user_view.html')


@login_required(login_url="loginpage")
def delete_user(request,id):
    d=userpage.objects.get(id=id)
    u=Login.objects.get(user=d)
    if request.method=='POST':
        u.delete()
        return redirect('view_user')
    else:
        return redirect('view_user')


@login_required(login_url="loginpage")
def view_worker(request):
    data=workerpage.objects.all()
    return render(request,'view_worker.html',{'data':data})


@login_required(login_url="loginpage")
def worker_view(request):
    return render(request,'worker_view.html')


@login_required(login_url="loginpage")
def delete_worker(request,id):
    d=workerpage.objects.get(id=id)
    w=Login.objects.get(worker=d)
    if request.method=="POST":
        w.delete()
        return redirect('view_worker')
    else:
        return redirect('view_worker')



@login_required(login_url="loginpage")
def update_worker(request,id):
    data=workerpage.objects.get(id=id)
    form=workerform(instance=data)
    if request.method=='POST':
        form=workerform(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_worker')
    return render(request,'update_worker.html',{'form':form})


@login_required(login_url="loginpage")
def uw(request):
 data=workerpage.objects.all()
 return render(request,'uw.html',{'data':data})


@login_required(login_url="loginpage")
def uw_view(request):
    return render(request,'uw_view.html')


@login_required(login_url="loginpage")
def addworker_schedule(request):
    form=workerscheduleform()
    if request.method=='POST':
        form=workerscheduleform(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.employee=workerpage.objects.get(user=request.user)
            form.save()
            return redirect('schedule_view')
    return render(request,'addworker_schedule.html',{'form':form})


@login_required(login_url="loginpage")
def schedule(request):
    return render(request,'w_scheduleview.html')


@login_required(login_url="loginpage")
def schedule_view(request):
 data=workershedule.objects.all()
 return render(request,'schedule.html',{'data':data})


@login_required(login_url="loginpage")
def update_schedule(request,id):
    data=workershedule.objects.get(id=id)
    form=workerscheduleform(instance=data)
    if request.method=='POST':
        form=workerscheduleform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('schedule_view')
    return render(request,'update_schedule.html',{'form':form})


@login_required(login_url="loginpage")
def delete_schedule(request,id):
    workershedule.objects.get(id=id).delete()
    return redirect('schedule_view')


@login_required(login_url="loginpage")
def user_schedule(request):
    s=workershedule.objects.all()
    context={
        'schedule': s
    }
    return render(request,'user_schedule.html',context)


@login_required(login_url="loginpage")
def user_sheduleview(request):
    return render(request,'user_schedueview.html')


@login_required(login_url="loginpage")
def admin_workemanagementview(request):
    return render(request,'admin_workemanagementview.html')

@login_required(login_url="loginpage")
def admin_addworks(request):
    form=admin_addworkeform
    if request.method=='POST':
        form=admin_addworkeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addwork_view')
    return render(request,'addwork.html',{'form':form})


@login_required(login_url="loginpage")
def addwork_view(request):
    data=admin_addwork.objects.all()
    return render(request,'addworke_view.html',{'data':data})


@login_required(login_url="loginpage")
def update_addwork(request,id):
    data=admin_addwork.objects.get(id=id)
    form=admin_addworkeform(instance=data)
    if request.method=='POST':
        form=admin_addworkeform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('addwork_view')
    return render(request,'update_addwork.html',{'form':form})


@login_required(login_url="loginpage")
def delete_addwork(request,id):
    data=admin_addwork.objects.get(id=id).delete()
    return redirect('addwork_view')




# def add_appoinment(request):
#     form=user_appoinmentform
#     if request.method=='POST':
#         form=user_appoinmentform(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('user')
#     return render(request,'add_appoinment.html',{'form':form})


@login_required(login_url="loginpage")
def admin_appoinment(request):
    data=user_appoinment.objects.all()
    return render(request,'admin_appoinment.html',{'data': data})


@login_required(login_url="loginpage")
def adminappoinment_view(request):
    return render(request,'admin_appoinmentview.html')


@login_required(login_url="loginpage")
def user_takeappoinment(request,id):
    s=workershedule.objects.get(id=id)
    c=userpage.objects.get(user=request.user)
    appoinment=user_appoinment.objects.filter(user=c,schedule=s)
    if appoinment.exists():
        messages.info(request, 'You have already requested appoinment for this schedule')
        return redirect('user_schedule')
    else:
        if request.method=='POST':
            obj = user_appoinment()
            obj.user = c
            obj.schedule = s
            obj.save()
            messages.info(request,'Appoinment booked successfully')
            return redirect('appoinment_view')
    return render(request,'add_appoinment.html',{'schedule':s})


@login_required(login_url="loginpage")
def appoinment_view(request):
    c=userpage.objects.get(user=request.user)
    a=user_appoinment.objects.filter(user=c)
    return render(request,'appoinment_view.html',{'a':a})

@login_required(login_url="loginpage")
def appoinment_viewworker(request):
    a=user_appoinment.objects.all()
    return render(request,'appoinment_viewworker.html',{'a':a})


@login_required(login_url="loginpage")
def appoinment_viewadmin(request):
    a=user_appoinment.objects.all()
    return render(request,'admin_appoinment.html',{'a':a})

@login_required(login_url="loginpage")
def approve_appointment(request,id):
    a=user_appoinment.objects.get(id=id)
    a.status=1
    a.save()
    messages.info(request,'Appointment Conformed')
    return redirect('appoinment_viewadmin')


@login_required(login_url="loginpage")
def reject_appointment(request,id):
    n=user_appoinment.objects.get(id=id)
    n.status=2
    n.save()
    messages.info(request,'Appointment Rejected')
    return redirect('appoinment_viewadmin')

@login_required(login_url="loginpage")
def feedbacks(request):
    form=feedbackform()
    u=request.user
    if request.method=='POST':
        form=feedbackform(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('user_feed_view')
    return render(request,'feedback.html', {'form': form})

@login_required(login_url="loginpage")
def user_feed_view(request):
    data=feedback.objects.filter(user=request.user)
    return render(request,"user_feed_view.html",{'data':data})


@login_required(login_url="loginpage")
def feedback_viewreplay(request):
    return render(request,'feedback_viewreplay.html')


@login_required(login_url="loginpage")
def admin_feedback(request):
    data = feedback.objects.all()
    return render(request,'admin_feedback.html',{'data': data})


@login_required(login_url="loginpage")
def adminfeedback_view(request):
    return render(request,'adminfeedback_view.html')


@login_required(login_url="loginpage")
def admin_replay(request,id):
    f=feedback.objects.get(id=id)
    if request.method=='POST':
        r = request.POST.get('replay')
        f.replay = r
        f.save()
        messages.info(request,'Reply send for complaint')
        return redirect('admin_feedback')
    return render(request,'replay.html', {'f': f})



@login_required(login_url="loginpage")
def user_bill(request):
    s =admin_addwork .objects.all()
    context ={
        'schedule': s
    }
    return render(request, 'user_bill.html', context)


# def payments(request):
#     data = admin_payment.objects.all()
#     context = {
#         'schedule': data
#     }
#     return render(request, 'user_payment.html', context)

@login_required(login_url="loginpage")
def payments(request):
    u=userpage.objects.get(user=request.user)
    data=admin_payment.objects.filter(name=u)
    return render(request, 'user_payment.html',{'data': data})


@login_required(login_url="loginpage")
def payment_view(request):
    return render(request, 'payment_view.html')


@login_required(login_url="loginpage")
def adminpayment_view(request):
    return render(request, 'adminpayment_view.html')


@login_required(login_url="loginpage")
def add_payment(request):
    form = admin_paymentform()
    if request.method == 'POST':
        form = admin_paymentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_payment')
    return render(request, 'adminadd_payment.html', {'form': form})


@login_required(login_url="loginpage")
def view_payment(request):
    a = admin_payment.objects.all()
    return render(request, 'adminview_payment.html', {'a': a})


@login_required(login_url="loginpage")
def paydirect(request,id):
    a = admin_payment.objects.get(id=id)
    a.status = 0
    a.save()
    messages.info(request, 'choose direct payment')
    return redirect('payments')


@login_required(login_url="loginpage")
def paynow(request,id):
    n=admin_payment.objects.get(id=id)
    n.status=1
    n.save()
    messages.info(request,'Appointment Rejected')
    return redirect('payments')

@login_required(login_url="loginpage")
def paybtn(request):
  data = admin_payment.objects.all()
  return render(request, 'paybtn.html',{'data': data})


@login_required(login_url="loginpage")
def worker_payments(request):
    data=admin_payment.objects.all()
    return render(request, 'worker_payment.html',{'data': data})

# def workerpayment_view(request):
#     return render(request, 'workerpayment_view.html')


@login_required(login_url="loginpage")
def logout_view(request):
    logout(request)
    return redirect('loginpage')





