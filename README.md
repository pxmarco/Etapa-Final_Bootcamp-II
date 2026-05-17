# MedSync
![CI](https://github.com/HeberMacedo/medsync/actions/workflows/main.yml/badge.svg)

Este é o meu projeto para o BootCamp. Criei o **MedSync** para ajudar no controle de medicamentos, pensando principalmente em idosos ou pessoas que tomam muitos remédios e acabam esquecendo os horários. 

É uma ferramenta simples que roda direto no terminal (CLI), mas que foca na organização e na segurança dos dados.

## O que o programa faz:
* Cadastra o nome do remédio e o horário que deve ser tomado.
* Lista todos os agendamentos salvos para consulta rápida.
* Valida as entradas (não deixa salvar se os campos estiverem vazios).

## Tecnologias que usei:
Para o código usei **Python**. Além disso, configurei o **Pytest** para garantir que tudo funciona e o **Ruff** para manter o código limpo e padronizado. Também montei um **GitHub Actions** que roda esses testes sozinho toda vez que eu subo uma alteração.

## Como rodar o projeto:
1. Primeiro, baixe ou clone o repositório.
2. Instale o que precisa com o comando: `pip install pytest ruff`
3. O comando padrão para rodar é `python src/main.py`. Caso o ambiente Python não esteja no PATH do sistema, o projeto também pode ser executado facilmente abrindo o arquivo `main.py` no VS Code e clicando no botão **Run** (triângulo) no canto superior direito.

## Testes e Qualidade:
Eu configurei comandos simples para testar o código:
* Para rodar os testes: `python -m pytest`
* Para ver se o código está no padrão (Lint): `python -m ruff check .`

**Versão:** 1.0.0  
**Autor:** Heber Macedo
**repositório:** `https://github.com/HeberMacedo/medsync`
