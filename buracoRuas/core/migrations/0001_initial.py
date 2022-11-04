# Generated by Django 4.1.2 on 2022-11-04 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bairros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ba_bairro', models.CharField(max_length=255, verbose_name='Bairro')),
            ],
            options={
                'verbose_name_plural': 'Bairros',
            },
        ),
        migrations.CreateModel(
            name='ruas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ru_rua', models.CharField(max_length=255, verbose_name='Rua')),
            ],
            options={
                'verbose_name_plural': 'Ruas',
            },
        ),
        migrations.CreateModel(
            name='situacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situ_situacao', models.CharField(default='leve', max_length=255, verbose_name='Situacao')),
            ],
            options={
                'verbose_name_plural': 'Situações',
            },
        ),
        migrations.CreateModel(
            name='buracos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bu_ba_bairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.bairros')),
                ('bu_ru_rua', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ruas')),
                ('bu_situ_situacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.situacoes')),
            ],
            options={
                'verbose_name_plural': 'Buracos',
                'unique_together': {('bu_ru_rua', 'bu_ba_bairro', 'bu_situ_situacao')},
            },
        ),
    ]