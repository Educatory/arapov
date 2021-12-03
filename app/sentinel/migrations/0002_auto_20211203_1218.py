# Generated by Django 3.1.9 on 2021-12-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentinel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbox',
            name='max_x',
            field=models.DecimalField(decimal_places=14, max_digits=22),
        ),
        migrations.AlterField(
            model_name='bbox',
            name='max_y',
            field=models.DecimalField(decimal_places=14, max_digits=22),
        ),
        migrations.AlterField(
            model_name='bbox',
            name='min_x',
            field=models.DecimalField(decimal_places=14, max_digits=22),
        ),
        migrations.AlterField(
            model_name='bbox',
            name='min_y',
            field=models.DecimalField(decimal_places=14, max_digits=22),
        ),
        migrations.AlterField(
            model_name='bboximage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='bbox_img'),
        ),
    ]
