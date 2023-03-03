import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(file_path: str) -> list:
        if file_path.endswith(".json"):
            with open(file_path, "r") as file:
                data = json.load(file)
            return data
        else:
            raise ValueError("Arquivo inválido")
