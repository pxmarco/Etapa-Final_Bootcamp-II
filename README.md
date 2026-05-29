# MedSync
![CI](https://github.com/HeberMacedo/medsync/actions/workflows/main.yml/badge.svg)

Deploy: https://hebermacedo.github.io/medsync/

Este é o projeto para Etapa Final da disciplina BootCamp. A ideia do MedSync é ajudar no controle de remédios, principalmente para quem toma vários medicamentos no dia, previnindo o esquecimento de algum horário e/ou dose.

## Funcionalidades

* Cadastrar um remédio, horário, dose e observação.
* Ver a lista de remédios cadastrados.
* Remover um remédio da lista na versão web.
* Consultar um endereço pelo CEP usando a API ViaCEP.
* Usar a versão web pelo navegador.

## API usada

Usamos a API pública ViaCEP para buscar endereços a partir de um CEP.

Endpoint:

`https://viacep.com.br/ws/{cep}/json/`

No projeto, essa consulta serve para simular um endereço de entrega ou retirada de medicamento.

## Como rodar no computador

1. Clone ou baixe o repositório.
2. Instale as dependências:

`pip install -r requirements.txt`

3. Rode o programa no terminal:

`python src/main.py`

Tambem há a possibilidade de abrir o arquivo `main.py` no VS Code e clicar em **Run**.

## Testes

Para rodar os testes:

`python -m pytest`

Para rodar o lint:

`python -m ruff check .`

## Links

Repositório: https://github.com/pxmarco/Etapa-final/
Deploy: https://hebermacedo.github.io/medsync/

Autores: Heber Macedo, Marco Antonio, Maria Bertin e Thaynara Lima.
