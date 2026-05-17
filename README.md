# MedSync
![CI](https://github.com/HeberMacedo/medsync/actions/workflows/main.yml/badge.svg)

**Deploy da aplicacao web:** https://hebermacedo.github.io/medsync/

Este e o meu projeto para o BootCamp. Criei o **MedSync** para ajudar no controle de medicamentos, pensando principalmente em idosos ou pessoas que tomam muitos remedios e acabam esquecendo os horarios.

E uma ferramenta simples que roda no terminal (CLI), mas que foca na organizacao e na seguranca dos dados. Na entrega intermediaria, o projeto tambem ganhou uma versao web publicada no GitHub Pages, permitindo que o avaliador use o sistema diretamente pelo navegador. A aplicacao consulta a API publica **ViaCEP** para buscar enderecos por CEP e apoiar entregas ou retiradas de medicamentos.

## O que o programa faz:
* Cadastra o nome do remedio e o horario que deve ser tomado.
* Lista todos os agendamentos salvos para consulta rapida.
* Consulta um endereco por CEP usando a API publica ViaCEP.
* Disponibiliza uma versao web para uso pelo link de deploy.
* Valida as entradas (nao deixa salvar se os campos estiverem vazios).

## Tecnologias que usei:
Para o codigo usei **Python**. Alem disso, configurei o **Pytest** para garantir que tudo funciona e o **Ruff** para manter o codigo limpo e padronizado. Tambem montei um **GitHub Actions** que roda esses testes sozinho toda vez que eu subo uma alteracao.

## Como rodar o projeto:
1. Primeiro, baixe ou clone o repositorio.
2. Instale o que precisa com o comando: `pip install -r requirements.txt`
3. O comando padrao para rodar e `python src/main.py`. Caso o ambiente Python nao esteja no PATH do sistema, o projeto tambem pode ser executado facilmente abrindo o arquivo `main.py` no VS Code e clicando no botao **Run** no canto superior direito.

## API integrada:
A aplicacao usa a API publica ViaCEP:
* Endpoint: `https://viacep.com.br/ws/{cep}/json/`
* Metodo: `GET`
* Uso no MedSync: consulta de endereco por CEP para entrega ou retirada de medicamentos.

## Testes e Qualidade:
Eu configurei comandos simples para testar o codigo:
* Para rodar os testes: `python -m pytest`
* Para ver se o codigo esta no padrao (Lint): `python -m ruff check .`

**Versao:** 1.1.0  
**Autor:** Heber Macedo  
**Repositorio:** `https://github.com/HeberMacedo/medsync`
