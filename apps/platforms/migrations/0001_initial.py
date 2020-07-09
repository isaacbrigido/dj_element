# Generated by Django 3.0.8 on 2020-07-09 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=80, verbose_name='Slug')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='platforms', to='companies.Company', verbose_name='Empresa')),
            ],
            options={
                'verbose_name': 'Plataforma',
                'verbose_name_plural': 'Plataformas',
                'ordering': ['-created_at'],
            },
        ),
    ]