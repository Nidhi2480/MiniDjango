from django.db import models

# Create your models here.
class reviews(models.Model):
    name=models.CharField(max_length=100)
    specs=models.CharField(max_length=1500)
    image=models.ImageField(upload_to='pics')

    def __str__(self) -> str:
        return self.name