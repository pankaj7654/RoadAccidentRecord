from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=100 )
    password = models.CharField(max_length=500)
    phone = models.CharField(max_length=10, unique = True)
    active = models.BooleanField(default=True)


# return user name in admin panel
    def __str__(self):
        return self.name

