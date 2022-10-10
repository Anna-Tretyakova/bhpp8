# Generated by Django 4.1.1 on 2022-10-10 17:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, verbose_name='имя')),
                ('email', models.EmailField(max_length=254, verbose_name='почта')),
                ('phone_number', models.CharField(max_length=13, verbose_name='номер телефона')),
                ('message', models.CharField(max_length=140, verbose_name='сообщение')),
                ('date_created', models.DateTimeField(default=datetime.datetime(2022, 10, 10, 17, 13, 21, 43795, tzinfo=datetime.timezone.utc), verbose_name='дата публикации')),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'отзывы',
                'db_table': 'app_feedbacks',
                'ordering': ('date_created',),
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 10, 17, 13, 21, 42797), verbose_name='дата'),
        ),
    ]
