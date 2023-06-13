from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



# Create your models here.


class UserManager(BaseUserManager):
    
   def create_user(self, first_name, last_name, username, email, password=None):
      if not email:
         raise ValueError('Users must have an email address')
      
      if not username:
         raise ValueError('Users must have an username')
      
      user = self.model(first_name=first_name, last_name=last_name, username=username, email=self.normalize_email(email))
      user.set_password(password)
      user.save(using=self._db)
      return user 

   def create_superuser(self, first_name, last_name, username, email, password=None):
      user = self.create_user(first_name, last_name, username, email, password=password)
      user.is_admin = True
      user.is_active = True
      user.is_staff = True
      user.is_superadmin= True
      user.save(using=self._db) 
      return user


class User(AbstractBaseUser):
   RESTAURANT_ROLE = 1
   CUSTOMER_ROLE = 2
   ROLE_CHOICE = (
      (RESTAURANT_ROLE, 'Restaurant'),
      (CUSTOMER_ROLE, 'Customer'),
   )

   first_name = models.CharField(max_length=100) 		# Name of user
   last_name = models.CharField(max_length=100) 		# Name of user
   username = models.CharField(max_length=100, unique=True) 	# Username of user
   email = models.EmailField(verbose_name="email address",max_length=100, unique=True) 	# Email of user
   phone_number = models.CharField(max_length=12, blank=True) 	# Phone number of user 		
   role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True) 	# Role of user

   #required fields
   date_joined = 	 models.DateTimeField(auto_now_add=True) 	# Date user joined database
   last_login = models.DateTimeField(auto_now_add=True) 	# Date user last logged in
   created_date = models.DateTimeField(auto_now_add=True) 	# Date user was created in database
   modified_date = models.DateTimeField(auto_now=True) 	# Date user was last modified in database
   is_admin = models.BooleanField(default=False) 	# Is user an admin?
   is_active = models.BooleanField(default=False) 	# Is user active?
   is_staff = models.BooleanField(default=False) 	# Is user a member of the 'Staff' or 'Admin' groups?
   is_superadmin = models.BooleanField(default=False) 	# Is user a superadmin?

   USERNAME_FIELD = 'email'   #login with the email adress
   REQUIRED_FIELDS = ['username', 'first_name', 'last_name']  #login with the username']

   def __str__(self): #name of user
      return self.email
   
   def has_perm(self, perm, obj=None):
      return self.is_admin
   
   def has_module_perms(self, app_label): #check if user has any perms for a given app label
      return True
   
   objects = UserManager()

class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete= models.CASCADE, blank=True, null=True) #user object in database, linked to the user table
   profile_picture = models.ImageField(default='default.jpg', upload_to='users/profile_pictures/%Y/%m/%d', blank=True, null=True) #path to the picture
   cover_photo = models.ImageField(default='default.jpg', upload_to='users/cover_photos/%Y/%m/%d', blank=True, null=True) #path to the cover photo') 
   address_line_1 = models.CharField(max_length=100, blank=True, null=True) #address line 1
   address_line_2 = models.CharField(max_length=100, blank=True, null=True) #address line 2
   country = models.CharField(max_length=50, blank=True, null=True) #country
   state = models.CharField(max_length=50, blank=True, null=True) #state
   city = models.CharField(max_length=50, blank=True, null=True) #city
   pin_code = models.CharField(max_length=10, blank=True, null=True) #pin code
   latitude = models.CharField(max_length=20, blank=True, null=True) #latitude
   longitude = models.CharField(max_length=20, blank=True, null=True) #longitude
   created_at = models.DateTimeField(auto_now_add=True) #date created
   modified_at = models.DateTimeField(auto_now=True) #date modified

   def __str__(self):
      return self.user.email


