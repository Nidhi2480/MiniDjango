from django.db import models

# Create your models here.
class profile(models.Model):
    Name=models.CharField(max_length=30)
    img=models.ImageField(upload_to='pics')
    about=models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return self.Name