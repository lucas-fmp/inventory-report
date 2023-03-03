from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(product_list):
        simple_report = SimpleReport.generate(product_list)

        companies = {}
        for product in product_list:
            company_name = product["nome_da_empresa"]
            if company_name not in companies:
                companies[company_name] = 1
            else:
                companies[company_name] += 1

        complete_report = f"{simple_report}\nProdutos estocados por empresa:\n"

        for company, count in companies.items():
            complete_report += f"- {company}: {count}\n"

        return complete_report
