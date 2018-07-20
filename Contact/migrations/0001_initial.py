# Generated by Django 2.0.7 on 2018-07-12 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormSubmition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=250)),
                ('organization', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IndustryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='QueryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='formsubmition',
            name='industryrelation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Contact.IndustryType'),
        ),
        migrations.AddField(
            model_name='formsubmition',
            name='professionfield',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Contact.ProfessionField'),
        ),
        migrations.AddField(
            model_name='formsubmition',
            name='queryabout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Contact.QueryType'),
        ),
    ]
