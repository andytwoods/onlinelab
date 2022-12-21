from django.contrib import admin
from django import forms

from . import models


class StudyAdminForm(forms.ModelForm):

    class Meta:
        model = models.Study
        fields = "__all__"


class StudyAdmin(admin.ModelAdmin):
    form = StudyAdminForm
    list_display = [
        "status",
        "title",
        "software",
        "description",
        "uuid",
    ]
    readonly_fields = [
        "status",
        "title",
        "software",
        "description",
        "uuid",
    ]


admin.site.register(models.Study, StudyAdmin)
