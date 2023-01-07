# Generated by Django 4.1.4 on 2023-01-03 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_page', '0003_delete_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=64)),
                ('destination', models.CharField(max_length=64)),
                ('nights', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
