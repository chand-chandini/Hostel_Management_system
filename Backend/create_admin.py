import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hostelproject.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

# These will come from Render environment variables
username = os.environ.get('ADMIN_USERNAME', 'hostel')
email = os.environ.get('ADMIN_EMAIL', 'hostel123@gmail.com')
password = os.environ.get('ADMIN_PASSWORD', 'admin123')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"✅ Superuser '{username}' created successfully!")
else:
    print(f"ℹ️ Superuser '{username}' already exists.")
