# Generated by Django 2.2.7 on 2019-11-24 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0002_agent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('sub', models.CharField(max_length=225)),
                ('msg', models.CharField(max_length=600)),
            ],
        ),
    ]
