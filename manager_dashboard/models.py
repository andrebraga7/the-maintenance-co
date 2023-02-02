from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


USER_TYPES = ((3, 'Client'), (2, 'Employee'), (1, 'Manager'))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    type = models.IntegerField(choices=USER_TYPES)

    class Meta:
        permissions = [
            ('manager', 'Manager'),
            ('employee', 'Employee'),
            ('client', 'Client')]


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
