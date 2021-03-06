# Generated by Django 2.2 on 2019-10-06 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='name',
            field=models.CharField(max_length=100, verbose_name='品名'),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='quantity',
            field=models.IntegerField(verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='ship_from',
            field=models.CharField(max_length=100, verbose_name='配送元'),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='ship_to',
            field=models.CharField(max_length=100, verbose_name='配送先'),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='staff',
            field=models.CharField(max_length=100, verbose_name='担当者'),
        ),
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.CharField(max_length=100, verbose_name='カテゴリー'),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=100, verbose_name='品名'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=100, verbose_name='名前'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='base',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='logistics.Base', verbose_name='拠点'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='賞味期限'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.Food', verbose_name='品名'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(verbose_name='数量'),
        ),
        migrations.CreateModel(
            name='StaffSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100, verbose_name='タスク')),
                ('start', models.DateTimeField(verbose_name='開始日時')),
                ('end', models.DateTimeField(verbose_name='終了日時')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.Staff', verbose_name='名前')),
            ],
        ),
    ]
