from django.db import models


# Create your models here.


class BlogPost(models.Model):
    """A post the user made on his blog."""
    title = models.CharField(max_length=80)
    text = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
