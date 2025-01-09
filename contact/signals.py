from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, fullname=instance.username)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create the UserProfile only if the user is newly created
        UserProfile.objects.create(user=instance, fullname=instance.username)
    else:
        # Ensure profile exists and update if necessary
        profile, created = UserProfile.objects.get_or_create(user=instance)
        
        if not created:  # If the profile already existed, update it
            # Optionally update the profile here if needed
            profile.fullname = instance.username  # Example update
            profile.save()