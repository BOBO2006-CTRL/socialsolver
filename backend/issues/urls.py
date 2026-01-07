from django.urls import path
from . import views

app_name = "issues"

urlpatterns = [
    path("", views.issue_list, name="issue_list"),
    path("create/", views.issue_create, name="issue_create"),
    path("<int:issue_id>/", views.issue_detail, name="issue_detail"),
    path("about/", views.about, name="about"),
]