from rest_framework.generics import ListAPIView

from corona.models import Country

from .serializers import CountrySerializer


class CountryListView(ListAPIView):
    queryset= Country.objects.all()
    serializer_class= CountrySerializer