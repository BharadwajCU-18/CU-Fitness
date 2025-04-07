from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from .models import FitnessProfile

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a fitness profile when a new user is created
        FitnessProfile.objects.create(user=instance)
    else:
        try:
            # Check if the user already has a fitness profile
            profile = instance.fitnessprofile
        except ObjectDoesNotExist:
            # Create a fitness profile if it doesn't exist
            FitnessProfile.objects.create(user=instance)
        else:
            # If it exists, save it
            profile.save()
