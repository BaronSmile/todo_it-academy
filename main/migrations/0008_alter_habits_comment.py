# Generated by Django 3.2.9 on 2021-11-11 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_user_name_habits_habits_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habits',
            name='comment',
            field=models.TextField(),
        ),
    ]
