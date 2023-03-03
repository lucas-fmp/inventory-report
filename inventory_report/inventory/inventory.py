import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(file_path: str, report_type: str) -> str:
        extension = file_path.split(".")[-1]

        if extension == "csv":
            data = Inventory.read_csv(file_path)
        elif extension == "json":
            data = Inventory.read_json(file_path)
        elif extension == "xml":
            data = Inventory.read_xml(file_path)
        else:
            raise ValueError("Tipo de arquivo não suportado.")

        if report_type == "simples":
            report = SimpleReport.generate(data)
        elif report_type == "completo":
            report = CompleteReport.generate(data)
        else:
            raise ValueError("Tipo de relatório inválido.")

        return report

    @staticmethod
    def read_csv(file_path: str) -> list:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            data = [dict(row) for row in reader]
        return data

    @staticmethod
    def read_json(file_path: str) -> list:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data

    @staticmethod
    def read_xml(file_path: str) -> list:
        tree = ET.parse(file_path)
        root = tree.getroot()
        data = []
        for item in root:
            data.append(
                {
                    "id": item.find("id").text,
                    "nome_do_produto": item.find("nome_do_produto").text,
                    "nome_da_empresa": item.find("nome_da_empresa").text,
                    "data_de_fabricacao": item.find("data_de_fabricacao").text,
                    "data_de_validade": item.find("data_de_validade").text,
                    "numero_de_serie": item.find("numero_de_serie").text,
                    "instrucoes_de_armazenamento": item.find(
                        "instrucoes_de_armazenamento"
                    ).text,
                }
            )
        return data
