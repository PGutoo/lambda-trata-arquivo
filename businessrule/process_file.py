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
        print(cnpjs)
        valida_cnpj = CNPJ()
        excel = Workbook()
        for cnpj in cnpjs:

            print(cnpj)
            cnpj_string = str(cnpj)
            valida_cnpj.validate(cnpj_string)
            dados_cnpj = call_cnpj_api(cnpj_string.zfill(14))
            nome = dados_cnpj.get('nome')
            logradouro = dados_cnpj.get('logradouro')
            bairro = dados_cnpj.get('bairro')
            uf = dados_cnpj.get('uf')
            email = dados_cnpj.get('email')

            # TODO
            # Retornar Nome, endereço, status, cnpj e email do CNPJ em um excel
            print(nome)
            planilha = excel.active
            planilha['A1'] = 'Nome'
            planilha['B1'] = 'Logradouro'
            planilha['C1'] = 'Bairro'
            planilha['D1'] = 'UF'
            planilha['E1'] = 'Email'
            planilha.append([nome, logradouro, bairro, uf, email])
            excel.save('novo_arquivo.xlsx') # TODO: nome do arquivo unico, onde retornar?
        return True
