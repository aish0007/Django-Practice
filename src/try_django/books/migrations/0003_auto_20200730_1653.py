# Generated by Django 2.1.5 on 2020-07-30 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_books_summary1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]