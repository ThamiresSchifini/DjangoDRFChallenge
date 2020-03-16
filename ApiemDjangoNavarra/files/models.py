from django.db import models

<<<<<<< HEAD
=======
# Create your models here.
>>>>>>> 01611cbef7d7db9c0e4f50dde6af17589b0f2e92
class fileHistory(models.Model):
    name = models.CharField(max_length=30)
    id = models.AutoField(primary_key=True)
