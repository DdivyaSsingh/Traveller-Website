# Generated by Django 3.2.9 on 2021-12-03 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('course', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
