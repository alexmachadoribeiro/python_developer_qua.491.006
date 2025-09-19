from django.db import models

# Create your models here.
class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)

    def __str__(self):
        return self.nome