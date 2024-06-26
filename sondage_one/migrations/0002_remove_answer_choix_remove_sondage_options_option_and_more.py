# Generated by Django 5.0.3 on 2024-03-27 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sondage_one', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='choix',
        ),
        migrations.RemoveField(
            model_name='sondage',
            name='options',
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('sondage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='sondage_one.sondage')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='choices',
            field=models.ManyToManyField(related_name='answers', to='sondage_one.option'),
        ),
    ]
