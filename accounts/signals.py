from django.db.models.signals import post_save, pre_save, post_delete, m2m_changed, pre_delete, post_init
from django.dispatch import receiver

from .models import User, UserProfile

@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, *args, **kwargs):
   if created:
      # UserProfile.objects.create(user=instance)
      print('create user profile')
      UserProfile.objects.create(user=instance)
   else:
      try:
         profile = UserProfile.objects.get(user=instance) #instance = user object.
         profile.save()
      except:
         UserProfile.objects.create(user=instance)
         print('Non existant profile was created')
     
      print('update user profile')

@receiver(pre_save, sender=User)
def pre_save_update_user_receiver(sender, instance, *args, **kwargs): #instance = user object.
   print(instance.username, 'is being saved...')