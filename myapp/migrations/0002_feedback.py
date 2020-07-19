# Generated by Django 2.0 on 2020-05-21 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('fbid', models.AutoField(primary_key=True, serialize=False)),
                ('provider', models.CharField(max_length=32)),
                ('opinion', models.CharField(max_length=256)),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'feedback',
                'managed': False,
            },
        ),
    ]
