# Lambda Trata Arquivos

## O que é?

Esta é uma aplicação de processamento de regras de negócio que lida com a validação de CNPJs e a integração com uma API externa.

## Pré-requisitos

Python 3.x instalado

## Clone o repositório:

git clone https://github.com/PGutoo/lambda-trata-arquivo.git

## Instale as bibliotecas necessárias:

pip install -r requirements.txt

## Uso

Abra um terminal na sua IDE e execute o comando ``py .\lambda_function.py``, isso iniciará a aplicação localmente na porta 5000.
Como a aplicação simula uma lambda AWS, utilize a rota /upload-arquivo como o gatilho inicial do evento de uma lambda, um arquivo xlsx deve ser enviado no body request.


## Contato

Se você tiver alg uma dúvida ou sugestão, entre em contato com o autor do projeto.

Espero que você encontre essa aplicação útil! Se você tiver alguma dúvida, fique à vontade para perguntar.