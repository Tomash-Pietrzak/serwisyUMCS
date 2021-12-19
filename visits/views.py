import requests
import json
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from visits.serializers import VisitSerializer
from .models import Visit


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

    @action(detail=True, methods=['post'])
    def register(self, request, pk):
        obj = self.get_object()
        obj.patient = request.user
        obj.save()
        return Response(status=201)

    @action(detail=True, methods=['get'])
    def get_visit_price(self, request, pk):
        obj = self.get_object()
        r = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/eur/')
        r_json = json.dumps(r.json())
        rate_eur = json.loads(r_json)["rates"][0]["mid"]
        price_eur = obj.price / rate_eur
        obj.save()

        return Response(["Cena PLN: " + "{:.2f}".format(obj.price), "Kurs EUR: " + "{:.2f}".format(rate_eur), "Cena EUR: " + "{:.2f}".format(price_eur)], status=201)
