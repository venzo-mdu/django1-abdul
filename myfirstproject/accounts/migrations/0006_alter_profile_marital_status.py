# Generated by Django 3.2.5 on 2022-05-13 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20220512_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='marital_status',
            field=models.CharField(choices=[('single', 'single'), ('married', 'married')], default='1', max_length=20),
        ),
    ]