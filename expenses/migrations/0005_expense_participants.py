# Generated by Django 5.1.1 on 2024-09-29 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_expense_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='participants',
            field=models.ManyToManyField(related_name='expenses_participated', to='expenses.member'),
        ),
    ]
