from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comic(models.Model):
    # unique comic number
    comic_id = models.IntegerField(unique=True) 

    # comic view status
    viewed = models.BooleanField(default=False) 

class ComicView(models.Model):
    # foreign key to comic
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

    # foreign key to user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # date and time comic was viewed
    viewed_at = models.DateTimeField(auto_now_add=True)
