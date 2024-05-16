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
    age = models.IntegerField(null=True, blank=True)



class Transactions(models.Model):
    # Define choices for Balance_Type field
    TOTAL_BALANCE = 'Total balance ($0.00)'
    BALANCE_CHOICES = [
        (TOTAL_BALANCE, 'Total balance ($0.00)'),
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

    def __str__(self):
        return f"Transaction {self.pk}"

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add additional fields for user profile information
#     bit_address = models.CharField(max_length=500)
#     # Add more fields as needed

#     def __str__(self):
#         return self.user.username
