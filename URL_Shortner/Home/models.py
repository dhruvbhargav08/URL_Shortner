from django.db import models

# Create your models here.
class ShortURL(models.Model):
    original_url=models.URLField(max_length=256)
    time_date_created=models.DateTimeField()
    shot_url=models.CharField(max_length=64)
    def __str__(self):
        return self.original_url