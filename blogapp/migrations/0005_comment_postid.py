# Generated by Django 3.0.7 on 2020-06-21 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20200621_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='postid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]