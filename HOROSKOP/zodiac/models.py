from django.db import models
from datetime import datetime


# Create your models here.
class Zodiac(models.Model):
    name = models.CharField(max_length=30)
    horoskop_data = models.CharField(max_length=300)
    now = datetime.now()
    date_publish_horoskop = now
