from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import MonthlyCPI
from .serializers import MonthlyCPISerializer

@api_view(['GET'])
def getData(request):
    items = MonthlyCPI.objects.all()
    serializer = MonthlyCPISerializer(items, many=True)
    return Response(serializer.data)