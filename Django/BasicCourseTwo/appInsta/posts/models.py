"""Post models"""

import profile
from django.db import models
from django.contrib.auth.models import User

from users.models import Profile

class Post(models.Model):
    """Post model.

    Args:
        user: foreign key (users)
        profile: foreign key (profile)
        title: post title
        photo: post photo
        created: post creation date
        modified: post modified date
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        """Returns title and username

        Returns:
            str: title
            str: username
        """
        return '{} by @{}'.format(self.title, self.user.username)

