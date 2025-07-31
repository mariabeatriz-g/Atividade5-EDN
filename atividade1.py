def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta com base no valor da conta e na porcentagem desejada.

    Parâmetros:
    - valor_conta (float): O valor total da conta
    - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)

    Retorna:
    - float: O valor da gorjeta calculada
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)