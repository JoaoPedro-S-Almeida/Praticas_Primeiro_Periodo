def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nomeArquivo):
    try:
            a = open(nomeArquivo, 'wt+')
            a.close()
    except:
        print(f'Erro ao tentar criar o arquivo {nomeArquivo}!')
    else:
        print(f'Arquivo {nomeArquivo} foi criado com sucesso!\n')

def cadastrarJogo(nomeArquivo, nomeJogo, nomePlataforma):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print(f'Erro ao tentar abrir o arquivo {nomeArquivo}!')
    else:
        a.write(f'{nomeJogo} - {nomePlataforma}\n')
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print(f'Erro ao tentar ler o arquivo {nomeArquivo}!')
    else:
        print(a.read())
    finally:
        a.close

#programa principal
arquivo = 'jogos.txt'
if existeArquivo(arquivo): #Tenta abrir o arquivo
    print('Arquivo localizado no dispositivo.')
else:
    print('Arquivo inexistente.')
    criarArquivo(arquivo) #Cria o arquivo

while True:
    print('MENU - Cadastro de jogos')
    print('1 - Cadastrar novo jogo')
    print('2 - Listar jogos cadastrados')
    print('3 - Sair')

    op = valida_int('Escolha a opcao desejada: ', 1, 3)
    if (op == 1): #Novo jogo
        print('Opcao de cadastrar novo jogo selecionada!\n')
        nomeJogo = input('Nome do jogo: ')
        nomePlataforma = input('Nome da plataforma: ')
        cadastrarJogo(arquivo, nomeJogo, nomePlataforma)
        print(f'{nomeJogo} do(s) {nomePlataforma} foi cadastrado!\n')

    elif (op == 2): #Listar jogos
        print('Opcao de listar selecionada!\n')
        listarArquivo(arquivo)

    elif (op == 3): #Sair
        print('Encerrando...')
        break