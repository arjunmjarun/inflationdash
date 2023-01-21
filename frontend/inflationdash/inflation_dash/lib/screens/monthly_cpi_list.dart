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
        print(list);
        monthlyCPIList = list.map((model) => InflationPercentage.fromJson(model)).toList();
        cpi_only_list = monthlyCPIList.map((x) => double.parse((x.inflation_percentage * 100).toStringAsFixed(1))).toList();
        for (int i = 0; i <= 9; i++) {
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
              minY: 2,
              maxY: 9,
              borderData: FlBorderData(  
                show: true,
                border: Border.all(color: const Color(0xff37434d)),
              ),
              gridData: FlGridData(
                show: true,
                drawHorizontalLine: true,
                drawVerticalLine: false,
                verticalInterval: 1,
                horizontalInterval: 1
              ),
              titlesData: FlTitlesData(
                show: true,
                rightTitles: AxisTitles(
                  sideTitles: SideTitles(showTitles: false)
                ),
                topTitles: AxisTitles(
                  axisNameWidget: Text(
                    "Monthly Inflation Percentage",
                    style: TextStyle(
                      fontSize: 18,
                    ) 
                  )
                ),
                bottomTitles: AxisTitles(
                  sideTitles: SideTitles(
                    showTitles: true,
                    reservedSize: 30,
                    interval: 1,
                    getTitlesWidget: bottomTitleWidgets,
                  )
                )
              ),
              lineBarsData: [
                LineChartBarData(spots:
                  final_list
                )
              ]
            ),
          )
      ));
  }
}

Widget bottomTitleWidgets(double value, TitleMeta meta) {
  const style = TextStyle(
    color: Color(0xff68737d),
    fontWeight: FontWeight.bold,
    fontSize: 12
  );
  Widget text;
  switch (value.toInt()) {
    case 1:
      text = const Text('JAN', style:style);
      break;
    case 2:
      text = const Text('FEB', style:style);
      break;
    case 3:
      text = const Text('MAR', style:style);
      break;
    case 4:
      text = const Text('APRIL', style:style);
      break;
    case 5:
      text = const Text('MAY', style:style);
      break;
    case 6:
      text = const Text('JUNE', style:style);
      break;
    case 7:
      text = const Text('JULY', style:style);
      break;
    case 8:
      text = const Text('AUG', style:style);
      break;
    case 9:
      text = const Text('SEPT', style:style);
      break;
    case 10:
      text = const Text('OCT', style:style);
      break;
    case 11:
      text = const Text('NOV', style:style);
      break;
    case 12:
      text = const Text('DEC', style:style);
      break;
    default:
      text = const Text('', style: style);
      break;
  }

  return SideTitleWidget(
    axisSide: meta.axisSide,
    child: text,
  );
}