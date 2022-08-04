"""Posts models
"""

from pyexpat import model
from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    is_admin = models.BooleanField(default=False)
    
    bio = models.TextField()
    
    birthdate = models.DateField(blank=True, null=True)
    
    create = models.DateTimeField(auto_now_add=True)
    
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return email."""
        return self.email
