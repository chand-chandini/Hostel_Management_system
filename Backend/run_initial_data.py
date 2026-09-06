# run_initial_data.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hostelproject.settings')
django.setup()

# Import your script
import load_room_data_fixed

print("✅ Initial data loaded successfully!")
