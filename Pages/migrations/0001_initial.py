# Generated by Django 5.1 on 2024-08-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url_title', models.SlugField()),
                ('image', models.ImageField(upload_to='service')),
            ],
        ),
    ]
