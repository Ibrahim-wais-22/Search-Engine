# Generated by Django 3.2 on 2021-10-06 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchEngine', '0002_auto_20210917_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
