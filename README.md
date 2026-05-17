# MedSync

**Status do Projeto:** v2.0.0 (Etapa Intermediária Concluída)  
🌍 **Link Público do Deploy / Disponibilidade:** [Acesse o Repositório Oficial do MedSync](https://github.com/HeberMacedo/medsync)

Este é o meu projeto para o BootCamp. Criei o MedSync para ajudar no controle de medicamentos, pensando principalmente em idosos ou pessoas que tomam muitos remédios e acabam esquecendo os horários.

É uma ferramenta simples que roda direto no terminal (CLI), mas que foca na organização e na segurança dos dados.

## O que o programa faz:
* Cadastra o nome do remédio e o horário que deve ser tomado.
* Lista todos os agendamentos salvos para consulta rápida.
* Valida as entradas (não deixa salvar se os campos estiverem vazios).

## Tecnologias que usei:
Para o código usei Python. Além disso, configurei o Pytest para garantir que tudo funciona e o Ruff para manter o código limpo e padronizado. Também montei um GitHub Actions que roda esses testes sozinho toda vez que eu subo uma alteração.

---

## Descrição do Problema Real
Muitas pessoas, especialmente idosos ou indivíduos que utilizam múltiplos medicamentos diários, enfrentam sérias dificuldades para manter a regularidade de seus tratamentos. O esquecimento de horários, a falta de registro e a ausência de orientações básicas de bem-estar podem comprometer a eficácia terapêutica e colocar a saúde em risco, gerando ansiedade tanto para o paciente quanto para seus familiares.

## Proposta do projeto
O MedSync surge como uma ferramenta objetiva e acessível para o controle de medicamentos e promoção da saúde. Através de uma interface de linha de comando (CLI) focada na simplicidade e usabilidade, o sistema resolve o problema do acompanhamento diário de tratamentos. Como diferencial para o bem-estar do usuário, o sistema agora integra uma funcionalidade ativa que busca conselhos e dicas de saúde em tempo real, transformando o gerenciamento de remédios em uma experiência informativa e humanizada.

## Público-alvo
Idosos, cuidadores, familiares e pacientes que necessitam de organização rigorosa em suas rotinas de medicação e buscam um monitoramento centralizado.

---

## Novidades da Versão 2.0.0 (Etapa Intermediária)
* **Integração com API de Dicas:** Consumo em tempo real da API REST gratuita Adviceslip para exibir dicas automáticas de autocuidado e saúde ao iniciar a aplicação.
* **Qualidade e Testes de Integração:** Implementação de testes robustos utilizando Mock para isolar o ambiente e validar a lógica de integração sem depender de oscilações de rede.
* **Gestão de Demandas (GitHub Issues):** Mapeamento e rastreabilidade profissional através da Issue #1 detalhando os critérios de aceitação.
* **Estratégia de Branching:** Desenvolvimento isolado na branch obrigatória `entrega-intermediaria-1` antes da integração final via Pull Request.

## Tecnologias Utilizadas
* **Linguagem:** Python 3.12
* **Integração:** Requests (Consumo de API REST externa)
* **Testes:** Pytest (Testes de unidade e testes de integração com Mock)
* **Qualidade de Código:** Ruff (Linting e padronização avançada/PEP 8)
* **CI/CD:** GitHub Actions (Esteira automatizada de testes para cada Push ou Pull Request)

---

## ⚙️ Instruções de Instalação, Configuração e Execução

### 1. Instalação de Dependências
Certifique-se de ter o Python 3.x instalado na sua máquina. Acesse a pasta raiz do projeto no terminal e instale as dependências necessárias executando:
```bash
pip install -r requirements.txt

**Versão:** 1.0.0  
**Autor:** Heber Macedo
**repositório:** `https://github.com/HeberMacedo/medsync`
