# Generated by Django 5.0.6 on 2024-05-23 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Help', '0004_alter_user_department_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='patronymic',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
