from django.db import models

class destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    #desc = models.TextField()
    price = models.IntegerField()
    offer = models.BinaryField(default=False)


