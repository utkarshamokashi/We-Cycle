from django.db import models

# Create your models here.
class Ngolist(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')
    address = models.TextField()
    city = models.CharField(max_length=50)
    datetime = datetime = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name