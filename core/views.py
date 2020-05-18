from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import haversine


class IndexView(TemplateView):
    template_name = "core/form.html"


class CalculateDistanceView(APIView):
    def post(self, request, *args, **kwargs):
        a = request.data["a"]
        b = request.data["b"]
        distance = haversine(a, b)
        distance = round(distance, 3)
        data = {
            "a": a,
            "b": b,
            "distance": distance,
        }
        return Response(data)
