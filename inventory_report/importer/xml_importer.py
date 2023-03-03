from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(file_path: str) -> list:
        if file_path.endswith(".xml"):
            tree = ET.parse(file_path)
            root = tree.getroot()
            data = []
            for item in root:
                data.append(
                    {
                        "id": item.find("id").text,
                        "nome_do_produto": item.find("nome_do_produto").text,
                        "nome_da_empresa": item.find("nome_da_empresa").text,
                        "data_de_fabricacao": item.find(
                            "data_de_fabricacao"
                        ).text,
                        "data_de_validade": item.find("data_de_validade").text,
                        "numero_de_serie": item.find("numero_de_serie").text,
                        "instrucoes_de_armazenamento": item.find(
                            "instrucoes_de_armazenamento"
                        ).text,
                    }
                )
            return data
        else:
            raise ValueError("Arquivo inválido")
