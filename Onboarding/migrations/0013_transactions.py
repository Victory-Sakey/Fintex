# Generated by Django 4.2.7 on 2024-05-18 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Onboarding', '0012_profile_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Select_Balance_Type', models.CharField(choices=[('Total balance ($0.00)', 'Total balance ($0.00)')], max_length=50)),
                ('Select_Assets', models.CharField(choices=[('Bitcoin', 'Bitcoin'), ('Ethereum', 'Ethereum')], max_length=50)),
            ],
        ),
    ]