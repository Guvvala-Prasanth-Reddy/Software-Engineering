# Generated by Django 2.2.10 on 2020-05-12 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20200428_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content',
            field=models.FileField(upload_to=''),
        ),
    ]