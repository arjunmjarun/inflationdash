from django.db import connection
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import MonthlyCPI
from .serializers import InflationPercentageSerializer

@api_view(['GET'])
def getUSInflationData(request):
    '''
    Gets all time US national inflation data, all items
    '''
    crsr = connection.cursor()
    crsr.execute('''SELECT DISTINCT
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
                    ) AS cpi_2022 ON cpi_2021.cpi_month_2021 = cpi_2022.cpi_month_2022''')
    items = crsr.fetchall()
    serializer = InflationPercentageSerializer(items, many=True)
    print(serializer.data)
    return Response(serializer.data)