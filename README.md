# 🏠 Hostel Management System

A full-stack web application for managing university hostel operations, including student registration, room allocation, fee management, and administrative controls.

## 🚀 Live Demo

| Service | URL |
|---------|-----|
| **Frontend (React)** | [https://hostel-frontend-84d3.onrender.com](https://hostel-frontend-84d3.onrender.com) |
| **Backend API (Django)** | [https://hostel-management-system-1-up0y.onrender.com](https://hostel-management-system-1-up0y.onrender.com) |
| **Admin Panel** | [https://hostel-management-system-1-up0y.onrender.com/admin/](https://hostel-management-system-1-up0y.onrender.com/admin/) |

## 📋 Features

- **Student Registration & Authentication** (JWT-based)
- **Room Allocation System** with block, floor, and room management
- **Payment Integration** (Razorpay)
- **Admin Dashboard** for managing students, rooms, and allocations
- **Email Notifications** for room allotment
- **PDF Generation** for allotment letters
- **Responsive React Frontend** with Tailwind CSS

## 🛠️ Tech Stack

### Frontend
- **React.js** with Vite
- **Tailwind CSS** for styling
- **Axios** for API calls
- **React Router** for navigation

### Backend
- **Django** & **Django REST Framework**
- **PostgreSQL** database
- **JWT Authentication** (Simple JWT)
- **Razorpay** payment gateway
- **ReportLab** for PDF generation

## 🗄️ Database Schema

The system includes:
- **Blocks** (Orange, Meta, Alumini hostels)
- **Floors** with room counts
- **Rooms** with capacity and pricing
- **Students** with registration details
- **Applications** for hostel admission
- **Payments** tracking

## 📦 Installation

### Prerequisites
- Python 3.13+
- Node.js 18+
- PostgreSQL

### Backend Setup

cd Backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 

### Frontend Setup
cd Frontend/hostel
npm install
npm run dev

### Env setup
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=postgresql://user:password@host:port/database
RAZORPAY_KEY_ID=your-razorpay-key
RAZORPAY_KEY_SECRET=your-razorpay-secret
EMAIL_HOST_PASSWORD=your-email-password

### Fronrend (env)
VITE_API_URL=https://hostel-management-system-1-up0y.onrender.com/api/
VITE_RAZORPAY_KEY_ID=your-razorpay-key

Backend (Render)
Root Directory: Backend

Build Command: pip install -r requirements.txt && python manage.py migrate && python create_admin.py && python manage.py collectstatic --noinput

Start Command: gunicorn hostelproject.wsgi:application


Frontend (Render)
Root Directory: Frontend/hostel

Build Command: npm install && npm run build

Publish Directory: dist

Redirects: Add _redirects file with /* /index.html 200
