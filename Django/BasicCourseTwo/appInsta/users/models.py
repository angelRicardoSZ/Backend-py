
# Django



from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    """profile model
    Proxy model that extends the base data with other information
    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    website = models.URLField(max_length=200, blank=True)
    
    phone_number = models.CharField(max_length=20, blank=True)
    
    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    
    created = models.DateTimeField(auto_now=True)
    
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """return username
        """
        return self.user.username
        