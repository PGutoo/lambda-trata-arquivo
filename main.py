from flask import Flask, request

from businessrule.ProcessFile import ProcessFile

app = Flask(__name__)


@app.route('/upload-arquivo', methods=['POST'])
def lambda_handler():
    # Recebe o arquivo
    arquivo_excel = request.files['file']
    print(arquivo_excel.filename)
    if arquivo_excel.filename.endswith('.xlsx'):
        process_file = ProcessFile()
        process_file.read_file(arquivo_excel)
    else:
        dados = 'Arquivo invalido'
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }


if __name__ == '__main__':
    app.run(debug=True)