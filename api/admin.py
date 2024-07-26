from django.contrib import admin

from . import models


admin.site.register(models.Challenge)
admin.site.register(models.ChallengeGroup)
admin.site.register(models.TypingSpeed)
