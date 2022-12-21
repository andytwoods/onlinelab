from django.urls import path, include


from . import views
from . import htmx


urlpatterns = (
    path("study/Study/", views.StudyListView.as_view(), name="study_Study_list"),
    path("study/Study/create/", views.StudyCreateView.as_view(), name="study_Study_create"),
    path("study/Study/detail/<int:pk>/", views.StudyDetailView.as_view(), name="study_Study_detail"),
    path("study/Study/update/<int:pk>/", views.StudyUpdateView.as_view(), name="study_Study_update"),
    path("study/Study/delete/<int:pk>/", views.StudyDeleteView.as_view(), name="study_Study_delete"),

    path("study/htmx/Study/", htmx.HTMXStudyListView.as_view(), name="study_Study_htmx_list"),
    path("study/htmx/Study/create/", htmx.HTMXStudyCreateView.as_view(), name="study_Study_htmx_create"),
    path("study/htmx/Study/delete/<int:pk>/", htmx.HTMXStudyDeleteView.as_view(), name="study_Study_htmx_delete"),
)
