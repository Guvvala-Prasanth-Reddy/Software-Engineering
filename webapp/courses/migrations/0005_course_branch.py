# Generated by Django 2.2.10 on 2020-04-26 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20200426_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Branch',
            field=models.CharField(default='CSE', max_length=4),
            preserve_default=False,
        ),
    ]
