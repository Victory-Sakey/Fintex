from django import forms
from django.forms import ModelForm
from .models import ContactFormSubmision , Verification , Administration , Profile , Transactions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormSubmision
        fields = ['name' , 'email', 'number', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-gray-200 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline focus:ring-2 focus:ring-indigo-400'}),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-gray-200 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline focus:ring-2 focus:ring-indigo-400'}),
            'number': forms.TextInput(attrs={
                'class': 'w-full bg-gray-200 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline focus:ring-2 focus:ring-indigo-400'}),
            'message': forms.Textarea(attrs={
                'class': 'w-full h-32 bg-gray-200 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline focus:ring-2 focus:ring-indigo-400'})
        }


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        custom_class = "block w-full rounded-md border-0 py-1.5 text-gray-900 p-4 shadow-sm ring-1 ring-inset ring-gray-300 outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': custom_class,
            })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    

class VerificationForm(forms.ModelForm):
    class Meta:
        model = Verification
        fields = ['code']
        labels = {
            'code': ''
        }
        widgets = {
            'code': forms.TextInput(attrs={
                'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 p-4 outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'  , 'placeholder':  'Input Code'  
            })
        }

class AdministrationForm(forms.ModelForm):
    class Meta:
        model = Administration
        fields = ['admin' , 'admin_pw']
        labels = ''
        widgets = {
            'admin': forms.TextInput(attrs={
                'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 outline-none p-4 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'
            }),
            'admin_pw': forms.PasswordInput(attrs={
                'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 outline-none p-4 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'})
        }

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['bit_address', ]  # Add more fields as needed




class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['Select_Balance_Type', 'Select_Assets']
