# Generated by Django 3.2 on 2021-04-23 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_category_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='date_created',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='quizresult',
            old_name='start_date',
            new_name='created',
        ),
    ]
