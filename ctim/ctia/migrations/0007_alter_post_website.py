# Generated by Django 4.2.8 on 2024-01-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ctia", "0006_alter_post_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="website",
            field=models.URLField(max_length=1000, null=True),
        ),
    ]
