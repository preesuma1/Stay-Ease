from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from reviews.models import PropertyReview,UserReview
from .serializers import PropertyReviewSerializer, UserReviewSerializer


class PropertyReviewView(GenericAPIView):

    @extend_schema(tags=["Reviews"])
    def get(self, request):
        return Response(PropertyReviewSerializer(PropertyReview.objects.all(), many=True).data)
    
class UserReviewView(GenericAPIView):

    @extend_schema(tags=["Reviews"])
    def get(self, request):
        return Response(UserReviewSerializer(UserReview.objects.all(), many=True).data)