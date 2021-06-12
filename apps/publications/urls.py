from django.urls import path

from .views import PublicationDetail, PublicationList

app_name = "publications"

urlpatterns = [
    path("", PublicationList.as_view(), name="publication-list"),
    path("<int:pk>", PublicationDetail.as_view(), name="publication-list"),
]
