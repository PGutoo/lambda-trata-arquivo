import pandas as pd
from integration.client_integration import call_cnpj_api
from validate_docbr import CNPJ


class ProcessFile:

    # TODO
    # Implementar tratamento de erros
    # Tratamento para CNPJ
    def process_file(self, file):
        coluna_cnpj = pd.read_excel(file)
        cnpjs = coluna_cnpj['CNPJ'].tolist()
        # valida_cnpj = CNPJ()
        for cnpj in cnpjs:

            # valida_cnpj.validate(cnpj)
            print(cnpj)
            dados_cnpj = call_cnpj_api(cnpj)
            nome = dados_cnpj['nome']
            print(nome)

        return True
