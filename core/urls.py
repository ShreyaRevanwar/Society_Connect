from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.continue_as, name="continue_as"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path("home/", views.home, name="home"),
    path("complaint_form/", views.complaint_form, name="complaint_form"),
    path("maintenance/", views.maintenance, name="maintenance"),
    path("payment-history/", views.payment_history, name="payment_history"),
    path("notice/", views.notice, name="notice"),
    path("rules_regulations/", views.rules_regulations, name="rules_regulations"),
    path("services/", views.services, name="services"),   
    path("profile/", views.profile, name="profile"),
    path("registration_success/", views.registration_success, name="registration_success"),
    path("test_email/", views.test_email, name="test_email"),




    # LOGOUT URL
    # path('resident_logout/',views.resident_logout,name='resident_logout'),

    path('create-order/', views.create_order, name='create_order'),

    # payment url
    path('save-payment/', views.save_payment, name='save_payment'),

    # CAPTCHA endpoints
    path('get-captcha/', views.get_captcha, name='get_captcha'),
    path('refresh-captcha/', views.refresh_captcha, name='refresh_captcha'),
]