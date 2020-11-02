from django.db import models

# Create your models here.

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplina'
