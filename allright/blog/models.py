from datetime import datetime
from django.db import models

class Post(models.Model):
    titulo = models.CharField(
        max_length=255,
        verbose_name='Título',
    )
    conteudo = models.TextField(
        verbose_name='Conteúdo',
    )
    midia = models.ImageField(
        verbose_name='Mídia',
        upload_to='media/',
        null=True,
        blank=True,
    )
    data_publicacao = models.DateTimeField(
        verbose_name='Data de publicação',
        auto_now_add=True
    )

class Case(Post):
    pass
