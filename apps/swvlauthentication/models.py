from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=500, blank=True, null=True)
    birthday = models.DateField(default=False)


def __str__(self):
    return str(self.user)


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
