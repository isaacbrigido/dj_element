from django.db import models


class Company(models.Model):
    fantasy_name = models.CharField('Nome fantasia', max_length=150)
    social_name = models.CharField('Razão Social', max_length=180)
    cnpj = models.CharField('CNPJ', max_length=14)
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)

    def __str__(self):
        return self.fantasy_name

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['-created_at']
