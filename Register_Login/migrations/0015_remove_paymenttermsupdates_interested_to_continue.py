# Generated by Django 4.2 on 2024-01-24 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0014_previouspaymentterms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymenttermsupdates',
            name='interested_to_continue',
        ),
    ]
