from django.urls import path
from users.api.v1.views import UserProfileView, UserProfileDetailView

urlpatterns = [
    path("profiles/", UserProfileView.as_view()),
    path("profiles/<int:id>/", UserProfileDetailView.as_view()),
]