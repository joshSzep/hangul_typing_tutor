import os

import celery
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hangul_tutor.settings")
app = celery.Celery("hangul_tutor")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
