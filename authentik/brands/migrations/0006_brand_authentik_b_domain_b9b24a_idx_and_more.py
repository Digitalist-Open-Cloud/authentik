# Generated by Django 5.0.4 on 2024-04-18 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_brands", "0005_tenantuuid_to_branduuid"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="brand",
            index=models.Index(fields=["domain"], name="authentik_b_domain_b9b24a_idx"),
        ),
        migrations.AddIndex(
            model_name="brand",
            index=models.Index(fields=["default"], name="authentik_b_default_3ccf12_idx"),
        ),
    ]