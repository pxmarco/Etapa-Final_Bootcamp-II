# MedSync
![CI](https://github.com/HeberMacedo/medsync/actions/workflows/main.yml/badge.svg)

Este é o meu projeto para o BootCamp. Criei o **MedSync** para ajudar no controle de medicamentos, pensando principalmente em idosos ou pessoas que tomam muitos remédios e acabam esquecendo os horários. 

É uma ferramenta simples que roda direto no terminal (CLI), mas que foca na organização e na segurança dos dados.

## O que o programa faz:
* Cadastra o nome do remédio e o horário que deve ser tomado.
* Lista todos os agendamentos salvos para consulta rápida.
* Valida as entradas (não deixa salvar se os campos estiverem vazios).

## Tecnologias que usei:
Para o código usei **Python**. Além disso, configurei o **Pytest** para garantir que tudo funciona e o Ruff para manter o código limpo e padronizado. Também montei um GitHub Actions que roda esses testes sozinho toda vez que eu subo uma alteração.

## Como rodar o projeto:
1. Primeiro, baixe ou clone o repositório.
2. Instale o que precisa com o comando: `pip install pytest ruff`
3. O comando padrão para rodar é `python src/main.py`. Caso o ambiente Python não esteja no PATH do sistema, o projeto também pode ser executado facilmente abrindo o arquivo `main.py` no VS Code e clicando no botão **Run** (triângulo) no canto superior direito.

## Testes e Qualidade:
Eu configurei comandos simples para testar o código:
* Para rodar os testes: `python -m pytest`
* Para ver se o código está no padrão (Lint): `python -m ruff check .`

---

## Descrição do Problema Real
Muitas pessoas idosas ou que tomam remédios controlados acabam se perdendo nos horários por causa da rotina ou por tomarem muitas pílulas diferentes no mesmo dia. Isso é perigoso porque esquecer de tomar ou tomar o remédio duas vezes pode fazer muito mal para a saúde.

## Proposta do projeto
O MedSync foi feito para resolver isso de um jeito direto no terminal. Para ajudar ainda mais o usuário, agora o sistema se conecta com a internet e puxa conselhos automáticos de saúde e bem-estar toda vez que o programa inicia, deixando o controle de remédios mais completo.

## Público-alvo
Idosos, familiares, cuidadores e qualquer pessoa que precise de uma força para lembrar de tomar os remédios nos horários certos.

## Novidades da Versão 2.0.0 (Etapa Intermediária)
* **Puxando dados de API:** O sistema agora se conecta com a API pública do Adviceslip para mostrar dicas de saúde automáticas na tela.
* **Testes de Integração com Mock:** Criei um teste que simula o funcionamento da API para garantir que o sistema não quebre se a internet cair.
* **Uso de Issues e Branches:** Abri a Issue #1 para planejar o código e fiz tudo separado na branch `entrega-intermediaria` antes de juntar na principal.

## Tecnologias Usadas
* Linguagem: Python
* Biblioteca para API: Requests
* Testes: Pytest e Mock
* Organização: GitHub Issues, Branches e Actions (CI)

## Instruções de Instalação e Execução
1. Baixe o projeto e abra no terminal.
2. Instale as dependências que estão no arquivo: `pip install -r requirements.txt`
3. Para rodar o programa completo com a API funcionando, use: `python src/main.py`

## Instruções para rodar os testes e linter:
* Para rodar os testes criados: `python -m pytest`
* Para rodar o verificador de código (Ruff): `python -m ruff check .`

## 🎯 Critérios de Aceitação da API Externa
| Nome da API | URL Base | O que ela faz no projeto | Status |
| :--- | :--- | :--- | :--- |
| **Adviceslip API** | `https://api.adviceslip.com/advice` | Mostra uma dica de saúde na tela assim que o programa abre no terminal. | **Funcionando** |

## Informações adicionais:
* **Versão atual:** 2.0.0
* **Autor:** Heber Macedo
* **Link do projeto:** https://github.com/HeberMacedo/medsync

Este projeto foi desenvolvido para a disciplina de Bootcamp II do curso de Engenharia de Software.
