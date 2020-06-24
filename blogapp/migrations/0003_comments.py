# Generated by Django 3.0.7 on 2020-06-21 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_post_postid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('username', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]