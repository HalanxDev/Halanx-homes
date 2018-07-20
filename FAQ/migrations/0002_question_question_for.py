# Generated by Django 2.0.7 on 2018-07-20 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FAQ', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_for',
            field=models.CharField(blank=True, choices=[('Owner', 'Owner'), ('Tenant', 'Tenant'), ('Other', 'Other')], max_length=25, null=True),
        ),
    ]
