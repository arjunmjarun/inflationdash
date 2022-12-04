import 'dart:async';
import 'package:http/http.dart' as http;

class MonthlyCPIApi {
  static Future getMonthlyCPIList() {
    var url = Uri.parse('http://127.0.0.1:8000/');
    return http.get(url);
  }
}
