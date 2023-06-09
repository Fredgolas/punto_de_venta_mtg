from django.db import models

def set_directory_path(instance, filename) -> str:
    return f'uploads/{instance.set}/{filename}'

# Create your models here.
class Card(models.Model):
    CONDITIONS = [
        ('NM', 'Near Mint'),
        ('PL', 'Played'),
        ('HP', 'Heavily Played')
    ]
    FOIL = [
        (False,'Non-Foil'),
        (True,'Foil')
    ]
    name = models.CharField(default='Plains', max_length=50)
    price = models.FloatField(default=0.05)
    quantity = models.IntegerField(default=0)
    types = models.CharField(default='Basic Land - Plains', max_length=50)
    set = models.CharField(max_length=4, default='DMU')
    collector_number = models.IntegerField(default=262)
    condition = models.CharField(choices=CONDITIONS, default='NM', max_length=2)
    finish = models.BooleanField(default=False, choices=FOIL)
    #img = models.ImageField(upload_to=set_directory_path)
    
    class Meta:
        ordering = ['name','price']

    def __str__(self):
        return self.name
    
