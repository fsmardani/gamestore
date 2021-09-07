import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.conf import settings
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "login"

class normalUserProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True,on_delete=models.CASCADE, related_name='profile')
    #first_name = models.CharField(max_length=50, unique=False)
    #last_name = models.CharField(max_length=50, unique=False)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
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

    def __str__(self):
        return self.user.user.email