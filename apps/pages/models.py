from django.db import models

from apps.platforms.models import Platform


class Page(models.Model):
    name = models.CharField('Nome da página', max_length=40)
    slug = models.SlugField('Slug', max_length=20)
    platform = models.ForeignKey(Platform, verbose_name='Plataforma', related_name='pages', on_delete=models.CASCADE)
    order = models.PositiveIntegerField('Ordem')
    main = models.BooleanField('Página principal', default=False)
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['order']

