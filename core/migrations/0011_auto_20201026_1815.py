# Generated by Django 3.1.2 on 2020-10-26 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20201026_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_id',
            field=models.CharField(default='FXta2wRp1vUkShS2', max_length=16),
        ),
    ]