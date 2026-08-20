from django.apps import AppConfig


class DjangoCronConfig(AppConfig):
    name = "django_cron"
    verbose_name = "Django cron"

    # Keep the primary key type of this package independent from the project's
    # DEFAULT_AUTO_FIELD. Without this, every project using BigAutoField (the
    # Django default since 3.2) sees a permanently pending migration for a
    # package it does not own, and `makemigrations` tries to write that
    # migration into site-packages, where it is lost on the next image build.
    default_auto_field = "django.db.models.BigAutoField"
