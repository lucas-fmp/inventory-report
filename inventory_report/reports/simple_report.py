import datetime


class SimpleReport:
    @staticmethod
    def generate(product_list):

        oldest_date = min(
            [
                datetime.datetime.strptime(
                    product["data_de_fabricacao"], "%Y-%m-%d"
                )
                for product in product_list
            ]
        ).strftime("%Y-%m-%d")

        now = datetime.datetime.now()

        valid_products = [
            product
            for product in product_list
            if datetime.datetime.strptime(
                product["data_de_validade"], "%Y-%m-%d"
            )
            > now
        ]

        closest_valid_date = min(
            [
                datetime.datetime.strptime(
                    product["data_de_validade"], "%Y-%m-%d"
                )
                for product in valid_products
            ]
        ).strftime("%Y-%m-%d")

        companies = [product["nome_da_empresa"] for product in product_list]
        company_count = {
            company: companies.count(company) for company in set(companies)
        }
        most_products_company = max(company_count, key=company_count.get)

        report = f"Data de fabricação mais antiga: {oldest_date}\n"
        report += f"Data de validade mais próxima: {closest_valid_date}\n"
        report += f"Empresa com mais produtos: {most_products_company}"

        return report
