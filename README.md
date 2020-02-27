# Rispar Teste

##  Requisitos minimos da aplicação
    Python 3.6+
>
##  Estrutura do projeto
    .
    ├── src
    │   ├── models/
    │   └── main.py
    ├── tests
    │   ├── csv/
    |   |    ├── accounts.csv
    |   |    └── transactions.csv
    │   ├── account_tests.py
    │   ├── file_tests.py
    |   └── transaction_tests.py
    └── README.md
>
## Executar o projeto:
1. É necessário esta no diretório principal da aplicação.
2. Utilizando o python localmente
    ~~~bash
        python3 src/main.py tests/csv/accounts.csv tests/csv/transactions.csv
    ~~~
    ou se o python 3 for o padrão:
    ~~~bash
        python src/main.py tests/csv/accounts.csv tests/csv/transactions.csv
    ~~~
>
## Executar Testes:
1. É necessário esta no diretório principal da aplicação.
2. Utilizando o python localmente.
    ~~~bash
        python3 -m unittest discover -s tests/ -p "*_tests.py"
    ~~~
    ou se o python 3 for o padrão:
    ~~~bash
        python3 -m unittest discover -s tests/ -p "*_tests.py"
    ~~~
>

## Observações:
1. A pasta csv é utilizada para conter os arquivos csv de teste e é utilizada tanto no teste da aplicação como nos teste unitários.
2. Não existe uma real necessidade do pipfile ou do controle de pacote pipenv. Neste caso utilizei para controlar dependencias de desenvolvimento. Como por exemplo o debbuger ipdb.
