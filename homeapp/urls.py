from django.urls import path

from homeapp import views

urlpatterns=[
    path('',views.mainpage,name='mainpage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('register',views.register,name='register'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('user',views.user,name='user'),
    path('worker',views.worker,name='worker'),
    path('userregister',views.userregister,name='userregister'),
    path('workerregister',views.workerregister,name='workerregister'),
    path('view_user',views.view_user,name='view_user'),
    path('delete_user/<int:id>/',views.delete_user,name='delete_user'),
    path('user_view',views.user_view,name='user_view'),
    path('worker_view',views.worker_view,name='worker_view'),
    path('view_worker',views.view_worker,name='view_worker'),
    path('delete_worker/<int:id>/',views.delete_worker,name='delete_worker'),
    path('update_worker/<int:id>/', views.update_worker, name='update_worker'),

    path('uw_view',views.uw_view,name='uw_view'),
    path('uw',views.uw,name='uw'),

    path('addworker_schedule',views.addworker_schedule,name='addworker_schedule'),
    path('schedule',views.schedule,name='schedule'),
    path('schedule_view',views.schedule_view,name='schedule_view'),
    path('update_schedule/<int:id>/',views.update_schedule,name='update_schedule'),
    path('delete_schedule/<int:id>/',views.delete_schedule,name='delete_schedule'),
    path('user_schedule',views.user_schedule,name='user_schedule'),
    path('user_sheduleview',views.user_sheduleview,name='user_sheduleview'),


    path('admin_workemanagementview',views.admin_workemanagementview,name='admin_workemanagementview'),
    path('admin_addworks',views.admin_addworks,name='admin_addworks'),
    path('addwork_view',views.addwork_view,name='addwork_view'),
    path('update_addwork/<int:id>/',views.update_addwork,name='update_addwork'),
    path('delete_addwork/<int:id>/',views.delete_addwork,name='delete_addwork'),


    # path('add_appoinment',views.add_appoinment,name='add_appoinment'),
    # path('appoinment_view',views.appoinment_view,name='appoinment_view'),
    path('admin_appoinment',views.admin_appoinment,name='admin_appoinment'),
    path('adminappoinment_view',views.adminappoinment_view,name='adminappoinment_view'),
    path('user_takeappoinment/<int:id>/',views.user_takeappoinment,name='user_takeappoinment'),
    path('appoinment_view',views.appoinment_view,name='appoinment_view'),
    path('appoinment_viewworker',views.appoinment_viewworker,name='appoinment_viewworker'),
    path('appoinment_viewadmin',views.appoinment_viewadmin,name='appoinment_viewadmin'),
    path('approve_appointment/<int:id>/',views.approve_appointment,name='approve_appointment'),
    path('reject_appointment/<int:id>/',views.reject_appointment,name='reject_appointment'),

    path('feedbacks',views.feedbacks,name='feedbacks'),
    path('feedback_viewreplay',views.feedback_viewreplay,name='feedback_viewreplay'),
    path('admin_feedback',views.admin_feedback,name='admin_feedback'),
    path('adminfeedback_view',views.adminfeedback_view,name='adminfeedback_view'),
    path('admin_replay/<int:id>/',views.admin_replay,name='admin_replay'),
    path('user_feed_view',views.user_feed_view,name='user_feed_view'),


    path('payments',views.payments,name='payments'),
    path('payment_view',views.payment_view,name='payment_view'),
    path('user_bill',views.user_bill,name='user_bill'),
    path('adminpayment_view',views.adminpayment_view,name='adminpayment_view'),
    path('add_payment',views.add_payment,name='add_payment'),
    path('view_payment',views.view_payment,name='view_payment'),
    path('paydirect/<int:id>/',views.paydirect,name='paydirect'),
    path('paynow/<int:id>/',views.paynow,name='paynow'),
    path('paybtn',views.paybtn,name='paybtn'),
    path('worker_payments',views.worker_payments,name='worker_payments'),
    path('logout_view',views.logout_view,name='logout_view'),








]