# Generated by Django 3.1.6 on 2021-03-04 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='JoiningDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
