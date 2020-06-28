# Generated by Django 3.0.7 on 2020-06-27 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('enrollment', models.IntegerField()),
                ('emailId', models.EmailField(max_length=50)),
                ('subjects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Subjects')),
            ],
        ),
    ]
