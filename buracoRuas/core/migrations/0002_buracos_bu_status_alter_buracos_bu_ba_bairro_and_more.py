# Generated by Django 4.1.2 on 2022-11-04 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buracos',
            name='bu_status',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='buracos',
            name='bu_ba_bairro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.bairros'),
        ),
        migrations.AlterField(
            model_name='buracos',
            name='bu_ru_rua',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.ruas'),
        ),
        migrations.AlterField(
            model_name='buracos',
            name='bu_situ_situacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.situacoes'),
        ),
    ]
