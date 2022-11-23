from os import system

def clear():
    system('cls')

def lerNotas(linha):
    a = open('notas.txt', 'r')
    notas = a.readlines()
    a.close()
    return notas[linha][2:]

def lerNome(numero):
    a = open('classe.txt', 'r')
    nomes = a.readlines()
    a.close()

    for i in nomes:
        if numero == i[0]:
            return i[2:].strip()

def eNumero(conv):
    try:
        conv = int(conv)
        return True
    except:
        return False

def main():
    clear()
    aluno = input('Digite o nome ou número do aluno que deseja ver a nota: ')
    clear()
    if eNumero(aluno):
        try:
            print(f'Notas de {lerNome(aluno)}: {lerNotas(int(aluno)-1)}')
        except:
            print('Numero de aluno desconhecido! Tente novamente')
            input('Enter para tentar novamente')
            main()
    else:
        cont = 0

        file = open('classe.txt', 'r')
        lista = file.readlines()
        file.close
        
        for i in lista:
            if aluno.capitalize() == i.strip()[2:]:
                print(f'Notas de {aluno.capitalize()}: {lerNotas(int(i[0])-1)}')
                input('Enter para buscar outro aluno ')
                main()
            else:
                cont += 1
        if cont == len(lista):
            print('Aluno não encontrado! Tente novamente')
            input('Enter para tentar novamente ')
            main()

main()
