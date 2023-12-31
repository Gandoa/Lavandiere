# Generated by Django 3.1.1 on 2023-07-26 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommandeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=200)),
                ('Numéro_de_Téléphone', models.IntegerField()),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Email', models.EmailField(max_length=200)),
                ('Services', models.BooleanField(default=False)),
                ('Code', models.IntegerField()),
                ('Commentaire', models.TextField(max_length=200)),
            ],
        ),
    ]
