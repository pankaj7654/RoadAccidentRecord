# Generated by Django 3.2.7 on 2021-09-04 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Record', '0002_user_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
