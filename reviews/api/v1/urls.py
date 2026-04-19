from django.urls import path
from reviews.api.v1.views import PropertyReviewView, UserReviewView

urlpatterns = [
    path("reviews/", PropertyReviewView.as_view(), name="review-list"),
    # path("reviews/", UserReviewView.as_view(), name="review-list"),
]