# Society Connect

## Description:
 Society Connect is a Django-based web application designed to simplify residential society management through features like admin approval workflow, CAPTCHA-based authentication, email notifications, complaint management, notices, events, services, maintenance modules, and an analytical dashboard for complaint tracking.

## Features:
- Admin Approval Workflow
- CAPTCHA-based Login System
- Email Notification System
- Complaint Management Module
- Notice & Event Management
- Maintenance Tracking
- Society Services Module
- Complaint Analytics Dashboard
- Role-based Access

## Tech Stack:

- Python
- Django
- SQLite / MySQL
- HTML
- CSS
- JavaScript
- Bootstrap

## Screenshots:

## Landing Page

### Homepage
![Landing Page](screenshots/Landing_Page.PNG)

## User Panel

### User Login
![User Login](screenshots/User_Login.PNG)

### User Registration Request
![User Registration request](screenshots/User_Login_Request.PNG)

### User Complaint Module
![User Complaint](screenshots/User_Complaint.PNG)

### User Maintenance Module
![User Maintenance](screenshots/User_Maintenance.PNG)

### User Maintenance Payment
![User Maintenance 2](screenshots/User_Maintenance2.PNG)

### User Notices & Updates
![User Notice](screenshots/User_Notice.PNG)

## Admin Panel

### Admin Login
![Admin Login](screenshots/Admin_Login.PNG)

### Complaint Management
![Admin Complaint](screenshots/Admin_Complaint.PNG)

### Complaint Dashboard
![Complaint Dashboard](screenshots/Admin_Dashboard.PNG)

### User Approval Workflow
![Admin Approval](screenshots/Admin_Approval.PNG)

### Notice Management
![Admin Notice](screenshots/Admin_Notice.PNG)

### Services Management
![Admin Service](screenshots/Admin_Service.PNG)

## Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/ShreyaRevanwar/Society_Connect.git
```

---

### 2. Navigate to Project Directory

```bash
cd Society_Connect
```

---

### 3. Create Virtual Environment

```bash
python -m venv myVenv
```

---

### 4. Activate Virtual Environment

### Windows

```bash
myVenv\Scripts\activate
```

---

### 5. Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

Enter:
- username
- email
- password

After creating the superuser, log in to the superadmin and update the account status from `Pending` to `Approved` for the required admin/user accounts.

---

## 8. Check Project for Errors

```bash
python manage.py check
```

---

## 9. Run Development Server

```bash
python manage.py runserver
```

---

## 10. Open in Browser

```txt
http://127.0.0.1:8000/
```

---

# Default Workflow

1. User submits registration request
2. Admin approves User accounts
3. Approved users can log into the system
4. Users can access complaint, notice, maintenance,rules and service modules