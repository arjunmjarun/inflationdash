class MonthlyCPI {
  String monthly_cpi_id;
  String cpi_date;
  int cpi_year;
  int cpi_month;
  String cpi_year_month;
  String cpi_internal_code;
  String cpi_description;
  int cpi;

  MonthlyCPI.fromJson(Map json)
    : monthly_cpi_id = json['monthly_cpi_id'],
      cpi_date = json['cpi_date'],
      cpi_year = json['cpi_year'],
      cpi_month = json['cpi_month'],
      cpi_year_month = json['cpi_year_month'],
      cpi_internal_code = json['cpi_internal_code'],
      cpi_description = json['cpi_description'],
      cpi = json['cpi'];

  Map toJson() {
    return {
      'monthly_cpi_id': monthly_cpi_id,
      'cpi_date': cpi_date,
      'cpi_year': cpi_year,
      'cpi_month': cpi_month,
      'cpi_year_month': cpi_year_month,
      'cpi_internal_code': cpi_internal_code,
      'cpi_description': cpi_description,
      'cpi': cpi
    };
  }
}

class InflationPercentage {
  int cpi_2021;
  int cpi_2022;
  int cpi_month_2022;
  double inflation_percentage;

  InflationPercentage.fromJson(Map json)
    : cpi_2021 = json['cpi_2021'],
      cpi_2022 = json['cpi_2022'],
      cpi_month_2022 = json['cpi_month_2022'],
      inflation_percentage = json['inflation_percentage'];

  Map toJson() {
    return {
      'cpi_2021': cpi_2021,
      'cpi_2022': cpi_2022,
      'cpi_month_2022': cpi_month_2022,
      'inflation_percentage': inflation_percentage
    };
  }
}