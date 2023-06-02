from Third_algorithm import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from get_BS_PL import *
from get_sync_data import *
#적극
# Load the UI file
Ui_Recommand, _ = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/aggressively_recommand.ui")

class aggresive(QtWidgets.QMainWindow, Ui_Recommand):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hide)

        # Call the function to populate the table
        self.populate_table()

    def populate_table(self):
        # Call first_arg(1) to get the values
        arg_corp = third_arg(4)

        # Sort the dictionary by Weighted Average in descending order
        sorted_corp = sorted(arg_corp.items(), key=lambda x: x[1][3], reverse=True)

        # Set the table dimensions based on the number of rows and columns
        num_rows = len(sorted_corp)
        num_columns = 5  # 4 values in corp list + 1 for company name
        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_columns)

        # Set the headers for each column
        headers = ['기업명', '기업규모', '순유동 자산가치', 'PER', '종합점수']
        self.tableWidget.setHorizontalHeaderLabels(headers)

        # Populate the table with the sorted values
        for row, (company, corp) in enumerate(sorted_corp):
            item_company = QTableWidgetItem(company)
            self.tableWidget.setItem(row, 0, item_company)

            for col, value in enumerate(corp, start=1):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)
