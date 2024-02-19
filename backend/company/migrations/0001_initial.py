# Generated by Django 5.0.1 on 2024-01-22 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('contact', models.IntegerField()),
                ('reg_num', models.IntegerField(unique=True)),
                ('logo', models.ImageField(upload_to='')),
            ],
        ),
    ]
