from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length = 200)
    mobilenumber = models.CharField(max_length=10)
    email = models.EmailField(max_length = 100)
    message = models.TextField()

    def __str__(self):
        return self.fullname + " " + self.message