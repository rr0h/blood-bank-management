# Blood Bank Management System

A comprehensive Django-based web application for managing blood bank operations, connecting donors with those in need.

## Features

### Core Functionality
- **Donor Management**: Register donors with complete profile information
- **Blood Inventory**: Track available blood units by type (A+, A-, B+, B-, AB+, AB-, O+, O-)
- **Blood Requests**: Submit and manage blood requests with urgency levels
- **Search System**: Find donors by blood type, name, email, or phone
- **User Authentication**: Secure login/registration system
- **Admin Dashboard**: Comprehensive admin panel for managing all operations

### Key Pages
- **Home**: Overview dashboard with statistics and recent requests
- **Donor Registration**: Easy-to-use form for new donors
- **Find Donors**: Search and filter available donors
- **Request Blood**: Submit blood requests with urgency levels
- **Inventory**: Real-time blood stock status
- **Admin Panel**: Full CRUD operations for all models

## Technology Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Frontend**: Bootstrap 5.3, Font Awesome 6.4
- **Deployment**: Gunicorn, Whitenoise for static files

## Installation

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/rr0h/blood-bank-management.git
cd blood-bank-management
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

7. Access the application:
- Website: http://localhost:8000
- Admin Panel: http://localhost:8000/admin

## Deployment

### Environment Variables

Create a `.env` file with:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### Production Deployment

The application is configured for deployment on:
- Railway
- Heroku
- Render
- Any platform supporting Django

Static files are handled by Whitenoise for production.

## Usage

### For Donors
1. Register as a donor with your details
2. Provide blood type, contact information, and availability
3. Update your profile when you donate

### For Recipients
1. Submit a blood request with patient details
2. Specify blood type, units needed, and urgency
3. Track request status

### For Administrators
1. Access admin panel at `/admin`
2. Manage donors, inventory, and requests
3. Update blood stock levels
4. Approve/reject blood requests

## Models

### Donor
- Full name, email, phone, address
- Blood type, age
- Last donation date
- Availability status

### BloodInventory
- Blood type
- Units available
- Last updated timestamp

### BloodRequest
- Patient information
- Blood type and units needed
- Hospital details
- Urgency level (low, medium, high, critical)
- Status (pending, approved, fulfilled, rejected)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Contact

For questions or support, please open an issue on GitHub.

---

**Saving Lives Together** 🩸
