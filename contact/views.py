from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .forms import ContactFormModel, LoginForm, SignUpForm
from .models import ContactForm, UserProfile
from django.http import HttpResponse
from .models import Order
from .models import Farmer
from .models import Month, Product
from .forms import ProductListingForm, ContactForm
from django.core.mail import send_mail
from .forms import ProductForm, ContactForm
from .forms import FarmerProfileForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import FarmerProfile
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Product
from .models import Discussion
from .forms import AddPostForm
from .models import Event
from .forms import AddEventForm
from .models import Feedback
from .forms import AddFeedbackForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login


# Contact View
def contact_view(request):
    if request.method == 'POST':
        form = ContactFormModel(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, "Your message has been sent successfully!")
            return render(request, 'contact/confirmation.html', {'form': form})
        else:
            messages.error(request, "There was an error in your submission.")
    else:
        form = ContactFormModel()
    return render(request, 'contact_us.html', {'form': form})


def home(request):
    return render(request, 'index.html')

def homepage(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(request, username=email, password=password)

            if user:
                print(f"[DEBUG] User authenticated: {user.email}")  # Email of authenticated user
                print(f"[DEBUG] Redirecting {user.username} to dashboard.")  # Debug user info
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('dashboard')  # Ensure 'dashboard' matches your URL name
            else:
                print("[ERROR] Authentication failed. Check credentials.")  # More specific debug message
                messages.error(request, "Invalid email or password.")
        else:
            print("[ERROR] Form is invalid. Validation failed.")  # Debug invalid form

    else:
        form = LoginForm()
        print("[DEBUG] Rendering login page.")  # Debug rendering info

    return render(request, '/login.html', {'form': form})

# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash password
            user.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
        else:
            messages.error(request, "There was an error with your registration.")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# User Logout View
def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')


def reset_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = UserProfile.objects.get(email=email)
            # Simulate sending a reset link (implement real email sending later)
            messages.success(request, "A reset link has been sent to your email.")
            return redirect('login')
        except UserProfile.DoesNotExist:
            messages.error(request, "Email not found.")
    return render(request, 'reset_password.html')


def about_view(request):
    return render(request, 'about.html')

def blog_post(request):
    return render(request, 'blog-post.html')

def affiliate(request):
    return render(request, 'affiliate.html')

def article1(request):
    return render(request, 'article1.html')

def article2(request):
    return render(request, 'article2.html')

def article3(request):
    return render(request, 'article3.html')

def article4(request):
    return render(request, 'article4.html')

def article5(request):
    return render(request, 'article5.html')

def article6(request):
    return render(request, 'article6.html')

def bank_payment(request):
    return render(request, 'bank-payment.html')

def base(request):
    return render(request, 'base.html')

def checkout(request):
    return render(request, 'checkout.html')

def community_forum(request):
    return render(request, 'community-forum.html')

def confirmation(request):
    return render(request, 'confirmation.html')

def contact(request):
    return render(request, 'contact.html')

#def dashboard(request):
    # Example data for charts and price suggestions
    product_views_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    product_views_data = [500, 700, 850, 1000, 1200, 1300]
    
    sales_labels = ['Tomatoes', 'Lettuce', 'Rice', 'Carrots', 'Pineapples']
    sales_data = [1200, 800, 1100, 650, 950]
    
    market_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    market_data = [400, 550, 700, 850, 1000, 1150]
    
    price_suggestions = [
        {'name': 'Tomatoes', 'price_change': '+5%', 'market_trend': 'High demand in the region'},
        {'name': 'Rice', 'price_change': '-3%', 'market_trend': 'Price drop expected in the coming weeks'},
        {'name': 'Lettuce', 'price_change': '+10%', 'market_trend': 'Seasonal peak expected'}
    ]
    
    context = {
        'product_views_labels': product_views_labels,
        'product_views_data': product_views_data,
        'sales_labels': sales_labels,
        'sales_data': sales_data,
        'market_labels': market_labels,
        'market_data': market_data,
        'price_suggestions': price_suggestions
    }
    
    return render(request, 'dashboard.html', context)

@login_required
def dashboard_view(request):
    print(f"User logged in: {request.user.username}")  # Debugging line
    return render(request, 'dashboard.html', {'user': request.user})


def data_analysis(request):
    return render(request, 'data analysis.html')

def logistics_view(request):
    orders = Order.objects.all()  # Fetch all orders from the database
    return render(request, 'Delivery and Logistics Page.html', {'orders': orders})

def farmer_profile(request):
    farmers = Farmer.objects.all()
    return render(request, 'farmer_profile.html', {'farmers': farmers})

def FarmerProfiles(request):
    farmers = Farmer.objects.all()
    return render(request, 'Farmer Profiles.html', {'farmers': farmers})

def data_analysis(request):
    return render(request, 'data analysis.html')

def Government_NGO_Paternership(request):
    return render(request, 'Government NGO Patnerships.html')

def leaderboard(request):
    # Sample data for demonstration
    referrers = [
        {"name": "Adebayo John", "referrals": 60},
        {"name": "Chinwe Ndukwe", "referrals": 55},
        {"name": "Ibrahim Musa", "referrals": 50},
        {"name": "Funke Ajayi", "referrals": 45},
        {"name": "Bola Okonkwo", "referrals": 40},
    ]
    return render(request, 'leaderboard Page.html', {'referrers': referrers})

def marketplace(request):
    return render(request, 'marketplace.html')

def password(request):
    return render(request, 'password.html')

def payment_processing(request):
    return render(request, 'payment-processing.html')

def payment(request):
    return render(request, 'payment.html')

def privacy(request):
    return render(request, 'privacy.html')

def product(request):
    return render(request, 'product.html')

def productlink(request):
    return render(request, 'productlink.html')

def resetpassword(request):
    return render(request, 'reset_password.html')

def resetpassword_done(request):
    return render(request, 'reset_password_done.html')

def reward(request):
    return render(request, 'Rewards Page.html')

#def seasonalCalendar(request):
    return render(request, 'seasonal-calendar.html')


def seasonal_calendar(request):
    months = Month.objects.all()
    available_products = Product.objects.all()
    return render(request, 'seasonal-calendar.html', {
        'months': months,
        'available_products': available_products,
    })

#def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        products = request.POST.getlist('products')
        # Process subscription logic here
        return redirect('thank_you')
    return redirect('subscribe')

def subscribe(request):
    return render(request, 'subscribe.html')

def subscription_plans(request):
    plans = [
        {"title": "Farmer Plan", "price": "₦5,000", "pricePerMonth": "₦5,000/month", "features": ["Highlighted listings", "Analytics", "Priority support"]},
        {"title": "Buyer Plan", "price": "₦2,000", "pricePerMonth": "₦2,000/month", "features": ["Early access", "Discounts", "24/7 support"]}
    ]
    return render(request, 'subscription_plans.html', {'plans': plans})

def payment(request):
    # Logic for handling payment
    plan = request.GET.get('plan')
    price = request.GET.get('price')
    return render(request, 'payment.html', {'plan': plan, 'price': price})

def terms(request):
    return render(request, 'terms.html')

def trackOrder(request):
    return render(request, 'track order.html')

def ussdPayment(request):
    return render(request, 'ussd-payment.html')

def welcome(request):
    return render(request, 'welcome.html')


def Delivery_logistics(request):
    return render(request, 'Delivery_and_Logistics_Page.html')

def farmers_dashboard(request):
    return render(request, 'farmers dashboard.html')

def blog(request):
    return render(request, 'blog-post.html')


def list_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your product has been listed successfully!')
            return redirect('list_product')
    else:
        form = ProductForm()
    return render(request, 'list_product.html', {'form': form})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Send email notification
            send_mail(
                subject='New Contact Message',
                message=f"Message from {form.cleaned_data['name']} ({form.cleaned_data['email']}):\n\n{form.cleaned_data['message']}",
                from_email='no-reply@example.com',
                recipient_list=['support@example.com'],
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact_us')
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

def farmer_profile_view(request):
    if request.method == 'POST':
        form = FarmerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect after successful save
    else:
        form = FarmerProfileForm()
    return render(request, 'farmer_profile.html', {'form': form})


@login_required
def edit_profile_view(request):
    profile = get_object_or_404(FarmerProfile, user=request.user)  # Assuming the profile is linked to the user
    if request.method == 'POST':
        form = FarmerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('farmer_profile')  # Redirect to farmer profile page
    else:
        form = FarmerProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form, 'profile': profile})


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')  # Redirect to the homepage or any other page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})

# Sample Notification Model (Adjust as per your implementation)
class Notification:
    def __init__(self, message, timestamp, read=False):
        self.message = message
        self.timestamp = timestamp
        self.read = read

# Simulating a list of notifications (Replace with actual database query)
@login_required
def notifications_view(request):
    notifications = [
        Notification("Your profile was updated successfully.", "2024-12-29 14:30:00", read=True),
        Notification("You received a new message from a buyer.", "2024-12-30 10:15:00", read=False),
        Notification("Your product listing has been approved.", "2024-12-30 12:45:00", read=False),
    ]
    return render(request, 'notifications.html', {'notifications': notifications})

def product_list(request):
    # Fetch available products (adjust according to your model)
    available_products = Product.objects.all()  # Modify according to your model query
    return render(request, 'product_list.html', {'available_products': available_products})

def add_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your discussion has been added successfully!")
            return redirect('community-forum')  # Redirect to forum or appropriate page
    else:
        form = AddPostForm()
    
    return render(request, 'add_post.html', {'form': form})


def add_event(request):
    if request.method == "POST":
        form = AddEventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your event has been added successfully!")
            return redirect('community-forum')  # Redirect to forum or appropriate page
    else:
        form = AddEventForm()
    
    return render(request, 'add_event.html', {'form': form})


def add_feedback(request):
    if request.method == "POST":
        form = AddFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your feedback has been submitted successfully!")
            return redirect('feedback_success')  
    else:
        form = AddFeedbackForm()
    
    return render(request, 'add_feedback.html', {'form': form})

def addfeedback(request):
    return render(request, 'feedback_success.html')


def submit_product(request):
    if request.method == "POST":
        product_name = request.POST.get("product-name")
        product_description = request.POST.get("product-description")
        product_price = request.POST.get("product-price")
        product_image = request.POST.get("product-image")
        
        # Save the product data to the database
        product = Product.objects.create(
            name = product_name,
            description = product_description,
            price = product_price,
            image_url = product_image
        )
        
        return redirect('success_page')  # Redirect to a success page or another view
    
    return render(request, 'product_list.html')


def success_page(request):
    return render(request, 'success_page.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


