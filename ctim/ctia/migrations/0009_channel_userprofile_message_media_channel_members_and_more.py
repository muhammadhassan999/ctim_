# Generated by Django 4.2.8 on 2024-01-08 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ctia", "0008_alter_location_updated"),
    ]

    operations = [
        migrations.CreateModel(
            name="Channel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("url", models.URLField()),
                ("source_urls", models.TextField(help_text="Comma-separated list of source URLs")),
                ("metadata", models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("username", models.CharField(max_length=255)),
                ("first_name", models.CharField(blank=True, max_length=255, null=True)),
                ("last_name", models.CharField(blank=True, max_length=255, null=True)),
                ("phone_number", models.CharField(blank=True, max_length=50, null=True)),
                ("user_id", models.BigIntegerField()),
                ("bio", models.TextField(blank=True, null=True)),
                ("online_status", models.CharField(max_length=100)),
                ("profile_picture", models.ImageField(blank=True, null=True, upload_to="profile_pics/")),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("content", models.TextField()),
                ("date_posted", models.DateTimeField()),
                ("views", models.IntegerField(blank=True, null=True)),
                ("message_url", models.URLField()),
                (
                    "channel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="messages", to="ctia.channel"
                    ),
                ),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="ctia.userprofile")),
            ],
        ),
        migrations.CreateModel(
            name="Media",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("media_file", models.FileField(upload_to="message_media/")),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="media", to="ctia.message"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="channel",
            name="members",
            field=models.ManyToManyField(related_name="channels", to="ctia.userprofile"),
        ),
        migrations.CreateModel(
            name="Adjacency",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "source_channel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="forwarded_from", to="ctia.channel"
                    ),
                ),
                (
                    "target_channel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="forwarded_to", to="ctia.channel"
                    ),
                ),
            ],
        ),
    ]
