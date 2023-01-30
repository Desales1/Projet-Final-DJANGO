# Generated by Django 4.1.5 on 2023-01-30 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_mycategorie_categorie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='categorie',
        ),
        migrations.RemoveField(
            model_name='article',
            name='contenu',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='categorie',
            name='description',
        ),
        migrations.AddField(
            model_name='article',
            name='ancien_prix',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='prix',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categorie',
            name='nom',
            field=models.CharField(max_length=150),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]