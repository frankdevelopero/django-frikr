# Generated by Django 2.1.3 on 2018-11-12 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('url', models.URLField()),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('licence', models.CharField(choices=[('RIG', 'Copyright'), ('LEF', 'Copyleft'), ('CC', 'Creative Commons')], max_length=3)),
            ],
        ),
    ]
