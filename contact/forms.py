from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import (
    ContactForm,
    UserProfile,
    Order,
    Product,
    ProductListing,
    ContactMessage,
    FarmerProfile,
    Discussion,
    Event,
    Feedback,
)
from django.core.exceptions import ValidationError


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter discussion title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your discussion details here'
            }),
        }

class ContactFormModel(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message', 'attachment', 'subject']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
        return price


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self):
        cleaned_data = super().clean()
        print(f"[DEBUG] Cleaned data: {cleaned_data}")  # Debug validated data
        return cleaned_data
    

# Use the UserCreationForm for the user registration
class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        min_length=8,  # Password should be at least 8 characters
        label="Password"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get("confirm_password")
        password = self.cleaned_data.get("password")
        if password != confirm_password:
            raise ValidationError("The passwords do not match")
        return confirm_password

    # Optionally, override the save method to also create the UserProfile
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Create the UserProfile after saving the user
            user_profile = UserProfile(user=user, fullname=self.cleaned_data['fullname'])
            user_profile.save()
        return user
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class UserRegistrationForm(UserCreationForm):
    fullname = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'order_number',
            'product_name',
            'tracking_number',
            'estimated_delivery_date',
            'current_status',
            'current_location',
        ]


class ProductListingForm(forms.ModelForm):
    class Meta:
        model = ProductListing
        fields = ['product_name', 'product_description', 'product_price', 'product_image']


class FarmerProfileForm(forms.ModelForm):
    class Meta:
        model = FarmerProfile
        fields = ['name', 'bio', 'location', 'products', 'image']


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter event title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write event details here'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

class AddFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'title', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter feedback title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your feedback here'
           }),
        }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = FarmerProfile
        fields = ['user', 'name', 'bio', 'location', 'image', 'products']


