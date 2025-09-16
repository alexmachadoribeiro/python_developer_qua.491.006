from django.db import models

# Create your models here.
class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    altura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    data_nascimento = models.DateField(null=False, blank=False)