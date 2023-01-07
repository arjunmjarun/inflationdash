import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:fl_chart/fl_chart.dart';
import 'package:http/http.dart' as http;

import '../data/monthly_cpi.dart';
import '../model/monthlycpi.dart';

class MonthlyCPIList extends StatefulWidget {
  MonthlyCPIList({Key? key}) : super(key: key);

  @override
  _MonthlyCPIListState createState() => _MonthlyCPIListState();
}

class _MonthlyCPIListState extends State<MonthlyCPIList> {
  List<InflationPercentage> monthlyCPIList = [];
  List<double> cpi_only_list = [];
  List<double> x_axis_points = new List<double>.generate(10, (i) => i+1);
  List<FlSpot> final_list = [];

  void getMonthlyCPIList() async {
    MonthlyCPIApi.getMonthlyCPIList().then((response) {
      setState(() {
        Iterable list = json.decode(response.body);
        monthlyCPIList = list.map((model) => InflationPercentage.fromJson(model)).toList();
        cpi_only_list = monthlyCPIList.map((x) => x.inflation_percentage).toList();
        print(cpi_only_list);
        for (int i = 0; i <= 5; i++) {
          final_list.add(FlSpot(x_axis_points[i], cpi_only_list[i]));
        }
      });
    });
  }

  @override
  void initState() {
    super.initState();
    getMonthlyCPIList();
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Monthly CPI Data"),
      ),
      body: Container(
          padding: const EdgeInsets.all(10),
          width: double.infinity,
          height: 300,
          child: LineChart(
            LineChartData(
              borderData: FlBorderData(show: false),
              lineBarsData: [
                LineChartBarData(spots:
                  final_list
                )
              ]
            )
          )
      ));
  }
}