import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        print("Verifique os argumentos", file=sys.stderr)
        return

    file_path = sys.argv[1]
    report_type = sys.argv[2]

    if file_path.endswith(".xml"):
        inventory = InventoryRefactor(XmlImporter)
    elif file_path.endswith(".json"):
        inventory = InventoryRefactor(JsonImporter)
    else:
        inventory = InventoryRefactor(CsvImporter)

    report = inventory.import_data(file_path, report_type)

    sys.stdout.write(report)


if __name__ == "__main__":
    main()
