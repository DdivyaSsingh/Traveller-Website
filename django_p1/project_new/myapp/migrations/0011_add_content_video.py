# Generated by Django 3.2.9 on 2021-12-23 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('myapp', '0010_doctor_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_content_video',
            fields=[
                ('title', models.CharField(max_length=30)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('content', models.ImageField(upload_to='my_data')),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
