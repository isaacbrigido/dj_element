from django.db import models

from apps.companies.models import Company


class Platform(models.Model):
    company = models.ForeignKey(Company, verbose_name='Empresa', related_name='platforms',
                                on_delete=models.CASCADE)
    slug = models.SlugField('Slug', max_length=80)
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Plataforma'
        verbose_name_plural = 'Plataformas'
        ordering = ['-created_at']
