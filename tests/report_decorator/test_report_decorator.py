from inventory_report.reports.colored_report import ColoredReport

# from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    product_list = [
        {
            "id": "1",
            "nome_do_produto": "Nicotine Polacrilex",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2021-02-18",
            "data_de_validade": "2023-09-17",
            "numero_de_serie": "CR25 1551 4467 2549 4402 1",
            "instrucoes_de_armazenamento": "instrucao 1",
        },
    ]

    colored_report = ColoredReport(SimpleReport)

    colored_simple_report = colored_report.generate(product_list)

    expected_phrase = (
        "\x1b[32mData de fabricação mais antiga:\x1b[0m "
        "\x1b[36m2021-02-18\x1b[0m\n"
        "\x1b[32mData de validade mais próxima:\x1b[0m "
        "\x1b[36m2023-09-17\x1b[0m\n"
        "\x1b[32mEmpresa com mais produtos:\x1b[0m "
        "\x1b[31mTarget Corporation\x1b[0m"
    )

    assert colored_simple_report == expected_phrase
