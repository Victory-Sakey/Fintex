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
    path('dashboard/transaction' , views.Transaction , name='Transaction'),
    path('dashboard/transaction/pending/<int:amount>/<str:wallet_address>/<str:account>/' , views.TransactionPending , name='TransactionPending'),
    path('dashboard/transaction/success' , views.TransactionSuccess , name='TransactionSuccess'),
    path('dashboard/settings-info' , views.SettingsInfo , name='SettingsInfo'),
    path('fadmin/dashboard' , views.AdminDashboard , name='AdminDashboard'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('my_view' , views.my_view , name='my_view'),
    # path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('translate' , views.translate , name='translate'),
]