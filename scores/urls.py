from django.urls import path
from . import views

app_name = "scores"

urlpatterns = [
    # Example route (you can add more as you go)
    path("", views.score_list, name="score_list"),
]
