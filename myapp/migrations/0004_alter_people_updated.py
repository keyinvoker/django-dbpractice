# Generated by Django 4.1 on 2022-08-30 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_alter_people_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="people",
            name="updated",
            field=models.BooleanField(default=False),
        ),
    ]
