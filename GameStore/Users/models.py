from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from utils.models_utils import model_image_directory_path
from GameStore.cart_ordering.models import cart



class User(AbstractUser):
    pass


class PublicUser(models.Model):
    pass

class VipUser(models.Model):
    pass









class NormalProfile(models.Model):
    django_user = models.OneToOneField(User)



class VIPProfile(models.Model):
    django_user = models.OneToOneField(User)



class CustomUserManager(BaseUserManager):



    def create_user(self, email, password, phone="", **extra_fields):

        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        name = models.CharField(max_length=150)
        #rate = models.ForeignKey(cart.sum_of_score)
        user = self.model(email=email, phone=phone, **extra_fields)#########
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, phone="",  **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password,phone, **extra_fields)



class Normal_user(CustomUserManager):
    Address = models.CharField(max_length=500)
    #username = None
    #phone = models.CharField(max_length=250)
    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []
    #objects = CustomUserManager()
    def __str__(self):
        return self.user




class Vip_user(CustomUserManager):
    CONSOLE_MODEL = (
        ("PS4","playstation4"),
        ("PS5",'playstation5'),
        ("XBOX",'Microsoft XBOX'),
        ("NINTENDO_SWITCH" ,'NINTENDO_SWITCH'),

    )

    ConsoleModel = models.CharField(max_length=16, null=True, blank=True, choices=CONSOLE_MODEL)

    picture = models.ImageField(upload_to=model_image_directory_path)
    Location = models.BooleanField(verbose_name="ساکن تهران")


