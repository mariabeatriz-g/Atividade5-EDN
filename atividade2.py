import string

def verificar_palindromo(texto: str) -> str:
    """
    Verifica se uma palavra ou frase é um palíndromo.

    Parâmetros:
    - texto (str): A palavra ou frase a ser verificada.

    Retorna:
    - str: "Sim" se for palíndromo, "Não" caso contrário.
    """
    # Remove espaços e pontuação, e converte para minúsculas
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())

    # Verifica se é igual ao reverso
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"