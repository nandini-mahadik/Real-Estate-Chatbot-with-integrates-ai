from django.urls import path
from .views import analyze, download_excel

urlpatterns = [
    path("analyze/", analyze, name="analyze"),
    path("download/", download_excel, name="download_excel"),
]
