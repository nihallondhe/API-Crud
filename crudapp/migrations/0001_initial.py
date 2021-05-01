# Generated by Django 3.1.6 on 2021-05-01 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Empid', models.IntegerField(primary_key=True, serialize=False)),
                ('Empname', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Salary', models.IntegerField(max_length=6)),
            ],
            options={
                'db_table': 'EmployeeTable',
            },
        ),
    ]