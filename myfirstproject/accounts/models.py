from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
# Create your models here.
 
class MyUserManager(BaseUserManager):
   def create_user(self, email,password=None):
       """
       Creates and saves a User with the given email,and password.
       """
       if not email:
           raise ValueError('Users must have an email address')
       if not password:
           raise ValueError('Users must have password')

       user = self.model(email=self.normalize_email(email))
       user.set_password(password)
       user.save(using=self._db)
       return user
 
   def create_superuser(self, email,password=None):
       """
       Creates and saves a superuser with the given email, date of
       birth and password.
       """
       user = self.create_user(email,password=password)
       user.is_admin = True
       user.is_staff = True
       user.save(using=self._db)
       return user

   def create_staffuser(self, email,password=None):
       """
       Creates and saves a superuser with the given email, date of
       birth and password.
       """
       user = self.create_user(email,password=password)
       user.is_staff = True
       user.save(using=self._db)
       return user

# UserManager class code here
class User(AbstractBaseUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True, default='abc@gmail.com')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

status_choice={
    ('single','single'),
    ('married','married')
}

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null =True)
    full_name = models.CharField(max_length=255)
    profile_pic = models.ImageField(null = True,blank=True) 
    bio_data = models.FileField(null=True,blank=True)
    contact = models.IntegerField()
    location = models.CharField(max_length=50)
    marital_status = models.CharField(
        max_length=20,
        choices = status_choice,
        default='1'
    )

    def __str__(self):
        return str(self.user)


