# Generated by Django 4.2.7 on 2024-05-19 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Onboarding', '0014_transactions_amount_transactions_wallet_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='age',
            new_name='tel',
        ),
        migrations.AddField(
            model_name='profile',
            name='bitcoin_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='etherum_address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]