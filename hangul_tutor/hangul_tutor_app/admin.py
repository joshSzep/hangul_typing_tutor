from django.contrib import admin

from hangul_tutor.hangul_tutor_app import models


admin.site.register(
    [
        models.Question,
        models.Choice,
    ]
)
