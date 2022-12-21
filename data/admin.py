from django.contrib import admin
from django import forms

from . import models


class ResultAdminForm(forms.ModelForm):

    class Meta:
        model = models.Result
        fields = "__all__"


class ResultAdmin(admin.ModelAdmin):
    form = ResultAdminForm
    list_display = [
        "data",
    ]
    readonly_fields = [
        "data",
    ]


admin.site.register(models.Result, ResultAdmin)
