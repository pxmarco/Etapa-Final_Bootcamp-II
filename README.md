# MedSync
![CI](https://github.com/HeberMacedo/medsync/actions/workflows/main.yml/badge.svg)

Deploy: https://hebermacedo.github.io/medsync/

Este e o meu projeto do BootCamp. A ideia do MedSync e ajudar no controle de remedios, principalmente para quem toma varios medicamentos no dia e pode acabar esquecendo algum horario.

Nesta entrega intermediaria eu mantive a versao em Python pelo terminal e tambem fiz uma versao web simples, para ficar mais facil testar pelo link do deploy.

## O que da para fazer

* Cadastrar um remedio e o horario.
* Ver a lista de remedios cadastrados.
* Consultar um endereco pelo CEP usando a API ViaCEP.
* Usar a versao web pelo navegador.

## API usada

Usei a API publica ViaCEP para buscar endereco a partir de um CEP.

Endpoint:

`https://viacep.com.br/ws/{cep}/json/`

No projeto, essa consulta serve para simular um endereco de entrega ou retirada de medicamento.

## Como rodar no computador

1. Clone ou baixe o repositorio.
2. Instale as dependencias:

`pip install -r requirements.txt`

3. Rode o programa no terminal:

`python src/main.py`

Tambem da para abrir o arquivo `main.py` no VS Code e clicar em **Run**.

## Testes

Para rodar os testes:

`python -m pytest`

Para rodar o lint:

`python -m ruff check .`

## Links

Repositorio: https://github.com/HeberMacedo/medsync  
Deploy: https://hebermacedo.github.io/medsync/

Autor: Heber Macedo
