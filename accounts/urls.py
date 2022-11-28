from django.urls import path, include
from . import views
app_name = "accounts"
urlpatterns = [
    path("Studentlogin/", views.Studentlogin, name="Studentlogin"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
]
