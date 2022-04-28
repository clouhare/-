from django.db import models
from acc.models import User
# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sitename = models.CharField(max_length=100)
    site_url = models.TextField()
    comment = models.TextField()
    impo = models.BooleanField()

    def __str__(self):
        return self.sitename