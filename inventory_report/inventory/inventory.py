from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(file_path: str, report_type: str) -> str:
        extension = file_path.split(".")[-1]

        if extension == "csv":
            data = CsvImporter.import_data(file_path)
        elif extension == "json":
            data = JsonImporter.import_data(file_path)
        else:
            data = XmlImporter.import_data(file_path)

        if report_type == "simples":
            report = SimpleReport.generate(data)
        elif report_type == "completo":
            report = CompleteReport.generate(data)
        else:
            raise ValueError("Tipo de relatório inválido.")

        return report
