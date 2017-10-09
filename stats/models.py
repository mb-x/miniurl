from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Page(models.Model):
    url = models.URLField()
    nb_visites = models.IntegerField(default=1)

    def __str__(self):
        return self.url

class Profil(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatars/")
    signature = models.TextField(blank=False)
    newsleter = models.BooleanField(default=False)

    def __str__(self):
        return "Profil de {0}".format(self.user.username)
