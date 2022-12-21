from django.contrib import admin
from django.urls import path, include

from data import views, htmx

urlpatterns = [
    path("data/Result/", views.ResultListView.as_view(), name="data_Result_list"),
    path("data/Result/create/", views.ResultCreateView.as_view(), name="data_Result_create"),
    path("data/Result/detail/<int:pk>/", views.ResultDetailView.as_view(), name="data_Result_detail"),
    path("data/Result/update/<int:pk>/", views.ResultUpdateView.as_view(), name="data_Result_update"),
    path("data/Result/delete/<int:pk>/", views.ResultDeleteView.as_view(), name="data_Result_delete"),

    path("data/htmx/Result/", htmx.HTMXResultListView.as_view(), name="data_Result_htmx_list"),
    path("data/htmx/Result/create/", htmx.HTMXResultCreateView.as_view(), name="data_Result_htmx_create"),
    path("data/htmx/Result/delete/<int:pk>/", htmx.HTMXResultDeleteView.as_view(), name="data_Result_htmx_delete"),
]
