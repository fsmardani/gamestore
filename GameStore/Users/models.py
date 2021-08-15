from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.models_utils import model_image_directory_path

# Create your models here.




class CustomUserManager(BaseUserManager):



    def create_user(self, email, password, phone="", **extra_fields):

        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
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







class Normal_user(AbstractUser):
    username = None
    phone = models.CharField(max_length=250)
    Addres = models.CharField(max_length=300)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()




class Vip_user(Normal_user):
    CONSOLE_MODEL = (
        ("PS4",),
        ("PS5",),
        ("XBOX",),
        ("NINTENDO_SWITCH",),

    )

    ConsoleModel = models.CharField(max_length=1, null=False, blank=False, choices=CONSOLE_MODEL)
    Rate = models.FloatField()

    email = models.EmailField(unique=True)
    picture = models.ImageField(upload_to=model_image_directory_path)
    pointuser = models.IntegerField()
    # Location =


