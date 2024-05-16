# Import necessary modules
from django.contrib.auth.models import User
from .models import Profile  # Import your Profile model if you have one defined

# Define the function to create profiles for existing users
def create_profiles_for_existing_users():
    # Get all existing users
    existing_users = User.objects.all()

    # Loop through each user
    for user in existing_users:
        # Check if the user already has a profile
        if not hasattr(user, 'profile'):
            # If the user doesn't have a profile, create one
            profile = Profile.objects.create(user=user)  # Adjust this according to your Profile model
            # Optionally, you can add additional fields to the profile here
            profile.save()

# Call the function to create profiles for existing users
create_profiles_for_existing_users()
