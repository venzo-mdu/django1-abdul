# Generated by Django 3.2.5 on 2022-05-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20220520_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio_data',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]