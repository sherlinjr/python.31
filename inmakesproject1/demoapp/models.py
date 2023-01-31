from django.db import models

# Create your models here.
class world(models.Model):
    name = models.CharField(max_length=180)
    img = models.ImageField(upload_to='pics',max_length=300*188)
    desc = models.TextField()


def __str__(self):
    return self.name