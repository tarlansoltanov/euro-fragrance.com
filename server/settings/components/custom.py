# Custom Project Settings

from server.settings.components import BASE_DIR
from server.settings.components.common import INSTALLED_APPS, TEMPLATES

# Application definition

INSTALLED_APPS += [
    "server.apps.base",
    "server.apps.category",
    "server.apps.product",
]

# Context processors
# https://docs.djangoproject.com/en/5.0/ref/templates/api/#writing-your-own-context-processors

TEMPLATES[0]["OPTIONS"]["context_processors"] += [
    "server.apps.base.logic.processors.settings",
    "server.apps.category.logic.processors.categories",
]

# Static and media files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/topics/files/

STATICFILES_DIRS = [
    BASE_DIR.joinpath("static"),
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

# Modeltranslation
# https://django-modeltranslation.readthedocs.io/en/latest/

MODELTRANSLATION_TRANSLATION_FILES = [
    "server.apps.portfolio.logic.translation",
]
