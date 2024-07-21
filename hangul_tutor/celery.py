import logging
import os
import time

import celery
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hangul_tutor.settings")
app = celery.Celery("hangul_tutor")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


logger = logging.getLogger(__name__)


@app.task(bind=True)
def debug_task(self):
    logger.info("Starting debug task")
    time.sleep(5)
    logger.info("Debug task finished")
    logger.debug(f"Request: {self.request!r}")
