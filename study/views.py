from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class StudyListView(generic.ListView):
    model = models.Study
    form_class = forms.StudyForm


class StudyCreateView(generic.CreateView):
    model = models.Study
    form_class = forms.StudyForm


class StudyDetailView(generic.DetailView):
    model = models.Study
    form_class = forms.StudyForm


class StudyUpdateView(generic.UpdateView):
    model = models.Study
    form_class = forms.StudyForm
    pk_url_kwarg = "pk"


class StudyDeleteView(generic.DeleteView):
    model = models.Study
    success_url = reverse_lazy("study_Study_list")
