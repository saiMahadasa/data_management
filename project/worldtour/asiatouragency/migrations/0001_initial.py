# Generated by Django 4.1 on 2024-09-05 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_country', models.CharField(max_length=64)),
                ('origin_country', models.CharField(max_length=64)),
                ('number_of_nights', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
