from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from vote.models import Subject, Teacher, to_md5_hex, User, USERNAME_PATTERN


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'create_date', 'is_hot')
    ordering = ('no', )


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'detail', 'good_count', 'bad_count', 'subject')
    ordering = ('subject', 'no')





admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)