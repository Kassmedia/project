import os
from django.core.files import File
import django
from contact.models import Farmer
from django.contrib.auth.models import User

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oja_agbe.settings")
django.setup()

# Image folder location
image_folder = os.path.join('C:', 'Users', 'OLABEL', 'Desktop', 'oja new', 'oja_agbe', 'media', 'farmer_images')

# Mapping of image filenames to usernames
image_mapping = {
    "a.png": "farmer1",
    "b.png": "olap",
    "c.png": "olapp",
    "d.png": "olabel",
    "e.png": "vico",
    "f.png": "omop",
    "g.png": "seun01",
}

# Farmer details (optional)
farmer_details = {
    "farmer1": {"name": "Farmer One", "bio": "A dedicated farmer", "rating": 5, "location": "Lagos"},
    "olap": {"name": "Olap", "bio": "Passionate about crops", "rating": 4, "location": "Ibadan"},
    "olapp": {"name": "Olapp", "bio": "Focused on poultry", "rating": 3, "location": "Abuja"},
    "olabel": {"name": "Olabel", "bio": "Advocate for organic farming", "rating": 4, "location": "Port Harcourt"},
    "vico": {"name": "Vico", "bio": "Specialized in irrigation systems", "rating": 5, "location": "Kaduna"},
    "omop": {"name": "Omop", "bio": "Grows vegetables and fruits", "rating": 3, "location": "Kano"},
    "seun01": {"name": "Seun", "bio": "Expert in sustainable agriculture", "rating": 4, "location": "Jos"},
}

# Iterate over the image mapping and update the Farmer profiles
for image_name, username in image_mapping.items():
    try:
        # Get the Farmer instance based on the username
        user = User.objects.get(username=username)
        farmer, created = Farmer.objects.get_or_create(user=user)

        # Set/update the farmer details (name, bio, rating, location)
        if username in farmer_details:
            details = farmer_details[username]
            farmer.name = details["name"]
            farmer.bio = details["bio"]
            farmer.rating = details["rating"]
            farmer.location = details["location"]

        # Check if the image is already uploaded in the database
        if not farmer.image:
            # Image path construction
            image_path = os.path.join(image_folder, image_name)
            print(f"Checking image path: {image_path}")  # To verify the correct path

            # Check if the image file exists and save it to the Farmer
            if os.path.exists(image_path):
                with open(image_path, "rb") as img_file:
                    farmer.image.save(image_name, File(img_file))
                    print(f"Uploaded image for Farmer: {username}")
            else:
                print(f"Image file not found for {username} at {image_path}")
                continue  # Skip this farmer if the image is not found
        else:
            print(f"Image already uploaded for Farmer: {username}")

        # Save the Farmer profile data
        farmer.save()

    except User.DoesNotExist:
        print(f"User with username {username} does not exist.")
    except Farmer.DoesNotExist:
        print(f"Farmer profile not found for username {username}")
    except Exception as e:
        print(f"Error processing farmer '{username}': {e}")
