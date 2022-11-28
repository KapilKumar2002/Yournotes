from django.urls import path, include
from . import views
app_name = "notes"
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("contact-us/", views.contact, name="contact"),
]
