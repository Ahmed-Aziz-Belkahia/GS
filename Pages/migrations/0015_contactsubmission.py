# Generated by Django 5.1 on 2024-08-24 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0014_client_contactinfo_faq_member_social'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]
