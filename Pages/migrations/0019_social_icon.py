# Generated by Django 5.1 on 2024-08-31 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0018_member_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
