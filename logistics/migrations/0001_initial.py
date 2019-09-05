# Generated by Django 2.2 on 2019-09-05 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('name_ja', models.CharField(max_length=100, unique=True)),
                ('name_en', models.CharField(max_length=100, unique=True)),
                ('no', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, upload_to='base_image')),
            ],
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_from', models.CharField(max_length=100)),
                ('ship_to', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('staff', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('base', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='logistics.Base')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.Food')),
            ],
        ),
    ]
