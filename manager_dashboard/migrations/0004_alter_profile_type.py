# Generated by Django 3.2.16 on 2023-02-02 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_dashboard', '0003_alter_profile_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.IntegerField(choices=[(3, 'Client'), (2, 'Employee'), (1, 'Manager')], default=3),
        ),
    ]
