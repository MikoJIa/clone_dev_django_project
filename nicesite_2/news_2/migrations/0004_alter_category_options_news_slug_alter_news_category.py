# Generated by Django 4.2.5 on 2023-09-21 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_2', '0003_category_news_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(max_length=150, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news_2.category', verbose_name='Категории'),
        ),
    ]