# Generated by Django 5.1.1 on 2024-09-16 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_author_category_customer_publisher_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
    ]
