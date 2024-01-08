from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("rulerchecker/", include("rulerchecker.urls")),
    path("admin/", admin.site.urls)
]
