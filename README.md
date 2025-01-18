# Oja Agbe


Oja Agbe(Harvestify) is a Django-based platform designed to connect farmers with their local communities and customers thereby reducing the problem of middle-men using the digital space. The project combines a clean, intuitive front-end interface with a robust back-end to support farmer profiles, customer engagement, and local commerce, share information about their farming practices, and engage with customers interested in fresh, locally-sourced agricultural products.
---

## Table of Contents

- [Project Overview]
- [Features]
- [Technologies Used]
- [Setup Instructions]
- [Usage Guidelines]
- [Project Architecture]
- [Contributing]
- [License]

---

## Project Overview

Oja Agbe is designed to empower farmers by providing an online platform where they can:
- Create and manage profiles with details such as location, bio, and ratings.
- Showcase their work with images and descriptions.
- Connect with customers interested in fresh, locally-sourced agricultural produce.

---

## Features

- **User Authentication:** Farmers and customers can securely register, log in, and manage accounts.
- **Farmer Profiles:** Detailed farmer profiles featuring location, bio, rating, and profile pictures.
- **Dynamic Front-End:** A responsive user interface for seamless interaction.
- **Database Flexibility:** SQLite for development and PostgreSQL for production.
- **Media Support:** Farmers can upload profile pictures and other media files.

---

## Technologies Used

### Front-End
- **HTML5**
- **CSS3**
- **JavaScript**

### Back-End
- **Django** (Python Framework)

### Databases
- **SQLite** for development
- **PostgreSQL** for production

### Other
- **Django Signals:** Automates profile creation for users upon registration.
- **Django ORM:** Simplifies database interactions.

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Django 4.x
- SQLite (default for development) or PostgreSQL
- Node.js and npm (optional, if using advanced JavaScript tools)
- Git
- Virtualenv

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Kassmedia/project.git
   cd oja-agbe
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database:**
   - **For Development:** SQLite is used by default.
   - **For Production:** Update the `DATABASES` setting in `settings.py` to configure PostgreSQL.
     Example:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_database_name',
             'USER': 'your_database_user',
             'PASSWORD': 'your_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```
   - Apply migrations:
     ```bash
     python manage.py migrate
     ```

5. **Load Initial Data:**
   - Optionally preload data for testing:
     ```bash
     python manage.py loaddata initial_data.json
     ```

6. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application:**
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Usage Guidelines

1. **Farmer Registration:**
   - Farmers can register through the sign-up page and create detailed profiles.

2. **Image Uploads:**
   - Farmer profile pictures are stored in the `media/farmer_images` directory.

3. **Admin Features:**
   - Superusers can manage users and farmer profiles via the admin panel.
     ```bash
     python manage.py createsuperuser
     ```

4. **Testing:**
   - Run tests to verify functionality:
     ```bash
     python manage.py test
     ```

---

## Project Architecture

### Core Apps
- **Users:** Handles authentication and farmer/customer user models.
- **Contact:** Manages farmer profiles with fields like name, location, bio, rating, and image.

### Front-End
- **HTML/CSS/JavaScript:** Provides a responsive and user-friendly interface.

### Folder Structure
```
OjaAgbe/
│
├── media/                   # Media files for farmer images
│   └── farmer_images/       # Folder for farmer profile images
│
├── oja_agbe/                # Main Django project folder
│   ├── settings.py          # Django settings
│   ├── urls.py              # Project-level URL configuration
│
├── contact/                 # App managing farmer profiles
│   ├── models.py            # Farmer and related models
│   ├── views.py             # Views for farmer profiles
│   ├── admin.py             # Farmer admin interface
│
├── users/                   # App managing authentication
│   ├── models.py            # Custom user model (if needed)
│   ├── views.py             # Authentication views
│
└── README.md                # Project documentation
```

---

## Contributing

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## License

This project is licensed under the [ALX License](LICENSE).

---

Enjoy building with **Oja Agbe**! 🌾