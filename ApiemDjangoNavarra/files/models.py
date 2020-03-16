from django.db import models

# Create your models here.
class fileHistory(models.Model):
    name = models.CharField(max_length=30)
    id = models.AutoField(primary_key=True)
