# Generated by Django 2.2.7 on 2020-05-14 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('apply_time', models.DateTimeField(blank=True, null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('max_num', models.IntegerField()),
                ('introduction', models.CharField(max_length=200)),
                ('act_status', models.IntegerField()),
                ('label1', models.CharField(blank=True, max_length=10, null=True)),
                ('label2', models.CharField(blank=True, max_length=10, null=True)),
                ('label3', models.CharField(blank=True, max_length=10, null=True)),
                ('label4', models.CharField(blank=True, max_length=10, null=True)),
                ('label5', models.CharField(blank=True, max_length=10, null=True)),
                ('img1', models.CharField(blank=True, max_length=16, null=True)),
                ('img2', models.CharField(blank=True, max_length=16, null=True)),
                ('img3', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'activity',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='用户名')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
            ],
            options={
                'managed': False,
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Discuss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('act_id', models.IntegerField()),
                ('post_time', models.DateTimeField()),
                ('content', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'discuss',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('email', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=32)),
                ('nickname', models.CharField(max_length=16)),
                ('status', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('label_vec', models.CharField(max_length=512)),
            ],
            options={
                'managed': False,
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('fav_user', models.ForeignKey(db_column='fav_user', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myapp.Users')),
            ],
            options={
                'managed': False,
                'db_table': 'favorite',
            },
        ),
        migrations.CreateModel(
            name='Participate',
            fields=[
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myapp.Users')),
                ('join_time', models.DateTimeField()),
                ('score', models.IntegerField()),
                ('comment', models.CharField(max_length=100)),
                ('comment_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'participate',
            },
        ),
    ]