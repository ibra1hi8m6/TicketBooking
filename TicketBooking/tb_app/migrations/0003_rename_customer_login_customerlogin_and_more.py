# Generated by Django 4.1.3 on 2023-01-01 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tb_app', '0002_customer_login_customer_signup_delete_customer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer_Login',
            new_name='CustomerLogin',
        ),
        migrations.RenameModel(
            old_name='Customer_Signup',
            new_name='CustomerSignup',
        ),
    ]
