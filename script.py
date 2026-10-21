print("--- GERENCIADOR DE GASTOS MENSAL ---")

# Inicialização de variáveis
try:
    receitas = float(input("Digite o valor total das suas receitas (R$): "))
except ValueError:
    print("Valor inválido. Definindo receita como R$ 0.00")
    receitas = 0.0

total_despesas = 0.0

# Loop para adicionar despesas dinamicamente
while True:
    descricao = input("\nDigite a descrição da despesa (ou 'sair' para finalizar): ").strip()
    
    if descricao.lower() == 'sair':
        break
        
    try:
        valor = float(input(f"Digite o valor de '{descricao}' (R$): "))
        total_despesas += valor
    except ValueError:
        print("Valor inválido! Essa despesa não foi computada. Tente novamente.")

# Cálculo do saldo final
saldo_final = receitas - total_despesas

# Exibição do Resumo
print("\n--- RESUMO FINANCEIRO ---")
print(f"Total de Receitas: R$ {receitas:.2f}")
print(f"Total de Despesas: R$ {total_despesas:.2f}")
print(f"Saldo Final: R$ {saldo_final:.2f}")

if saldo_final >= 0:
    print("Situação: Saldo Positivo 🟢")
else:
    print("Situação: Saldo Negativo (Alerta de Dívida!) 🔴")
