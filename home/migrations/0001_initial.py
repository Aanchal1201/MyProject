# Generated by Django 3.1.6 on 2021-02-27 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('desc', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
