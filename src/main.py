class MedSync:
    def __init__(self):
        self.medicamentos = []

    def adicionar_medicamento(self, nome, horario):
        if not nome.strip() or not horario.strip():
            raise ValueError("Nome e horário são obrigatórios.")
        item = {"nome": nome, "horario": horario}
        self.medicamentos.append(item)
        return f"Sucesso: {nome} agendado para às {horario}."

    def listar_medicamentos(self):
        if not self.medicamentos:
            return "Nenhum medicamento agendado."
        resultado = "\n--- Medicamentos Agendados ---"
        for m in self.medicamentos:
            resultado += f"\n💊 {m['nome']} - {m['horario']}"
        return resultado

def menu():
    app = MedSync()
    print("=== Bem-vindo ao MedSync (Versão 1.0.0) ===")
    while True:
        print("\n1. Adicionar Medicamento\n2. Listar Todos\n3. Sair")
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            n = input("Nome do remédio: ")
            h = input("Horário (ex: 08:00): ")
            try:
                print(app.adicionar_medicamento(n, h))
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == "2":
            print(app.listar_medicamentos())
        elif opcao == "3":
            print("Encerrando... Cuide-se!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()