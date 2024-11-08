class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros = valor / self.valor_litro
        if litros > self.quantidade_combustivel:
            print("Não há combustível suficiente na bomba.")
            litros = self.quantidade_combustivel
            valor = litros * self.valor_litro
        self.quantidade_combustivel -= litros
        print(f"Abastecido: {litros:.2f} litros de {self.tipo_combustivel}. Valor a pagar: R$ {valor:.2f}")

    def abastecer_por_litro(self, litros):
        # Calcula o valor a ser pago pelo cliente
        if litros > self.quantidade_combustivel:
            print("Não há combustível suficiente na bomba.")
            litros = self.quantidade_combustivel
        valor = litros * self.valor_litro
        self.quantidade_combustivel -= litros
        print(f"Abastecido: {litros:.2f} litros de {self.tipo_combustivel}. Valor a pagar: R$ {valor:.2f}")

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
        print(f"Valor do litro alterado para R$ {self.valor_litro:.2f}")

    def alterar_combustivel(self, novo_tipo):
        self.tipo_combustivel = novo_tipo
        print(f"Tipo de combustível alterado para {self.tipo_combustivel}")

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade
        print(f"Quantidade de combustível na bomba alterada para {self.quantidade_combustivel:.2f} litros")


def main():
    bomba = BombaCombustivel("Gasolina", 5.50, 100)

    while True:
        print("\n--- Bomba de Combustível ---")
        print("1. Abastecer por Valor")
        print("2. Abastecer por Litro")
        print("3. Alterar Valor do Litro")
        print("4. Alterar Tipo de Combustível")
        print("5. Alterar Quantidade de Combustível")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Informe o valor a ser abastecido: R$ "))
            bomba.abastecer_por_valor(valor)

        elif opcao == '2':
            litros = float(input("Informe a quantidade em litros a ser abastecida: "))
            bomba.abastecer_por_litro(litros)

        elif opcao == '3':
            novo_valor = float(input("Informe o novo valor do litro: R$ "))
            bomba.alterar_valor(novo_valor)

        elif opcao == '4':
            novo_tipo = input("Informe o novo tipo de combustível: ")
            bomba.alterar_combustivel(novo_tipo)

        elif opcao == '5':
            nova_quantidade = float(input("Informe a nova quantidade de combustível: "))
            bomba.alterar_quantidade_combustivel(nova_quantidade)

        elif opcao == '6':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()