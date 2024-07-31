from django.db import models

# Model of theme
class SiteSettings(models.Model):
    banner = models.ImageField(upload_to='media/site/')
    caption = models.TextField()