from . import views
from django.urls import path

app_name = 'Onboarding'

urlpatterns = [
    path('' , views.suspension , name='Home'),
    path('register' , views.suspension , name='Register'),
    path('email_verification/<str:user>/<str:verification_code>/' , views.suspension , name='RegVerify'),
    path('login' , views.suspension , name='Login'),
    path('logout/' , views.suspension ,  name='LogoutUser'),
    path('dashboard' , views.suspension , name='dashboard'),
    path('dashboard/trade' , views.suspension , name='Trade'),
    path('dashboard/transaction' , views.suspension , name='Transaction'),
    path('dashboard/transaction/pending/<int:amount>/<str:wallet_address>/<str:account>/' , views.suspension , name='TransactionPending'),
    path('dashboard/transaction/success' , views.suspension , name='TransactionSuccess'),
    path('dashboard/settings-info' , views.SettingsInfo , name='SettingsInfo'),
    path('fadmin/dashboard' , views.suspension , name='AdminDashboard'),
    path('edit_user/<int:user_id>/', views.suspension, name='edit_user'),
    path('my_view' , views.suspension , name='my_view'),
    # path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('translate' , views.suspension , name='translate'),
    path('suspension' , views.suspension , name='Suspension'),
]