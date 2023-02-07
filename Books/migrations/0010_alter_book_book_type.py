# Generated by Django 4.1.1 on 2023-01-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0009_alter_rating_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_type',
            field=models.CharField(choices=[('e_book', 'e_book'), ('hard_book', 'hard_book')], max_length=250),
        ),
    ]
