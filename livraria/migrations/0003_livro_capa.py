# Generated by Django 4.2.3 on 2023-07-07 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('livraria', '0002_alter_autor_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='capa',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image'),
        ),
    ]