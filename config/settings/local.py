from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="lQieUs9prtrwEN4cTEcjyr2whGnS1IuAW2e7XpFdgAabXLwzd1Rf8juTBcbnkIQf",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
default_hosts = ["localhost", "0.0.0.0", "127.0.0.1"]

# Pull ALLOWED_HOSTS from environment variable, fallback to default if not set
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=default_hosts)
CSRF_TRUSTED_ORIGINS = ["https://api.thompson.gr", "https://ctim.agentia.tech"]

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env("DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")

# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa: F405


# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa: F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
if env("USE_DOCKER") == "yes":
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa: F405

# Your stuff...
# ------------------------------------------------------------------------------

# Logging configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "sentry": {
            "level": "INFO",
            "class": "sentry_sdk.integrations.logging.EventHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
        "null": {
            "class": "logging.NullHandler",
        },
    },
    "loggers": {
        "": {  # root logger
            "handlers": ["console"],
            "level": "INFO",  # Set to 'INFO' in production
        },
        "django": {
            "handlers": ["console"],
            "level": "CRITICAL",
            "propagate": True,
        },
        "django.server": {
            "handlers": ["console"],
            "level": "CRITICAL",
            "propagate": True,
        },
        "oauth2_provider": {
            "handlers": ["sentry"],
            "level": "INFO",
            "propagate": True,
        },
        "debug_toolbar": {
            "handlers": ["null"],
            "level": "CRITICAL",  # Only log errors and critical issues
            "propagate": False,
        },
        "ctim.ctia.tasks": {
            "handlers": ["null"],  # set to null as the celeery handler picks it up
            "level": "DEBUG",
            "propagate": True,
        },
    },
}


# Celery
# ------------------------------------------------------------------------------
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-eager-propagates
CELERY_TASK_EAGER_PROPAGATES = True
