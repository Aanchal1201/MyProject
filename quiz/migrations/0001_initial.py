# Generated by Django 3.1.6 on 2021-03-09 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('language', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('title', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Difficult', 'Difficult')], default='Easy', max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/Quiz/')),
                ('timeTaken', models.CharField(max_length=50)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('Language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.language')),
            ],
        ),
        migrations.CreateModel(
            name='UserScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_score', models.IntegerField()),
                ('total_score', models.IntegerField()),
                ('total_correct', models.IntegerField()),
                ('total_incorrect', models.IntegerField()),
                ('total_unanswered', models.IntegerField()),
                ('time_consume', models.CharField(max_length=50)),
                ('quiz_data', models.TextField()),
                ('played_date', models.DateTimeField(auto_now_add=True)),
                ('quizTitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.title')),
                ('quizUsername', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ques', models.CharField(max_length=200)),
                ('choice1', models.CharField(max_length=200)),
                ('choice2', models.CharField(max_length=200)),
                ('choice3', models.CharField(max_length=200)),
                ('choice4', models.CharField(max_length=200)),
                ('Ans', models.CharField(max_length=200)),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('modifiedDate', models.DateField(auto_now=True)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.title')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('stars', models.IntegerField()),
                ('review', models.TextField(blank=True, null=True)),
                ('quizTitle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.title')),
            ],
        ),
    ]
