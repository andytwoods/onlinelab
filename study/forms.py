from django import forms
from user.models import User
from . import models


class StudyForm(forms.ModelForm):
    class Meta:
        model = models.Study
        fields = [
            "status",
            "title",
            "software",
            "description",
            "researchers",
        ]

    def __init__(self, *args, **kwargs):
        super(StudyForm, self).__init__(*args, **kwargs)
        self.fields["researchers"].queryset = User.objects.all()

