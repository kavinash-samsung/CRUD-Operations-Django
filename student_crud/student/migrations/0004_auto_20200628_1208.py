# Generated by Django 3.0.7 on 2020-06-28 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20200627_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enrollment',
            field=models.PositiveIntegerField(),
        ),
    ]
