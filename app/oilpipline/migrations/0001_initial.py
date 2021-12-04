# Generated by Django 3.1.9 on 2021-12-03 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OilPipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('coords', models.JSONField(verbose_name='Координаты')),
            ],
            options={
                'verbose_name': 'Нефтепровод',
                'verbose_name_plural': 'Нефтепроводы',
                'ordering': ['name'],
            },
        ),
    ]
