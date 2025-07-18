# Generated by Django 5.2.3 on 2025-07-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('new', 'новая'), ('deleted', 'удаленная'), ('old', 'старое')], default='new', max_length=10, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата редактирования'),
        ),
    ]
