# Generated by Django 3.1.9 on 2021-12-03 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oilpipline', '0005_auto_20211203_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='detection',
            name='type',
            field=models.CharField(choices=[('warning', 'Предупреждение'), ('danger', 'Опасно')], default='warning', max_length=15, verbose_name='Тип'),
        ),
    ]
