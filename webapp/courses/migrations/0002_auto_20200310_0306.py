# Generated by Django 2.2.10 on 2020-03-10 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='content',
            name='course_code',
            field=models.CharField(max_length=10),
        ),
    ]
