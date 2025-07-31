def calcular_desconto(preco_original: float, percentual: float) -> float:
    """
    Calcula o valor do desconto.
    
    Parâmetros:
    - preco_original: valor original do produto
    - percentual: percentual de desconto (ex: 20 para 20%)
    
    Retorna:
    - valor do desconto
    """
    return round(preco_original * (percentual / 100), 2)

def calcular_preco_final(preco_original: float, desconto: float) -> float:
    """
    Calcula o preço final após aplicar o desconto.
    
    Retorna:
    - preço final do produto
    """
    return round(preco_original - desconto, 2)

# Interação com o usuário
try:
    preco = float(input("Digite o preço original do produto (em R$): "))
    porcentagem = float(input("Digite a porcentagem de desconto (%): "))

    valor_desconto = calcular_desconto(preco, porcentagem)
    preco_final = calcular_preco_final(preco, valor_desconto)

    # Exibição formatada
    print(f"\nResumo:")
    print(f"Preço original: R$ {preco:.2f}")
    print(f"Desconto de {porcentagem:.2f}%: R$ {valor_desconto:.2f}")
    print(f"Preço final com desconto: R$ {preco_final:.2f}")

except ValueError:
    print("Por favor, insira valores numéricos válidos.")