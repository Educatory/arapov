# Generated by Django 3.1.9 on 2021-12-04 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sentinel', '0005_auto_20211204_0350'),
        ('oilpipline', '0008_auto_20211204_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='detection',
            name='bbox',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sentinel.bbox'),
        ),
    ]
