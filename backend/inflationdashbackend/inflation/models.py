import uuid
from django.db import models

# Create your models here.

## Data sets:
## CPIAUCSL = US inflation, all items
## CUSR0000SETA02 = US inflation, used cars and trucks
## CUUR0000SETA01 = US inflation, new cars
## CPIUFDSL = US inflation, food
## CUUR0000SEHA = US inflation, rent
## CPIENGSL = US inflation, energy
## CUSR0000SETB01 = US inflation, gasoline
## CUSR0000SEHG = US inflation, water trash & sewer collection
## CUUR0000SAS4 = US inflation, transportation services

class MonthlyCPI(models.Model):
    '''
    This table is at the year-month level and has the CPI data from
    FRED: St.Louis

    The CPI is an actual number, not a percentage difference
    '''
    monthly_cpi_id = models.TextField(primary_key=True, default=uuid.uuid4(), editable=False)
    cpi_date = models.DateField()
    cpi_year = models.IntegerField()
    cpi_month = models.IntegerField()
    cpi_year_month = models.TextField()
    cpi_internal_code = models.TextField(default='')
    cpi_description = models.TextField()
    cpi = models.DecimalField(max_digits=10, decimal_places=10)

    def __str__(self):
        return self.name