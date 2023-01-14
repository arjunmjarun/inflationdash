from inflation.models import MonthlyCPI
from rest_framework.serializers import Serializer, ModelSerializer, SerializerMethodField

class MonthlyCPISerializer(ModelSerializer):
    '''
    Serializes the monthly CPI table
    '''
    class Meta:
        model = MonthlyCPI
        fields = ("cpi_2021", "cpi_2022", "cpi_month_2022", "inflation_percentage")

class InflationPercentageSerializer(Serializer):
    cpi_2021 = SerializerMethodField()
    cpi_2022 = SerializerMethodField()
    cpi_month_2022 = SerializerMethodField()
    inflation_percentage = SerializerMethodField()

    def get_cpi_2021(self, obj):
        return obj[0]

    def get_cpi_2022(self, obj):
        return obj[1]

    def get_cpi_month_2022(self, obj):
        return obj[2]

    def get_inflation_percentage(self, obj):
        return obj[3]
