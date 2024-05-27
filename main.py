
nomes = []

while True:
    try:
        # exibe a lista de funções
        print ('\nLISTA DE FUNÇÕES\n')
        print (f'Função 1 - Inserir pessoa na lista')
        print (f'Função 2 - Listar pessoas cadastradas')
        print (f'Função 3 - Pesquisar pelo nome de uma pessoa')
        print (f'Função 4 - Ordene a lista por ordem alfabetica')
        print (f'Função 5 - Atualizar nome')
        print (f'Função 6 - Deletar nome da lista')
        print (f'Função 7 - Sair do programa')

        # Escolhe a função
        funcao = int(input('Informe a função desejada: '))
        
        # executa a função selecionada
        match funcao:
            case 1:
                novo_nome = input('Informe o novo nome: ') 
                nomes.append(novo_nome)
                continue
            case 2:
                for nome in nomes:
                    print(nome)
                    continue
            case 3:
                # informa o nome a ser pesquisado
                nome_pesquisa = input('Digite o nome a ser pesquisado: ')
                if nome_pesquisa in nomes:
                    indice = nomes.index(nome_pesquisa)
                    print(f'Nome encontrado: {nome_pesquisa} no indice {indice}.')
                    continue
                else:
                    print(f'{nome_pesquisa} não encontrado na lista')
                    continue
            case 4:
                nomes.sort() # sort(reverse=True) para decrescente
                for nome in nomes:
                    print(nome)
                    continue
            case 5:
                # usuário informa o indice que deseja alterar
                indice = int(input('Informa o indice que deseja alterar: '))
                indice  -= 1

                #usuário informa o novo nome
                nomes[indice] = input('Informe o novo nome: ')

                #exibe a lista
                for nome in nomes:
                    print(nome)
                    continue
            case 6:
                # deletar um item da lista
                indice = int(input('Informe a posição do item que deseja excluir: '))
                indice -= 1
                del(nomes[indice])
                for nome in nomes:
                    print(nome)
                    continue
            case 7:
                # Sair do programa
                break
    except:
        break 


