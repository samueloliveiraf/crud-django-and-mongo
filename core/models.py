from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=200, 
        verbose_name='Nome'
    )
    date = models.DateTimeField(
        auto_now=True, 
        verbose_name='Data criado'
    )
    image = models.ImageField(
        upload_to='products', 
        verbose_name='Imagem'
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.PROTECT
    )


    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        
        return url
