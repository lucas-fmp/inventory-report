from collections.abc import Iterable
from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Iterable):
    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = []

    def import_data(self, file_path: str, report_type: str) -> str:
        new_data = self.importer.import_data(file_path)
        self.data.extend(new_data)

        if report_type == "simples":
            report = SimpleReport.generate(self.data)
        elif report_type == "completo":
            report = CompleteReport.generate(self.data)
        else:
            raise ValueError("Tipo de relatório inválido.")

        return report

    def __iter__(self):
        return InventoryIterator(self.data)
