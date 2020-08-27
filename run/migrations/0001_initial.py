# Generated by Django 3.0.3 on 2020-05-26 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RunInfo',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('run_mile', models.FloatField()),
                ('run_time', models.DateTimeField()),
                ('created_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('rank', models.IntegerField()),
                ('total_mile', models.FloatField(default=0.0)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('group_id', models.IntegerField()),
                ('join_time', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='run.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='GroupInfo',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=32, unique=True)),
                ('group_number', models.IntegerField()),
                ('group_intro', models.CharField(max_length=1000, null=True)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('cap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cap_id', to='run.UserInfo')),
            ],
        ),
    ]