from __future__ import absolute_import, unicode_literals

# Import Celery application to make it accessible
from .celery import app as celery_app

__all__ = ('celery_app',)