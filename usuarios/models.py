from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    celular = models.CharField(max_length=10)
    saldo = models.DecimalField(default=0)

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)