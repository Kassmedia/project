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
        # Only create the UserProfile if the user is being created (not updated)
        UserProfile.objects.create(user=instance, fullname=instance.username)
    else:
        # Ensure profile exists when the user already exists
        if not hasattr(instance, 'profile'):  # Checking if the user has a profile
            UserProfile.objects.create(user=instance, fullname=instance.username)
        else:
            # Optionally update the profile here if needed
            instance.profile.fullname = instance.username  # Update the fullname if required
            instance.profile.save()