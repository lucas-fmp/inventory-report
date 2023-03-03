import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(file_path: str) -> list:
        if file_path.endswith(".csv"):
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                data = [dict(row) for row in reader]
            return data
        else:
            raise ValueError("Arquivo inválido")
