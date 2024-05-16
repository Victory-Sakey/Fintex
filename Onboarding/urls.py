from . import views
from django.urls import path

app_name = 'Onboarding'

urlpatterns = [
    path('' , views.Home , name='Home'),
    path('register' , views.Register , name='Register'),
    path('email_verification/<str:user>/<str:verification_code>/' , views.RegVerify , name='RegVerify'),
    path('login' , views.Login , name='Login'),
    path('logout/' , views.LogoutUser ,  name='LogoutUser'),
    path('dashboard' , views.dashboard , name='dashboard'),
    path('dashboard/trade' , views.Trade , name='Trade'),
    path('transaction' , views.Transaction , name='Transaction'),
    path('crestadmin/dashboard' , views.AdminDashboard , name='AdminDashboard'),
    path('my_view' , views.my_view , name='my_view')
    # path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    
    # path('crestadmin' , views.Admin , name='Administration'),
]