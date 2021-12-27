# Generated by Django 3.2.8 on 2021-12-27 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='insect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/travel')),
            ],
        ),
        migrations.AlterField(
            model_name='bird',
            name='image',
            field=models.ImageField(upload_to='images/bird'),
        ),
        migrations.AlterField(
            model_name='nature',
            name='image',
            field=models.ImageField(upload_to='images/nature'),
        ),
        migrations.AlterField(
            model_name='reptile',
            name='image',
            field=models.ImageField(upload_to='images/reptile'),
        ),
    ]
