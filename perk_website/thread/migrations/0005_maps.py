# Generated by Django 5.1 on 2024-08-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0004_alter_contact_lname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_name', models.CharField(max_length=100)),
                ('wonder_weapon', models.CharField(max_length=100)),
                ('easter_egg', models.CharField(max_length=10)),
                ('video_guide', models.ImageField(upload_to='')),
            ],
        ),
    ]
