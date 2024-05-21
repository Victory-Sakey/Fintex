from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class ContactFormSubmision(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.IntegerField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Verification(models.Model):
    code = models.CharField(max_length=50)

class Administration(models.Model):
    admin = models.CharField(max_length=100)
    admin_pw = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add your custom fields here
    tel = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=100 , null=True)
    bitcoin_address = models.CharField  (max_length=100 , null=True)
    etherum_address = models.CharField(max_length=100 , null=True)
    bonus = models.IntegerField(default=0)
    profit = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username



class Transactions(models.Model):
    # Define choices for Balance_Type field
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions' , null=True)  # Add this line
    TOTAL_BALANCE = 'Total balance'
    BALANCE_CHOICES = [
        (TOTAL_BALANCE, 'Total balance'),
    ]

    # Define choices for Withdraw_Method field
    BITCOIN = 'Bitcoin'
    ETHEREUM = 'Ethereum'
    WITHDRAW_METHOD_CHOICES = [
        (BITCOIN, 'Bitcoin'),
        (ETHEREUM, 'Ethereum'),
    ]

    # Define fields with choices
    Select_Balance_Type = models.CharField(max_length=50, choices=BALANCE_CHOICES)
    Select_Assets = models.CharField(max_length=50, choices=WITHDRAW_METHOD_CHOICES)
    Wallet_Address = models.CharField(max_length=50, null=True)
    Amount = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.user.username} - {self.Select_Assets} - {self.Amount}"


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add additional fields for user profile information
#     bit_address = models.CharField(max_length=500)
#     # Add more fields as needed

#     def __str__(self):
#         return self.user.username
