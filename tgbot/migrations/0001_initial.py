# Generated by Django 4.1.7 on 2023-04-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.PositiveBigIntegerField(unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=128, null=True)),
            ],
        ),
    ]
