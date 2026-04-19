from django.urls import path
from properties.api.v1.views import PropertyView, PropertyDetailView

urlpatterns = [
    path("properties/", PropertyView.as_view()),
    path("properties/<int:id>/", PropertyDetailView.as_view()),
]