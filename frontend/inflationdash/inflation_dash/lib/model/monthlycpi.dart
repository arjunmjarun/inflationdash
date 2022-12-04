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
      'monthl_cpi_id': monthly_cpi_id,
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