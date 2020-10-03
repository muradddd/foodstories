# Generated by Django 3.1.2 on 2020-10-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_dscrp', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=1000)),
                ('choice', models.CharField(choices=[(1, 'first'), (2, 'second')], default=1, max_length=50)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]