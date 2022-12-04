import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import '../data/monthly_cpi.dart';
import '../model/monthlycpi.dart';

class MonthlyCPIList extends StatefulWidget {
  MonthlyCPIList({Key? key}) : super(key: key);

  @override
  _MonthlyCPIListState createState() => _MonthlyCPIListState();
}

class _MonthlyCPIListState extends State<MonthlyCPIList> {
  List<MonthlyCPI> monthlyCPIList = [];

  void getMonthlyCPIList() async {
    MonthlyCPIApi.getMonthlyCPIList().then((response) {
      setState(() {
        Iterable list = json.decode(response.body);
        monthlyCPIList = list.map((model) => MonthlyCPI.fromJson(model)).toList();
        print(monthlyCPIList.elementAt(0).cpi_description);
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
        child: ListView.builder(
          itemCount: monthlyCPIList.length,
          itemBuilder: (context, index) {
            return ListTile(
              title: Text(monthlyCPIList[index].cpi_internal_code),
              subtitle: Text(monthlyCPIList[index].cpi_description),
            );
          }),
      ));
  }
}