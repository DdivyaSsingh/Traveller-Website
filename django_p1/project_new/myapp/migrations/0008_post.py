# Generated by Django 3.2.9 on 2021-12-16 17:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', ckeditor.fields.RichTextField()),
                ('title', ckeditor.fields.RichTextField()),
                ('desc', ckeditor.fields.RichTextField()),
            ],
        ),
    ]