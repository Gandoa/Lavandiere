# Generated by Django 3.1.1 on 2023-08-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230807_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
