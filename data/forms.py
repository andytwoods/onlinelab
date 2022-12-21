from django import forms
from user.models import User
from study.models import Study
from . import models


class ResultForm(forms.ModelForm):
    class Meta:
        model = models.Result
        fields = [
            "data",
            "participant",
            "study",
        ]

    def __init__(self, *args, **kwargs):
        super(ResultForm, self).__init__(*args, **kwargs)
        self.fields["participant"].queryset = User.objects.all()
        self.fields["study"].queryset = Study.objects.all()

