# Brings back the migration that matches BigAutoField primary keys (see apps.py).
# The name is kept exactly as django's autodetector generates it, so databases
# that already applied it under a previous fork stay consistent.
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_cron", "0004_alter_cronjoblog_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cronjoblock",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="cronjoblog",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
