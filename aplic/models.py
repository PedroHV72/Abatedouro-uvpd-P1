from django.db import models


class Curso(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição', max_length=400)
    carga_horaria = models.IntegerField('Carga Horária')

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nome
