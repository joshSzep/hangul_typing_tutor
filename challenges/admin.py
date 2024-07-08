from django.contrib import admin

from .models import Challenge, ChallengeResult, Sentence

admin.site.register(Sentence)
admin.site.register(Challenge)
admin.site.register(ChallengeResult)
