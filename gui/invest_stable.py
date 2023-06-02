from First_algorithm import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from get_BS_PL import *
from get_sync_data import *
# 안정추구형
# Load the UI file
Ui_Recommand, _ = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/stable_seek_recommand.ui")

class stable(QtWidgets.QMainWindow, Ui_Recommand):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.pushButton.clicked.connect(self.hide)

        # Call the function to populate the table with choice=2
        self.populate_table(2)

    def populate_table(self, choice):
        # Call first_arg(choice) to get the values
        arg_corp = first_arg(choice)

        # Sort the dictionary by Weighted Average in descending order
        sorted_corp = sorted(arg_corp.items(), key=lambda x: x[1][4], reverse=True)

        # Set the table dimensions based on the number of rows and columns
        num_rows = len(sorted_corp)
        num_columns = 6  # 5 values in corp list + 1 for company name
        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_columns)

        # Set the headers for each column
        headers = ['회사명', '기업 규모', 'PER', '기업의 안정성', '수익성', '종합 점수']
        self.tableWidget.setHorizontalHeaderLabels(headers)

        # Populate the table with the sorted values
        for row, (company, corp) in enumerate(sorted_corp):
            item_company = QTableWidgetItem(company)
            self.tableWidget.setItem(row, 0, item_company)

            for col, value in enumerate(corp, start=1):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)
