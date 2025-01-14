from asyncio.log import logger
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.utils.timezone import now
from django.contrib.auth.backends import BaseBackend
from django.core.exceptions import ObjectDoesNotExist


class ContactForm(models.Model):
    SUBJECT_CHOICES = [
        ('General Inquiry', 'General Inquiry'),
        ('Partnership', 'Partnership'),
        ('Feedback', 'Feedback'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    attachment = models.FileField(upload_to='uploads/', null=True, blank=True)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='farmer_images/', blank=True, null=True)
    products = models.ManyToManyField('Product', blank=True)
    

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=200, null=True, blank=True)  # Allow null or blank values

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('placed', 'Order Placed'),
        ('shipped', 'Shipped'),
        ('sorting', 'Sorting'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    ]

    order_number = models.CharField(max_length=20, unique=True)
    product_name = models.CharField(max_length=255)
    tracking_number = models.CharField(max_length=50, unique=True)
    estimated_delivery_date = models.DateField()
    current_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='placed')
    last_updated = models.DateField(auto_now=True)
    current_location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.order_number



class ProductListing(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name


class SubscriptionPlan(models.Model):
    title = models.CharField(max_length=100)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField()

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.fullname or self.user.username

class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="farmer_profile")
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='farmer_images/', blank=True, null=True)
    products = models.ManyToManyField('Product', blank=True)
    subscription_plan = models.ForeignKey('SubscriptionPlan', on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField(default=0)
    email = models.EmailField(null=True, blank=True)  # Add this line
    phone = models.CharField(max_length=15, null=True, blank=True)  # Add this line

    def __str__(self):
        return self.name

    @property
    def product_count(self):
        """Returns the number of products associated with this farmer"""
        return self.products.count()

    @property
    def active_orders(self):
        """Returns the active orders for this farmer's products"""
        return Order.objects.filter(product_name__in=self.products.all(), status='pending')

class Month(models.Model):
    name = models.CharField(max_length=255)
    days_in_month = models.IntegerField()
    products = models.ManyToManyField(Product, related_name='months')

    def __str__(self):
        return self.name

class Discussion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title   
    
class Feedback(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None  # Return None if username or password is missing

        try:
            # Check if the user exists with the provided email (username)
            user = User.objects.get(email=username)
        except ObjectDoesNotExist:
            return None  # Return None if no user is found with the provided email

        # Check if the user provided the correct password
        if user.check_password(password):
            return user
        else:
            logger.error(f"Incorrect password for user: {username}")
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None  # Return None if the user does not exist