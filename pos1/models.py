# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    idcurso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='idCurso', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aluno'


class AlunoDisciplina(models.Model):
    idaluno = models.OneToOneField(Aluno, models.DO_NOTHING, db_column='idAluno', primary_key=True)  # Field name made lowercase.
    iddisciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='idDisciplina')  # Field name made lowercase.
    semestre = models.CharField(max_length=6)
    situacao = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aluno_disciplina'
        unique_together = (('idaluno', 'iddisciplina', 'semestre'),)


class Curso(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso'


class CursoDisciplina(models.Model):
    idcurso = models.OneToOneField(Curso, models.DO_NOTHING, db_column='idCurso', primary_key=True)  # Field name made lowercase.
    iddisciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='idDisciplina')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'curso_disciplina'
        unique_together = (('idcurso', 'iddisciplina'),)


class Disciplina(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplina'
