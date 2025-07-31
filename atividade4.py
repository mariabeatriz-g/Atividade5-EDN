from datetime import datetime

def calcular_dias_vividos(data_nascimento: str) -> int:
    """
    Calcula o número de dias que uma pessoa está viva.
    
    Parâmetro:
    - data_nascimento (str): Data de nascimento no formato DD/MM/AAAA

    Retorna:
    - int: Número de dias vividos
    """
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    hoje = datetime.today()
    dias_vividos = (hoje - nascimento).days
    return dias_vividos

# Interação com o usuário
data_input = input("Digite sua data de nascimento (DD/MM/AAAA): ")

try:
    dias = calcular_dias_vividos(data_input)
    print(f"Você está vivo há aproximadamente {dias} dias.")
except ValueError:
    print("Formato de data inválido. Use o formato DD/MM/AAAA.")