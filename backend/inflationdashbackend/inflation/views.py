from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import MonthlyCPI
from .serializers import MonthlyCPISerializer

@api_view(['GET'])
def getUSInflationData(request):
    '''
    Gets all time US national inflation data, all items
    '''
    query = '''SELECT DISTINCT
                cpi_2021,
                cpi_2022,
                cpi_2022.cpi_month_2022,
                (cpi_2022 - cpi_2021) / cast(cpi_2022 AS REAL) AS inflation_percentage
           FROM (
            SELECT
                cpi as cpi_2021,
                cpi_month as cpi_month_2021
            FROM inflation_monthlycpi
            WHERE cpi_internal_code = "CUUR0000SEHA"
            AND   cpi_year IN ("2021")
           ) AS cpi_2021
           JOIN
           (
            SELECT
                cpi as cpi_2022,
                cpi_month as cpi_month_2022
            FROM inflation_monthlycpi
            WHERE cpi_internal_code = "CUUR0000SEHA"
            AND   cpi_year IN ("2022")
           ) AS cpi_2022 ON cpi_2021.cpi_month_2021 = cpi_2022.cpi_month_2022
        '''
    items = MonthlyCPI.objects.raw(query)
    serializer = MonthlyCPISerializer(items, many=True)
    return Response(serializer.data)