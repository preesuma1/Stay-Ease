from rest_framework import serializers
from reviews.models import PropertyReview,UserReview


class PropertyReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyReview
        fields = "__all__"

class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = "__all__"