from inflation.models import MonthlyCPI
from rest_framework import serializers

class MonthlyCPISerializer(serializers.ModelSerializer):
    '''
    Serializes the monthly CPI table
    '''
    class Meta:
        model = MonthlyCPI
        fields = '__all__'