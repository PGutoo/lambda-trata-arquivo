from flask import Flask, request

from businessrule.process_file import ProcessFile

app = Flask(__name__)


@app.route('/upload-arquivo', methods=['POST'])
def lambda_handler():

    try:
        # Recebe o arquivo
        arquivo_excel = request.files['file']
        print(arquivo_excel.filename)
        if arquivo_excel.filename.endswith('.xlsx'):
            process_file = ProcessFile()
            process_file.process_file(arquivo_excel)
        else:
            return {
                'statusCode': 500,
                'body': 'Erro ao processar arquivo'
            }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': 'Erro ao processar arquivo'
        }   
    return {
        'statusCode': 200,
        'body': 'Arquivo processado com sucesso'
    }


if __name__ == '__main__':
    app.run(debug=True)