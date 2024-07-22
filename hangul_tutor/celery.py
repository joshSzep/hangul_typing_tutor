import logging
import os
import time

import celery


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hangul_tutor.settings")

# Instantiate Celery once per Django start.
app = celery.Celery("hangul_tutor")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


logger = logging.getLogger(__name__)


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    logger.info("Starting debug task")
    time.sleep(5)
    logger.info("Debug task finished")
    logger.debug(f"Request: {self.request!r}")
