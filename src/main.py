from cep_service import CepServiceError, consultar_cep, formatar_endereco


class MedSync:
    def __init__(self):
        self.medicamentos = []
        self.endereco_entrega = None

    def adicionar_medicamento(self, nome, horario):
        if not nome.strip() or not horario.strip():
            raise ValueError("Nome e horario sao obrigatorios.")
        item = {"nome": nome, "horario": horario}
        self.medicamentos.append(item)
        return f"Sucesso: {nome} agendado para as {horario}."

    def listar_medicamentos(self):
        if not self.medicamentos:
            return "Nenhum medicamento agendado."
        resultado = "\n--- Medicamentos Agendados ---"
        for medicamento in self.medicamentos:
            resultado += f"\n[medicamento] {medicamento['nome']} - {medicamento['horario']}"
        return resultado

    def definir_endereco_por_cep(self, cep):
        endereco = consultar_cep(cep)
        self.endereco_entrega = endereco
        return f"Endereco encontrado: {formatar_endereco(endereco)}"

    def ver_endereco_entrega(self):
        if not self.endereco_entrega:
            return "Nenhum endereco de entrega cadastrado."
        return f"Endereco de entrega: {formatar_endereco(self.endereco_entrega)}"


def menu():
    app = MedSync()
    print("=== Bem-vindo ao MedSync (Versao 1.1.0) ===")
    while True:
        print(
            "\n1. Adicionar Medicamento"
            "\n2. Listar Todos"
            "\n3. Consultar endereco por CEP"
            "\n4. Ver endereco de entrega"
            "\n5. Sair"
        )
        opcao = input("\nEscolha uma opcao: ")
        if opcao == "1":
            nome = input("Nome do remedio: ")
            horario = input("Horario (ex: 08:00): ")
            try:
                print(app.adicionar_medicamento(nome, horario))
            except ValueError as erro:
                print(f"Erro: {erro}")
        elif opcao == "2":
            print(app.listar_medicamentos())
        elif opcao == "3":
            cep = input("CEP para entrega/retirada: ")
            try:
                print(app.definir_endereco_por_cep(cep))
            except (ValueError, CepServiceError) as erro:
                print(f"Erro: {erro}")
        elif opcao == "4":
            print(app.ver_endereco_entrega())
        elif opcao == "5":
            print("Encerrando... Cuide-se!")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    menu()
