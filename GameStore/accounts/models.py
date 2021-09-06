from django.conf import settings
import uuid
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class normalUserProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True,on_delete=models.CASCADE, related_name='profile')
    #first_name = models.CharField(max_length=50, unique=False)
    #last_name = models.CharField(max_length=50, unique=False)
    phone_number = models.CharField(max_length=10,  null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='O')

    class Meta:
        db_table = "profile"

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        normalUserProfile.objects.create(user=instance)
    instance.profile.save()


class vipUserProfile(models.Model):

   # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(normalUserProfile,primary_key=True, on_delete=models.CASCADE, related_name='normal')
    rate = models.IntegerField()

    class Meta:
        db_table = "vip"

