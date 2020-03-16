from django.db import models

class fileHistory(models.Model):
    name = models.CharField(max_length=30)
    id = models.AutoField(primary_key=True)
