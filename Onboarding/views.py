from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from .models import ContactFormSubmision , Verification , Administration , Profile
from .forms import ContactForm , CreateUserForm , VerificationForm , AdministrationForm 
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
import random
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def Home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            person_name = form.cleaned_data['name']
            person_email = form.cleaned_data['email']
            person_number = form.cleaned_data['number']
            person_message = form.cleaned_data['message']
            person = ContactFormSubmision.objects.create(email=person_email, number=person_number , name=person_name, message=person_message)
            person.save()
            subject = 'Response to Your Inquiry'
            subject2 = f'{person_name} just filled a Contact Form'

            # Render HTML email template
            html_message = render_to_string('email_template.html', {'person_name': person_name})
            plain_message = strip_tags(html_message)
            
            second_html_message = render_to_string('email_template2.html' , {'person_name': person_name , 'person_message': person_message , 'person_email': person_email})
            admin_plain_message = strip_tags(second_html_message)
             # Strips HTML tags to create plaintext version

            # Send HTML email
            configured_email = settings.EMAIL_HOST_USER
            receiver = [person_email]
            admin = ['crestalphatrade.com@gmail.com']
            email = EmailMultiAlternatives(subject, plain_message, configured_email, receiver)
            admin_email = EmailMultiAlternatives(subject2 , admin_plain_message , configured_email , admin)
            email.attach_alternative(html_message, "text/html")
            admin_email.attach_alternative(second_html_message , 'text/html')
            email.send(fail_silently=False)
            admin_email.send(fail_silently=False)


            print("Worked")

            return render(request , 'contact_submision.html' , {'name': person_name})
    else:
        form = ContactForm()
        print("Nope")
        return render(request , 'home.html' , {'form': form})

def Register(request):
    if request.user.is_authenticated:
        return redirect('Onboarding:dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                # Check if profile exists, create if not
                profile = Profile.objects.get_or_create(user=user)[0]  # Get or create profile
                # Now you can set additional profile fields if needed
                profile.save()
                user = form.cleaned_data['username']
                user_email = form.cleaned_data['email']
                codes = ["0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
                code = random.choices(codes , k=random.randint(6   , 6))
                verification_code = ' '.join(code)
                print(verification_code)
                subject = "Your Verification Code - Crest Alpha Trade"
                subject2 = f'{user} just signed up!'
                # Render HTML email template
                html_message = render_to_string('registeration_email.html', {'user': user ,  'verification_code': verification_code})
                plain_message = strip_tags(html_message)
                
                second_html_message = render_to_string('admin_reg_email.html' , {'user': user ,  'email': user_email})
                admin_plain_message = strip_tags(second_html_message)

                 # Strips HTML tags to create plaintext version

                # Send HTML email
                configured_email = settings.EMAIL_HOST_USER
                receiver = [user_email]
                admin = ['crestalphatrade.com@gmail.com']
                email = EmailMultiAlternatives(subject, plain_message, configured_email, receiver)
                admin_email = EmailMultiAlternatives(subject2 , admin_plain_message , configured_email , admin)
                email.attach_alternative(html_message, "text/html")
                admin_email.attach_alternative(second_html_message , 'text/html')
                email.send(fail_silently=False)
                admin_email.send(fail_silently=False)
                messages.success(request , f'Account created successfully, {user}')
                return redirect('Onboarding:RegVerify' , verification_code=verification_code , user=user)
        context = {'form': form}
        return render(request , 'test.html' , context)

def Login(request):
    if request.user.is_authenticated:
        return redirect('Onboarding:dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password') # Corrected field name
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Onboarding:dashboard')  # Redirect to the dashboard after successful login
            else:
                messages.error(request, 'Invalid username or password.')  # Add error message for invalid login
        context = {}
        return render(request, 'test2.html' , context)  # Render the login template


def LogoutUser(request):
    logout(request)
    return redirect('Onboarding:Login')

@login_required(login_url='Onboarding:Login')
def dashboard(request):
    return render(request , 'dashboard.html')

@login_required(login_url='Onboarding:Login')
def Trade(request):
    # Retrieve the username of the logged-in user
    username = request.user.username
    email = request.user.email
    subject = 'Successful Trade - Your Profit Awaits!'
    subject2 = f'{username} made a Trade!'

    # Render HTML email template
    html_message = render_to_string('trade_email.html', {'username': username})
    plain_message = strip_tags(html_message)
    
    second_html_message = render_to_string('admin_trade_email.html' , {'username': username ,  'email': email})
    admin_plain_message = strip_tags(second_html_message)
        # Strips HTML tags to create plaintext version

    # Send HTML email
    configured_email = settings.EMAIL_HOST_USER
    receiver = [email]
    admin = ['crestalphatrade.com@gmail.com']
    email = EmailMultiAlternatives(subject, plain_message, configured_email, receiver)
    admin_email = EmailMultiAlternatives(subject2 , admin_plain_message , configured_email , admin)
    email.attach_alternative(html_message, "text/html")
    admin_email.attach_alternative(second_html_message , 'text/html')
    email.send(fail_silently=False)
    admin_email.send(fail_silently=False)

    context = {'user': username}
    return render(request , 'trade.html', context)

def RegVerify(request , verification_code , user):
     if request.user.is_authenticated:
        return redirect('Onboarding:dashboard')
     else:
        if request.method == 'POST':
            form = VerificationForm(request.POST)
            if form.is_valid():
                verified_code = form.cleaned_data['code']
                new_code = ' '.join(verified_code)     
                verify = Verification.objects.create(code=new_code)
                verify.save()
                if verify.code == verification_code:
                    print("Access Granted")
                    return redirect('Onboarding:Login')
                else:
                    print("Access Denied")
                    message = 'Wrong Code'
                    context = {'form': form , 'user': user , 'message': message}
                    return render(request ,  'reg_verification.html' , context)
        else:
            form = VerificationForm()
            context = {'form': form , 'user': user}
            return render(request , 'reg_verification.html' , context)

def Transaction(request):
    return render(request , 'transaction.html')

# def Admin(request):
#     if request.method == 'POST':
#         form = AdministrationForm(request.POST)
#         if form.is_valid():
#             admin_name = form.cleaned_data['admin']
#             admin_password = form.cleaned_data['admin_pw']
#             admin = Administration.objects.create(name=admin_name , password=admin_password)
#             admin.save()
#             default_name = 'admin'
#             default_pw = 'crestadmin@2004'
#             if admin_name == default_name and admin_password == default_pw:
#                 return redirect('Onboarding:AdminDashboard')
#             else:
#                 return redirect('Onboarding:Admin')
#     else:
#         form = AdministrationForm()
#         context = {'form': form}          
#         return render(request, 'admin.html', context)



def AdminDashboard(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request , 'admin_dash.html' , context)

# def user_detail(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     return render(request, 'user_detail.html', {'user': user})

# def edit_user_profile(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     user_profile = user.userprofile  # Retrieve the UserProfile object associated with the User
#     form = UserProfileForm(request.POST or None, instance=user_profile)
#     if form.is_valid():
#         form.save()
#         return redirect('Onboarding:user_detail', user_id=user_id)
#     return render(request, 'edit_user_profile.html', {'form': form})

def my_view(request):
    # Assuming 'example' is the username of the user you want to retrieve profile information for
    user = User.objects.get(username='Samuek')
    profile = user.profile  # Access the profile using the reverse relationship
    # Now you can access the profile fields, for example:
    age = profile.age
    # Use the profile information as needed in your view logic
    return render(request, 'my_view.html', {'profile': profile})