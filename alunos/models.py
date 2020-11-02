from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    idcurso = models.CharField(max_length=100, blank=True, null=True, db_column='idCurso')  # Field 

    class Meta:
        managed = False
        db_table = 'aluno'


class AlunoDisciplina(models.Model):
    idaluno = models.OneToOneField(Aluno, models.DO_NOTHING, db_column='idAluno', primary_key=True)  # Field name made lowercase.
    iddisciplina = models.CharField(max_length=100, blank=True, null=True, db_column='idDisciplina')  # Field name made lowercase.
    semestre = models.CharField(max_length=6)
    situacao = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aluno_disciplina'
        unique_together = (('idaluno', 'iddisciplina', 'semestre'),)