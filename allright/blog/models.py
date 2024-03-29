from datetime import datetime
from django.db import models


class Case(models.Model):
    titulo = models.CharField(
        max_length=255,
        verbose_name='Título',
    )
    introducao = models.TextField(
        verbose_name='Introdução',
        blank=True,
        null=True,
    )
    trabalho_executado = models.TextField(
        verbose_name='Trabalho executado',
    )
    imagem = models.ImageField(
        verbose_name='Mídia',
        upload_to='case/',
        null=True,
        blank=True,
    )
    data_publicacao = models.DateTimeField(
        verbose_name='Data de publicação',
        auto_now_add=True
    )
    
    def __str__(self):
        return self.titulo


class Post(Case):
    pass

class Depoimento(models.Model):
    autor=models.CharField(max_length=255)
    conteudo=models.TextField(
        verbose_name='Conteúdo'
    )
    case=models.ForeignKey(
        'Case',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.case} - Depoimento {self.autor}'


class CadastroHomePage(models.Model):
    nome=models.CharField(max_length=255, verbose_name='Nome')
    email=models.EmailField(max_length=255, verbose_name='E-mail')
    telefone=models.IntegerField(verbose_name='Telefone', null=True, blank=True)
    descricao=models.TextField(verbose_name='Descrição', null=True, blank=True)

    def __str__(self):
        return f'{self.nome} - {self.email}'
