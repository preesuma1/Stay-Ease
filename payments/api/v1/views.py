from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from payments.models import Payment
from .serializers import PaymentSerializer


class PaymentView(GenericAPIView):

    @extend_schema(tags=["Payments"])
    def get(self, request):
        return Response(PaymentSerializer(Payment.objects.all(), many=True).data)