# Generated by Django 3.2.7 on 2021-09-13 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Record', '0008_auto_20210914_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordformdata',
            name='district',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
