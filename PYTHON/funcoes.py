#sem funcao:
#print('|','__' * 10,'|')
#print('|','__' * 10,'|')
#print(' ' * 10, 'MENU')
#print('|','__' * 10,'|')
#print('|','__' * 10,'|')

#definicao da funcao:
def realce():
    print('|','__' * 10,'|')
    print('|','__' * 10,'|')

#programa principal 1:
realce()
print(' ' * 10, 'MENU')
realce()

#parametros em funcoes
def realce(s1):
    print('|','__' * 10,'|')
    print('|','__' * 10,'|')
    print(s1)
    print('|','__' * 10,'|')
    print('|','__' * 10,'|')

#programa principal 2:
realce('          MENU')

#outros parametros
def sub2(x, y):
    res = x - y
    print(res)

#programa principal 3:
sub2(5, 7)
sub2(7, 5)
sub2(y = 7, x = 5)

##parametros opcionais
def soma3(x, y, z): #sem parametros opcionais (menos de 3 valores = erro)
    res = x + y + z
    print(res)

def soma3(x = 0, y = 0, z = 0): #valor padrao para variavel (sem valor = 0, nesse caso)
    res = x + y + z
    print(res)

#programa principal 4:
soma3(1,2,3)
soma3(1,2)
soma3(1)
soma3()

#exercicio 1 - realce de palavras por input
def borda(texto_realce):
    tam = len(texto_realce)
    if tam:
        print('+','-' * tam,'+')
        print('|',texto_realce ,'|')
        print('+','-' * tam, '+')

#programa exercicio 1:
print('O que voce digitar, vou colocar dentro de uma caixa de realce!')
borda(input('Digite o que desejar: '))

##escopo de variaveis
def duzia():
    numeros = 12 #variavel local

#programa principal 5:
#duzia()
#print(numeros) #escopo global (=erro)

def duzia():
    print(numeros) #escopo local

numeros = 12 #variavel global
duzia()

def duzia():
    numeros = 12 #variavel local (!= numeros de pares)
    pares()
    print(numeros)

def pares():
    numeros = 6 #variavel local

#programa principal 6:
duzia()

def duzia():
    numeros = 12 #variavel local 'duzia'
    print('Numeros = ', numeros)

def pares():
    numeros = 6 #variavel local 'pares'
    print('Numeros = ', numeros)
    duzia()
    print('Numeros = ', numeros)

#programa principal 6:
numeros = 2 #variavel global
pares()
print('Numeros = ', numeros)

##instrucao global
def duzia():
    global numeros
    numeros = 12

#programa principal 7:
numeros = 6
duzia()
print(numeros)

def duzia():
    global numeros
    numeros = 12
    pares()

def pares():
    numeros = 6 #variavel local
    algorismos()

def algorismos():
    print(numeros)

#programa principal 8:
numeros = 4
duzia()
print(numeros)

#def duzia():
    #global ovos OU
    #print(numeros) #inverter com a variavel local abaixo
    #numeros = 12

#programa principal 9:
#numeros = 6
#duzia()

##retorno de valores em funcoes
def soma3(x = 0, y = 0, z = 0):
    res = x + y + z
    return res #retornando para o programa principal

#programa principal 10:
retornado = soma3(1,2,3)
print(retornado)

#forma alternativa simplificada
print(soma3(2,2))

#programa principal 11:
retornado1 = soma3(1,2,3)
retornado2 = soma3(1,2)
retornado3 = soma3()
print(f'Somatorios: {retornado1}, {retornado2} e {retornado3}.')

#exercicio 2:
def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam < min) or (tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
    return s1

#programa principal exercicio 2:
x = valida_string('Digite uma string (min. 10 e max. 30): ', 10, 30)
print('Voce digitou a string: {}. \nDado valido.'.format(x))

##recursos avancados com funcoes
#try/except para ValueError
while True:
    try:
        x = int(input('Por favor digite um numero: '))
        break
    except ValueError:
        print('Erro! Numero invalido. Tente novamente...')

#try/except/finally para ValueError e IndexError
i = 0
while True:
    try:
        nome = input('Digite o seu nome: ')
        ind = int(input('Digite um indice do seu nome: '))
        print(nome[ind])
        break
    except ValueError:
        print('Nome invalido. Tente novamente...')
    except IndexError:
        print('Indice invalido. Tente novamente...')
    finally:
        print(f'Essa foi sua tentativa {i}!')
        i += 1

#try/except para ZeroDivisionError e sem declarar erro
def div():
    while True:
        try:
            num1 = int(input('Digite um numero: '))
            num2 = int(input('Digite um numero: '))
            res = num1 / num2
        except ZeroDivisionError:
            print('Nao e possivel dividir por 0, tente novamente...')
        except:
            print('Algum erro foi detectado, tente novamente...')
        else:
            return res

#programa principal 12:
print('Seu resultado e: ',div())

##funcoes lambda
#calculo ao quadrado
res = lambda x: x * x
print(res(3))

#calculo de soma
soma = lambda x, y: x + y
print(soma(3,5))

#exercicio 3:
calc = lambda a, b: (a + 5) * b
print(calc(5,10))

##docstrings
def soma_help(x = 0, y = 0, z = 0):
    """Retorna o somatorio de tres valores.

    Args:
        x: Primeiro valor;
        y: Segundo valor;
        z: Terceiro valor.
    
    Returns:
        A soma de x, y e z.        
    """
    return  x + y + z

print(soma_help(5,7))
