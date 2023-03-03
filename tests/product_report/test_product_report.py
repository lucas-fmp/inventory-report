from inventory_report.inventory.product import Product


def test_relatorio_produto():
    fake_product = {
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1",
    }

    product_data = Product(
        fake_product["id"],
        fake_product["nome_do_produto"],
        fake_product["nome_da_empresa"],
        fake_product["data_de_fabricacao"],
        fake_product["data_de_validade"],
        fake_product["numero_de_serie"],
        fake_product["instrucoes_de_armazenamento"],
    )

    assert (
        str(product_data)
        == "O produto Nicotine Polacrilex fabricado em 2021-02-18 "
        "por Target Corporation com validade até 2023-09-17 precisa "
        "ser armazenado instrucao 1."
    )
