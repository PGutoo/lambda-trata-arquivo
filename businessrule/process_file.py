import pandas as pd
from integration.client_integration import call_cnpj_api
from validate_docbr import CNPJ
from openpyxl import Workbook


class ProcessFile:

    # TODO
    # Implementar tratamento de erros
    # Tratamento para CNPJ
    def process_file(self, file):
        coluna_cnpj = pd.read_excel(file)
        cnpjs = coluna_cnpj['CNPJ'].tolist()
        valida_cnpj = CNPJ()
        cria_excel = Workbook()
        for cnpj in cnpjs:

            print(cnpj)
            cnpj_string = str(cnpj)
            valida_cnpj.validate(cnpj_string)
            dados_cnpj = call_cnpj_api(cnpj_string.zfill(14))
            nome = dados_cnpj.get('nome')
            # TODO
            # Retornar Nome, endereço, status, cnpj e email do CNPJ em um excel
            print(nome)
            planilha = cria_excel.active

        return True
