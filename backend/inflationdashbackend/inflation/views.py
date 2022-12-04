from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import MonthlyCPI
from .serializers import MonthlyCPISerializer

@api_view(['GET'])
def getUSInflationData(request):
    '''
    Gets all time US national inflation data, all items
    '''
    items = MonthlyCPI.objects.filter(cpi_internal_code='CPIAUCSL')
    serializer = MonthlyCPISerializer(items, many=True)
    return Response(serializer.data)