from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Coach)
admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.Lesson)
admin.site.register(models.BookedLesson)
admin.site.register(models.Review)