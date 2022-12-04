import 'package:flutter/material.dart';
import 'screens/monthly_cpi_list.dart';

void main() {
  runApp(FlutterSearch());
}
class FlutterSearch extends StatefulWidget {
  @override
  _FlutterSearchState createState() => _FlutterSearchState();
}

class _FlutterSearchState extends State<FlutterSearch> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MonthlyCPIList(),
    );
  }
}