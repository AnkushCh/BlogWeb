from django.db.models.signals import post_save

from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# here v have  a funtion that createsa user profile
# every time a user is created.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# there is asender user and a sginal post_save
# means that when a user is saved  User sends post_save signal
# and the signa is received by the decoraot receiver
# and here this reciever is th create_profile function,
# and this takes all the arguments.
# two main r instance and created args.
# and then if that user instance is created ,then create a profile of that user instance.

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


# herev just save the instance of user profile.
