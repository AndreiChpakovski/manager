# Generated by Django 5.0.6 on 2024-05-25 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Name of the homework')),
                ('is_complete', models.BooleanField(default=False, verbose_name='Finished homework')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
