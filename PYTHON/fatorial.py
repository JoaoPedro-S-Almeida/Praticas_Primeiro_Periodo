def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def fatorial(num):
    """Funcao que calcula fatorial de numero inteiro apresentado.
    
    Args:
        num: valor padrao;
        x: valor inserido por usuario.
    
    Returns:
        A fatoracao do numero inserido.
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num + 1, 1):
        fat *= i
    return fat

x = valida_int('Digite um valor para calcular a fatorial: ', 0, 9999)
print(f'{x}! = {fatorial(x)}')