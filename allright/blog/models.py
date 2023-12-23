from django.db import models

class Post(models.Model):
    titulo = models.CharField(
        max_length=255,
        verbose_name='Título'
    )
    conteudo = models.TextField(
        verbose_name='Conteúdo'
    )