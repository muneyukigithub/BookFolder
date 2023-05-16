from django.db import models
from datetime import datetime
# Create your models here.

class Book(models.Model):
    title = models.CharField(verbose_name="タイトル",max_length=200)
    text = models.TextField(verbose_name="本文",max_length=500)
    date = models.DateField(verbose_name="日付",default=datetime.now)
    image = models.ImageField(verbose_name="本のイメージ",upload_to='img/')

    def __str__(self):
        return self.title