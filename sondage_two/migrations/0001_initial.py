# Generated by Django 5.0.3 on 2024-04-02 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('options', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='SondageTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReponseTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reponse', models.JSONField(default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='sondage_two.questiontwo')),
            ],
        ),
        migrations.AddField(
            model_name='questiontwo',
            name='sondage',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='sondage_two.sondagetwo'),
        ),
    ]
