from django.contrib import admin
from . import models

admin.site.register(models.Course)


class AdminResult(admin.ModelAdmin):
    list_display = ['student', 'exam', 'marks']
    readonly_fields = ['student', 'exam', 'code']


admin.site.register(models.Result, AdminResult)

admin.site.register(models.Question)
